from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from filer.tests import create_image, DjangoFile
from filer.models import Folder, Image
from rest_framework import status
from rest_framework.test import APIClient

from apps.articles.models import Article
from apps.categories.models import Category


class ArticleViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='u',
            email='u@DOMAIN.com',
            password='password',
        )
        self.user.clean()
        self.client = APIClient()
        self.category = Category.objects.create(
            name='Category name',
            description='Some description'
        )

        for i in range(25):
            Article.objects.create(
                user=self.user,
                title=f'some title {i}',
                description='some description',
                content='some content',
                category=self.category
            )

    def test_articles_list_OK(self):
        self.client.credentials()
        response = self.client.get(
            reverse('frontend:list'),
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_articles_detail_OK(self):
        self.client.credentials()
        response = self.client.get(
            reverse(
                'frontend:blog-article-detail',
                kwargs={'pk': Article.objects.first().pk}
            ),
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_random_background_404(self):
        response = self.client.get(
            reverse(
                'frontend:blog-background',
            ),
            format='json',
        )
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_random_background_OK(self):
        self.folder = Folder.objects.create(name='backgrounds')
        #
        # # from filer.models import Folder, Image, tools
        # # from django.core.files import File
        # from core.settings.base import FILER_CANONICAL_URL
        # import os
        # #
        # self.image_name = 'some-name.jpg'
        #
        # self.file = File(open(self.image_name, 'rb'), name=self.image_name)
        # file = Image.objects.create(original_filename='file3',
        #                             file=self.file, folder=self.folder)
        #
        # self.filename = os.path.join('/media/', self.image_name)
        # file.save(self.filename, 'JPEG')
        #
        #
        # file = create_image()
        # filename = 'some-name.jpg'
        # file_obj = File(file, name=filename)
        # self.image = Image.objects.get_or_create(
        #     original_filename=filename,
        #     file=file_obj,
        #     folder=self.folder,
        #     is_public=True)

        from tempfile import mktemp
        import os

        filename = mktemp()

        # self.img = create_image()
        # self.image_name = 'test_file.jpg'
        # self.filename = os.path.join(filename, self.image_name)
        # self.img.save(self.filename, 'JPEG')
        #
        # file_obj = DjangoFile(open(self.filename, 'rb'), name=self.image_name)
        # image = Image.objects.create(
        #     original_filename=self.image_name,
        #     file=file_obj,
        #     folder=self.folder
        # )
        from filer.tests.models import FilerApiTests

        tmp = FilerApiTests()
        image = tmp.create_filer_image()

        # self.folder.files
        image.folder = self.folder
        image.save()

        response = self.client.get(
            reverse(
                'frontend:blog-background',
            ),
            format='json',
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
