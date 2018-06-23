from django.contrib.auth.models import User
from django.test import TestCase

from apps.articles.models import Article, Tag
from apps.categories.models import Category


class ArticleTestCase(TestCase):
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
        self.article = Article.objects.create(
            user=self.user,
            title='Test title 4 testing',
            description='Some description',
            content='Moar content',
            category=self.category
        )

    # test verbose name
    def test_article_user_verbose_name(self):
        article = self.article
        field_label = article._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'Пользователь')

    def test_article_title_verbose_name(self):
        article = self.article
        field_label = article._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Заголовок поста')

    def test_article_image_verbose_name(self):
        article = self.article
        field_label = article._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'Изображение')

    def test_article_description_verbose_name(self):
        article = self.article
        field_label = article._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание поста')

    def test_article_slug_verbose_name(self):
        article = self.article
        field_label = article._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'Слаг')

    def test_article_content_verbose_name(self):
        article = self.article
        field_label = article._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'Контент')

    def test_article_draft_verbose_name(self):
        article = self.article
        field_label = article._meta.get_field('draft').verbose_name
        self.assertEquals(field_label, 'В процессе написания')

    def test_article_timestamp_verbose_name(self):
        article = self.article
        field_label = article._meta.get_field('timestamp').verbose_name
        self.assertEquals(field_label, 'Время создания')

    def test_article_updated_verbose_name(self):
        article = self.article
        field_label = article._meta.get_field('updated').verbose_name
        self.assertEquals(field_label, 'Обновлен')

    def test_article_views_verbose_name(self):
        article = self.article
        field_label = article._meta.get_field('views').verbose_name
        self.assertEquals(field_label, 'Просмотров')

    # test fields length
    def test_article_title_max_length(self):
        article = self.article
        max_length = article._meta.get_field('title').max_length
        self.assertEquals(max_length, 120)

    def test_article_description_max_length(self):
        article = self.article
        max_length = article._meta.get_field('description').max_length
        self.assertEquals(max_length, 400)

    # test article methods
    def test_article_str_method(self):
        article = self.article
        expected = 'Test title 4 testing'
        self.assertEquals(str(article), expected)

    # def test_article_get_absolute_url_method(self):
    #     article = self.article
    #     expected = '/test-title-4-testing'
    #     self.assertEquals(article.get_absolute_url, expected)

    def test_article_add_view_method(self):
        article = self.article
        article.add_view()
        self.assertEquals(article.views, 1)

    def test_article_add_view_one_more_method(self):
        article = self.article
        article.add_view()
        article.add_view()
        self.assertEquals(article.views, 2)

    def test_article_get_view_method(self):
        article = self.article
        self.assertEquals(article.get_views(), 0)

    def test_article_get_view_method_not_null(self):
        article = self.article
        article.add_view()
        self.assertEquals(article.get_views(), 1)

    def test_article_slug(self):
        article = self.article
        expected = 'test-title-4-testing'
        self.assertEquals(article.slug, expected)

    def test_article_slug_rus(self):
        article = Article.objects.create(
            user=self.user,
            title='Тестовый заголовок',
            description='Some description',
            content='Moar content',
            category=self.category
        )
        article = Article.objects.get(pk=article.pk)
        expected = 'тестовый-заголовок'
        self.assertEquals(article.slug, expected)

    def test_article_slug_if_exist(self):
        article = Article.objects.create(
            user=self.user,
            title='Test title 4 testing',
            description='Some description',
            content='Moar content',
            category=self.category
        )
        article = Article.objects.get(pk=article.pk)
        expected = 'test-title-4-testing-1'
        self.assertEquals(article.slug, expected)

    # test manager methods
    def test_article_manager_published_method_view_all_length(self):
        published = Article.objects.published()
        self.assertEquals(len(published), 1)

    def test_article_manager_published_method_view_(self):
        Article.objects.create(
            user=self.user,
            title='Test title 4 testing',
            description='Some description',
            content='Moar content',
            category=self.category
        )
        published = Article.objects.published()
        self.assertEquals(len(published), 2)

    def test_article_manager_published_method_which_false(self):
        article = self.article
        article.draft = True
        article.save()
        published = Article.objects.published()
        self.assertEquals(len(published), 0)

    def test_article_manager_published_method_which_some_false(self):
        Article.objects.create(
            user=self.user,
            title='Test title 4 testing',
            description='Some description',
            content='Moar content',
            draft=True,
            category=self.category
        )
        published = Article.objects.published()
        self.assertEquals(len(published), 1)


class TagTestCase(TestCase):
    def setUp(self):
        self.tag_name = 'tag name'
        self.tag = Tag.objects.create(
            name=self.tag_name
        )

    def test_str_method(self):
        self.assertEqual(self.tag_name, str(self.tag))
