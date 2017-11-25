from unittest.mock import patch

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from blog.comments.models import Comment
from blog.articles.models import Article


class ArticleListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='12345', is_superuser=True)
        test_user.save()
        # Create 13 Articles for pagination tests
        number_of_articles = 13
        for Article_num in range(number_of_articles):
            Article.objects.create(title='Test title', description='desc', content='content')
        # Create 2 Articles with draft=false
        Article.objects.create(title='Test title', description='desc', content='content', draft=True)
        Article.objects.create(title='Test title', description='desc', content='content', draft=True)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('articles:list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('articles:list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'articles/article_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('articles:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEquals(len(resp.context['object_list']), 10)

    def test_lists_all_Articles(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('articles:list') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertEquals(len(resp.context['object_list']), 3)

    def test_lists_with_search_field_with_no_results(self):
        resp = self.client.get(reverse('articles:list') + '?q=lorem')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertFalse(resp.context['is_paginated'])
        self.assertEquals(len(resp.context['object_list']), 0)

    def test_lists_with_search_field_with_results(self):
        Article.objects.create(title='Test title', description='Lorem', content='Lorem')
        resp = self.client.get(reverse('articles:list') + '?q=lorem')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertFalse(resp.context['is_paginated'])
        self.assertEquals(len(resp.context['object_list']), 1)

    def test_list_with_draft_articles_authorized_user(self):
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('articles:list') + '?page=2')
        self.assertEquals(len(resp.context['object_list']), 5)


class ArticleDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='12345', is_superuser=True)
        test_user.save()

        Article.objects.create(title='Test title', description='desc', content='content')
        Article.objects.create(title='Test title', description='desc', content='content', draft=True)

        Comment.objects.create(article_id=1, text='test')
        Comment.objects.create(article_id=1, text='test')
        Comment.objects.create(article_id=1, text='test', approved=True)

    def test_view_article_not_in_draft_unauthorised_user(self):
        article = Article.objects.get(pk=1)
        resp = self.client.get(reverse('articles:detail', kwargs={'slug': article.slug}))
        self.assertEqual(resp.status_code, 200)

    def test_view_article_in_draft_unauthorised_user(self):
        article = Article.objects.get(pk=2)
        resp = self.client.get(reverse('articles:detail', kwargs={'slug': article.slug}))
        self.assertEqual(resp.status_code, 404)

    def test_view_article_not_in_draft_authorised_user(self):
        article = Article.objects.get(pk=1)
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('articles:detail', kwargs={'slug': article.slug}))
        self.assertEqual(resp.status_code, 200)

    def test_view_article_in_draft_authorised_user(self):
        article = Article.objects.get(pk=2)
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('articles:detail', kwargs={'slug': article.slug}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        article = Article.objects.get(pk=1)
        resp = self.client.get(reverse('articles:detail', kwargs={'slug': article.slug}))
        self.assertTemplateUsed(resp, 'articles/article_detail.html')
        self.assertTemplateUsed(resp, 'comments/comments_form.html')

    def test_view_comments_is_one_unauthorized_user(self):
        article = Article.objects.get(pk=1)
        resp = self.client.get(reverse('articles:detail', kwargs={'slug': article.slug}))
        self.assertEquals(len(resp.context['comments']), 1)

    def test_view_comments_is_three_authorized_user(self):
        article = Article.objects.get(pk=1)
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('articles:detail', kwargs={'slug': article.slug}))
        self.assertEquals(len(resp.context['comments']), 3)

    def test_view_add_view_method_call(self):
        article = Article.objects.get(pk=1)
        with patch('blog.articles.models.Article.add_view') as add_view:
            self.client.get(reverse('articles:detail', kwargs={'slug': article.slug}))
        self.assertEquals(add_view.call_count, 1)


class ArticleCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='12345', is_superuser=True)
        test_user.save()

    def test_create_article_unauthorised_user(self):
        resp = self.client.get(reverse('articles:create'))
        self.assertEqual(resp.status_code, 302)

    def test_create_article_authorised_user(self):
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('articles:create'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('articles:create'))
        self.assertTemplateUsed(resp, 'articles/article_form.html')


class ArticleEditViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Article.objects.create(title='Test title', description='desc', content='content')

        test_user = User.objects.create_user(username='testuser', password='12345', is_superuser=True)
        test_user.save()

    def test_edit_article_unauthorised_user(self):
        article = Article.objects.get(pk=1)
        resp = self.client.get(reverse('articles:edit', kwargs={'slug': article.slug}))
        self.assertEqual(resp.status_code, 302)

    def test_edit_article_authorised_user(self):
        article = Article.objects.get(pk=1)
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('articles:edit', kwargs={'slug': article.slug}))
        self.assertEqual(resp.status_code, 200)

    def test_edit_uses_correct_template(self):
        article = Article.objects.get(pk=1)
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('articles:edit', kwargs={'slug': article.slug}))
        self.assertTemplateUsed(resp, 'articles/article_form.html')


class ArticleDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Article.objects.create(title='Test title', description='desc', content='content')

        test_user = User.objects.create_user(username='testuser', password='12345', is_superuser=True)
        test_user.save()

    def test_delete_article_unauthorised_user(self):
        article = Article.objects.get(pk=1)
        resp = self.client.get(reverse('articles:delete', kwargs={'slug': article.slug}))
        self.assertEqual(resp.status_code, 302)

    def test_delete_article_authorised_user(self):
        article = Article.objects.get(pk=1)
        self.client.login(username='testuser', password='12345')
        resp = self.client.get(reverse('articles:delete', kwargs={'slug': article.slug}))
        self.assertEqual(resp.status_code, 200)
