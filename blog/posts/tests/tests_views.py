from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

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

    # test draft position
    def test(self):
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('posts:list') + '?page=2')
        self.assertEquals(len(resp.context['object_list']), 5)
