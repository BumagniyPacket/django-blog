from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.articles.models import Article


class ArticleViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='u',
            email='u@DOMAIN.com',
            password='password',
        )
        self.user.clean()
        self.client = APIClient()

        for i in range(25):
            Article.objects.create(
                user=self.user,
                title=f'some title {i}',
                description='some description',
                content='some content',

            )

    def test_articles_list_OK(self):
        self.client.credentials()
        response = self.client.get(
            reverse('v1:list'),
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_articles_retrieve_OK(self):
        self.client.credentials()
        response = self.client.get(
            reverse(
                'v1:article-detail',
                kwargs={'pk': Article.objects.first().pk}
            ),
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
