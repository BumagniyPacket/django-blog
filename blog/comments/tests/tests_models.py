from django.test import TestCase

from blog.comments.models import Comment
from blog.posts.models import Post


class CommentTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='Test title 4 testing',
                            description='Some description',
                            content='Moar content')
        Comment.objects.create(post_id=1, author='Anon', text='lorem ipsum')

    # test verbose name
    def test_comment_post_verbose_name(self):
        comment = Comment.objects.get(pk=1)
        field_label = comment._meta.get_field('post').verbose_name
        self.assertEquals(field_label, 'Пост')

    def test_comment_author_verbose_name(self):
        comment = Comment.objects.get(pk=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'Автор')

    def test_comment_timestamp_verbose_name(self):
        comment = Comment.objects.get(pk=1)
        field_label = comment._meta.get_field('timestamp').verbose_name
        self.assertEquals(field_label, 'Время создания')

    def test_comment_text_verbose_name(self):
        comment = Comment.objects.get(pk=1)
        field_label = comment._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'Текст комментария')

    def test_comment_approved_verbose_name(self):
        comment = Comment.objects.get(pk=1)
        field_label = comment._meta.get_field('approved').verbose_name
        self.assertEquals(field_label, 'Подтвержден')

    # test field length
    def test_comment_author_max_length(self):
        comment = Comment.objects.get(pk=1)
        max_length = comment._meta.get_field('author').max_length
        self.assertEquals(max_length, 50)

    def test_comment_text_max_length(self):
        comment = Comment.objects.get(pk=1)
        max_length = comment._meta.get_field('text').max_length
        self.assertEquals(max_length, 1000)

    # test default value
    def test_comment_default_value_approved(self):
        comment = Comment.objects.get(pk=1)
        self.assertFalse(comment.approved)

    # test model methods
    def test_comment_str_method(self):
        comment = Comment.objects.get(pk=1)
        expected = 'Anon - lorem ipsum | approved: False'
        self.assertEquals(str(comment), expected)

    def test_comment_approve_link_method(self):
        comment = Comment.objects.get(pk=1)
        expected = '/comments/1/approve'
        self.assertEquals(comment.approve_link(), expected)

    def test_comment_delete_link_method(self):
        comment = Comment.objects.get(pk=1)
        expected = '/comments/1/delete'
        self.assertEquals(comment.delete_link(), expected)

    def test_comment_approve_method(self):
        comment = Comment.objects.get(pk=1)
        comment.approve()
        self.assertTrue(comment.approved)


