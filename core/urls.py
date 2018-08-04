"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin_urls = [
    url(r'^admin/', include(admin.site.urls)),
    # Django JET URLS
    url(r'^jet/', include('jet.urls', 'jet')),
    # Django JET dashboard URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^filer/', include('filer.urls')),
]

custom_urls = [
    url(r'^api/v1/', include([
        url(r'^article/', include('apps.articles.urls')),
        url(r'^category/', include('apps.categories.urls')),
        url(r'^tag/', include('apps.tags.urls')),
    ], namespace='v1')),
    url(
        r'^blog/',
        include('apps.frontend_blog.urls', namespace='frontend-blog')
    ),
    url(
        '', include('apps.frontend_main.urls', namespace='frontend-main')
    ),
]

editor_urls = [
    # https://ckeditor.com/legal/ckeditor-oss-license/
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]


urlpatterns = admin_urls + custom_urls + editor_urls


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
