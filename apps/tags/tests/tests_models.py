from django.test import TestCase

from apps.tags.models import Tag


class TagTestCase(TestCase):
    def setUp(self):
        self.tag_name = 'tag name'
        self.tag = Tag.objects.create(
            name=self.tag_name
        )

    def test_str_method(self):
        self.assertEqual(self.tag_name, str(self.tag))
