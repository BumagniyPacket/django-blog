from django.test import TestCase

from blog.posts.forms import PostForm
from blog.posts.models import Post


class PostFormTest(TestCase):
    # test labels
    def test_post_form_title_field_label(self):
        form = PostForm()
        self.assertEquals(form.fields['title'].label, 'Заголовок поста')

    def test_post_form_image_field_label(self):
        form = PostForm()
        self.assertEquals(form.fields['image'].label, 'Ссылка на изображение')

    def test_post_form_description_field_label(self):
        form = PostForm()
        self.assertEquals(form.fields['description'].label, 'Описание поста')

    def test_post_form_content_field_label(self):
        form = PostForm()
        self.assertIsNone(form.fields['content'].label)

    def test_post_form_draft_field_label(self):
        form = PostForm()
        self.assertEquals(form.fields['draft'].label, 'В процессе написания')

    # valid data
    def test_post_form_normal_length_title(self):
        form_data = {
            'title': 'Normal length',
            'description': 'Description',
            'content': 'Some content'
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()

    def test_post_form_save(self):
        form_data = {
            'title': 'Normal length',
            'description': 'Description',
            'content': 'Some content'
        }
        form = PostForm(data=form_data)
        form.save()
        post = Post.objects.get(pk=1)
        self.assertEquals(post.title, form_data['title'])
        self.assertEquals(post.description, form_data['description'])
        self.assertEquals(post.content, form_data['content'])

    # invalid data
    def test_post_form_invalid_blank_title(self):
        form_data = {
            'title': None,
            'description': 'Description',
            'content': 'Some content'
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_post_form_invalid_blank_description(self):
        form_data = {
            'title': 'Normal length',
            'description': None,
            'content': 'Some content'
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_post_form_invalid_blank_content(self):
        form_data = {
            'title': 'Normal length',
            'description': 'Description',
            'content': None
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_post_form_invalid_length_title(self):
        form_data = {
            'title': 'Normal length' * 20,
            'description': 'Description',
            'content': 'Some content'
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
