from django.test import TestCase

from blog.articles.models import Article


class ArticleTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Article.objects.create(title='Test title 4 testing',
                               description='Some description',
                               content='Moar content')

    # test verbose name
    def test_article_user_verbose_name(self):
        article = Article.objects.get(pk=1)
        field_label = article._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'Пользователь')

    def test_article_title_verbose_name(self):
        article = Article.objects.get(pk=1)
        field_label = article._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Заголовок поста')

    def test_article_image_verbose_name(self):
        article = Article.objects.get(pk=1)
        field_label = article._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'Ссылка на изображение')

    def test_article_description_verbose_name(self):
        article = Article.objects.get(pk=1)
        field_label = article._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание поста')

    def test_article_slug_verbose_name(self):
        article = Article.objects.get(pk=1)
        field_label = article._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'Слаг')

    def test_article_content_verbose_name(self):
        article = Article.objects.get(pk=1)
        field_label = article._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'Контент')

    def test_article_draft_verbose_name(self):
        article = Article.objects.get(pk=1)
        field_label = article._meta.get_field('draft').verbose_name
        self.assertEquals(field_label, 'В процессе написания')

    def test_article_timestamp_verbose_name(self):
        article = Article.objects.get(pk=1)
        field_label = article._meta.get_field('timestamp').verbose_name
        self.assertEquals(field_label, 'Время создания')

    def test_article_updated_verbose_name(self):
        article = Article.objects.get(pk=1)
        field_label = article._meta.get_field('updated').verbose_name
        self.assertEquals(field_label, 'Обновлен')

    def test_article_views_verbose_name(self):
        article = Article.objects.get(pk=1)
        field_label = article._meta.get_field('views').verbose_name
        self.assertEquals(field_label, 'Просмотров')

    # test fields length
    def test_article_title_max_length(self):
        article = Article.objects.get(pk=1)
        max_length = article._meta.get_field('title').max_length
        self.assertEquals(max_length, 120)

    def test_article_description_max_length(self):
        article = Article.objects.get(pk=1)
        max_length = article._meta.get_field('description').max_length
        self.assertEquals(max_length, 400)

    # test article methods
    def test_article_str_method(self):
        article = Article.objects.get(pk=1)
        expected = 'Test title 4 testing'
        self.assertEquals(str(article), expected)

    def test_article_get_absolute_url_method(self):
        article = Article.objects.get(pk=1)
        expected = '/test-title-4-testing'
        self.assertEquals(article.get_absolute_url(), expected)

    def test_article_get_delete_url_method(self):
        article = Article.objects.get(pk=1)
        expected = '/test-title-4-testing/delete'
        self.assertEquals(article.get_delete_url(), expected)

    def test_article_get_edit_url_method(self):
        article = Article.objects.get(pk=1)
        expected = '/test-title-4-testing/edit'
        self.assertEquals(article.get_edit_url(), expected)

    def test_article_add_view_method(self):
        article = Article.objects.get(pk=1)
        article.add_view()
        self.assertEquals(article.views, 1)

    def test_article_add_view_one_more_method(self):
        article = Article.objects.get(pk=1)
        article.add_view()
        article.add_view()
        self.assertEquals(article.views, 2)

    def test_article_get_view_method(self):
        article = Article.objects.get(pk=1)
        self.assertEquals(article.get_views(), 0)

    def test_article_get_view_method_not_null(self):
        article = Article.objects.get(pk=1)
        article.add_view()
        self.assertEquals(article.get_views(), 1)

    def test_article_slug(self):
        article = Article.objects.get(pk=1)
        expected = 'test-title-4-testing'
        self.assertEquals(article.slug, expected)

    def test_article_slug_rus(self):
        Article.objects.create(title='Тестовый заголовок')
        article = Article.objects.get(pk=2)
        expected = 'тестовый-заголовок'
        self.assertEquals(article.slug, expected)

    def test_article_slug_if_exist(self):
        Article.objects.create(title='Test title 4 testing')
        article = Article.objects.get(pk=2)
        expected = 'test-title-4-testing-1'
        self.assertEquals(article.slug, expected)

    # test manager methods
    def test_article_manager_published_method_view_all_length(self):
        published = Article.objects.published()
        self.assertEquals(len(published), 1)

    def test_article_manager_published_method_view_(self):
        Article.objects.create(title='Test title 4 testing')
        published = Article.objects.published()
        self.assertEquals(len(published), 2)

    def test_article_manager_published_method_which_false(self):
        article = Article.objects.get(pk=1)
        article.draft = True
        article.save()
        published = Article.objects.published()
        self.assertEquals(len(published), 0)

    def test_article_manager_published_method_which_some_false(self):
        Article.objects.create(draft=True, title='Test title 4 testing')
        published = Article.objects.published()
        self.assertEquals(len(published), 1)
