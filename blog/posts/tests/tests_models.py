from django.test import TestCase

from blog.posts.models import Post


class PostTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='Test title 4 testing',
                            description='Some description',
                            content='Moar content')

    # test verbose name
    def test_post_user_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_label = post._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'Пользователь')

    def test_post_title_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Заголовок поста')

    def test_post_image_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_label = post._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'Ссылка на изображение')

    def test_post_description_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_label = post._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание поста')

    def test_post_slug_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_label = post._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'Слаг')

    def test_post_content_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_label = post._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'Контент')

    def test_post_draft_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_label = post._meta.get_field('draft').verbose_name
        self.assertEquals(field_label, 'В процессе написания')

    def test_post_timestamp_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_label = post._meta.get_field('timestamp').verbose_name
        self.assertEquals(field_label, 'Время создания')

    def test_post_updated_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_label = post._meta.get_field('updated').verbose_name
        self.assertEquals(field_label, 'Обновлен')

    def test_post_views_verbose_name(self):
        post = Post.objects.get(pk=1)
        field_label = post._meta.get_field('views').verbose_name
        self.assertEquals(field_label, 'Просмотров')

    # test fields length
    def test_post_title_max_length(self):
        post = Post.objects.get(pk=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 120)

    def test_post_description_max_length(self):
        post = Post.objects.get(pk=1)
        max_length = post._meta.get_field('description').max_length
        self.assertEquals(max_length, 400)

    # test post methods
    def test_post_str_method(self):
        post = Post.objects.get(pk=1)
        expected = 'Test title 4 testing'
        self.assertEquals(str(post), expected)

    def test_post_get_absolute_url_method(self):
        post = Post.objects.get(pk=1)
        expected = '/test-title-4-testing'
        self.assertEquals(post.get_absolute_url(), expected)

    def test_post_get_delete_url_method(self):
        post = Post.objects.get(pk=1)
        expected = '/test-title-4-testing/delete'
        self.assertEquals(post.get_delete_url(), expected)

    def test_post_get_edit_url_method(self):
        post = Post.objects.get(pk=1)
        expected = '/test-title-4-testing/edit'
        self.assertEquals(post.get_edit_url(), expected)

    def test_post_add_view_method(self):
        post = Post.objects.get(pk=1)
        post.add_view()
        self.assertEquals(post.views, 1)

    def test_post_add_view_one_more_method(self):
        post = Post.objects.get(pk=1)
        post.add_view()
        post.add_view()
        self.assertEquals(post.views, 2)

    def test_post_get_view_method(self):
        post = Post.objects.get(pk=1)
        self.assertEquals(post.get_views(), 0)

    def test_post_get_view_method_not_null(self):
        post = Post.objects.get(pk=1)
        post.add_view()
        self.assertEquals(post.get_views(), 1)

    def test_post_slug(self):
        post = Post.objects.get(pk=1)
        expected = 'test-title-4-testing'
        self.assertEquals(post.slug, expected)

    def test_post_slug_rus(self):
        Post.objects.create(title='Тестовый заголовок')
        post = Post.objects.get(pk=2)
        expected = 'тестовый-заголовок'
        self.assertEquals(post.slug, expected)

    def test_post_slug_if_exist(self):
        Post.objects.create(title='Test title 4 testing')
        post = Post.objects.get(pk=2)
        expected = 'test-title-4-testing-1'
        self.assertEquals(post.slug, expected)

    # test manager methods
    def test_post_manager_published_method_view_all_length(self):
        published = Post.objects.published()
        self.assertEquals(len(published), 1)

    def test_post_manager_published_method_view_(self):
        Post.objects.create(title='Test title 4 testing')
        published = Post.objects.published()
        self.assertEquals(len(published), 2)

    def test_post_manager_published_method_which_false(self):
        post = Post.objects.get(pk=1)
        post.draft = True
        post.save()
        published = Post.objects.published()
        self.assertEquals(len(published), 0)

    def test_post_manager_published_method_which_some_false(self):
        Post.objects.create(draft=True, title='Test title 4 testing')
        published = Post.objects.published()
        self.assertEquals(len(published), 1)
