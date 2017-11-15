from unittest.mock import patch

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from blog.comments.models import Comment
from blog.posts.models import Post


class PostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='12345', is_superuser=True)
        test_user.save()
        # Create 13 Posts for pagination tests
        number_of_posts = 13
        for Post_num in range(number_of_posts):
            Post.objects.create(title='Test title', description='desc', content='content')
        # Create 2 Posts with draft=false
        Post.objects.create(title='Test title', description='desc', content='content', draft=True)
        Post.objects.create(title='Test title', description='desc', content='content', draft=True)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('posts:list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('posts:list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'posts/post_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('posts:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEquals(len(resp.context['object_list']), 10)

    def test_lists_all_Posts(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('posts:list') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEquals(len(resp.context['object_list']), 3)

    def test_lists_with_search_field_with_no_results(self):
        resp = self.client.get(reverse('posts:list') + '?q=lorem')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertFalse(resp.context['is_paginated'])
        self.assertEquals(len(resp.context['object_list']), 0)

    def test_lists_with_search_field_with_results(self):
        Post.objects.create(title='Test title', description='Lorem', content='Lorem')
        resp = self.client.get(reverse('posts:list') + '?q=lorem')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertFalse(resp.context['is_paginated'])
        self.assertEquals(len(resp.context['object_list']), 1)

    def test_list_with_draft_posts_authorized_user(self):
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('posts:list') + '?page=2')
        self.assertEquals(len(resp.context['object_list']), 5)


class PostDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='12345', is_superuser=True)
        test_user.save()

        Post.objects.create(title='Test title', description='desc', content='content')
        Post.objects.create(title='Test title', description='desc', content='content', draft=True)

        Comment.objects.create(post_id=1, text='test')
        Comment.objects.create(post_id=1, text='test')
        Comment.objects.create(post_id=1, text='test', approved=True)

    def test_view_post_not_in_draft_unauthorised_user(self):
        post = Post.objects.get(pk=1)
        resp = self.client.get(reverse('posts:detail', kwargs={'slug': post.slug}))
        self.assertEqual(resp.status_code, 200)

    def test_view_post_in_draft_unauthorised_user(self):
        post = Post.objects.get(pk=2)
        resp = self.client.get(reverse('posts:detail', kwargs={'slug': post.slug}))
        self.assertEqual(resp.status_code, 404)

    def test_view_post_not_in_draft_authorised_user(self):
        post = Post.objects.get(pk=1)
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('posts:detail', kwargs={'slug': post.slug}))
        self.assertEqual(resp.status_code, 200)

    def test_view_post_in_draft_authorised_user(self):
        post = Post.objects.get(pk=2)
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('posts:detail', kwargs={'slug': post.slug}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        post = Post.objects.get(pk=1)
        resp = self.client.get(reverse('posts:detail', kwargs={'slug': post.slug}))
        self.assertTemplateUsed(resp, 'posts/post_detail.html')
        self.assertTemplateUsed(resp, 'comments/comments_form.html')

    def test_view_comments_is_one_unauthorized_user(self):
        post = Post.objects.get(pk=1)
        resp = self.client.get(reverse('posts:detail', kwargs={'slug': post.slug}))
        self.assertEquals(len(resp.context['comments']), 1)

    def test_view_comments_is_three_authorized_user(self):
        post = Post.objects.get(pk=1)
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('posts:detail', kwargs={'slug': post.slug}))
        self.assertEquals(len(resp.context['comments']), 3)

    def test_view_add_view_method_call(self):
        post = Post.objects.get(pk=1)
        with patch('blog.posts.models.Post.add_view') as add_view:
            self.client.get(reverse('posts:detail', kwargs={'slug': post.slug}))
        self.assertEquals(add_view.call_count, 1)


class PostCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='12345', is_superuser=True)
        test_user.save()

    def test_create_post_unauthorised_user(self):
        resp = self.client.get(reverse('posts:create'))
        self.assertEqual(resp.status_code, 302)

    def test_create_post_authorised_user(self):
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('posts:create'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('posts:create'))
        self.assertTemplateUsed(resp, 'posts/post_form.html')


class PostEditViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='Test title', description='desc', content='content')

        test_user = User.objects.create_user(username='testuser', password='12345', is_superuser=True)
        test_user.save()

    def test_edit_post_unauthorised_user(self):
        post = Post.objects.get(pk=1)
        resp = self.client.get(reverse('posts:edit', kwargs={'slug': post.slug}))
        self.assertEqual(resp.status_code, 302)

    def test_edit_post_authorised_user(self):
        post = Post.objects.get(pk=1)
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('posts:edit', kwargs={'slug': post.slug}))
        self.assertEqual(resp.status_code, 200)

    def test_edit_uses_correct_template(self):
        post = Post.objects.get(pk=1)
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('posts:edit', kwargs={'slug': post.slug}))
        self.assertTemplateUsed(resp, 'posts/post_form.html')


class PostDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='Test title', description='desc', content='content')

        test_user = User.objects.create_user(username='testuser', password='12345', is_superuser=True)
        test_user.save()

    def test_delete_post_unauthorised_user(self):
        post = Post.objects.get(pk=1)
        resp = self.client.get(reverse('posts:delete', kwargs={'slug': post.slug}))
        self.assertEqual(resp.status_code, 302)

    def test_delete_post_authorised_user(self):
        post = Post.objects.get(pk=1)
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('posts:delete', kwargs={'slug': post.slug}))
        self.assertEqual(resp.status_code, 200)
