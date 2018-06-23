from django.test import TestCase

from apps.categories.models import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category_name = 'category name'
        self.category = Category.objects.create(
            name=self.category_name,
            description='some description'
        )

    def test_str_method(self):
        self.assertEqual(self.category_name, str(self.category))
