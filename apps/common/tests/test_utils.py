from django.contrib.auth.models import User
from django.test import TestCase

from apps.articles.models import Article
from apps.categories.models import Category
from apps.common.utils import create_slug


class UtilsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='u',
            email='u@DOMAIN.com',
            password='password',
        )
        self.category = Category.objects.create(
            name='Category name',
            description='Some description'
        )
        self.article_title = 'Test title 4 testing'
        self.article = self.create_article(self.article_title)

    def create_article(self, title):
        return Article.objects.create(
            user=self.user,
            title=title,
            description='Some description',
            content='Moar content',
            category=self.category
        )

    def test_default_slug(self):
        expected_slug = 'test-title-4-testing'
        self.assertEqual(expected_slug, self.article.slug)

    def test_cyrillic_slug(self):
        title = 'Просто рушн слаг'
        expected_slug = 'просто-рушн-слаг'
        article = self.create_article(title)
        self.assertEqual(expected_slug, article.slug)

    def test_exist_slug(self):
        expected_slug = 'test-title-4-testing-1'
        article = self.create_article(self.article_title)
        self.assertEqual(expected_slug, article.slug)

    def test_exist_slug_lag(self):
        expected_slug = 'test-title-4-testing-1'
        slug = create_slug(self.article, expected_slug)
        self.assertEqual(expected_slug, slug)
