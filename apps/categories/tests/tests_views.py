from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.categories.models import Category


class CategoryViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.length = 5
        for i in range(self.length):
            self.category = Category.objects.create(
                name=f'Category name {i}',
                description='Some description'
            )

    def test_articles_list_OK(self):
        response = self.client.get(
            reverse('v1:category-list'),
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_articles_list_length(self):
        response = self.client.get(
            reverse('v1:category-list'),
            format='json',
        )
        data = response.data
        self.assertEqual(len(data), self.length)
