"""yunquan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from collect.views import AddCollect, ajax_dict, FindCollect, ReturnCollect
import xadmin
from django.conf import settings
from django.conf.urls.static import static

from moments.views import AddMomentsView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^collect/add/', AddCollect.as_view()),
    url(r'^collect/find/', FindCollect.as_view()),
    url(r'^collect/return/', ReturnCollect.as_view()),
    url(r'^collect/ceshi/', ajax_dict),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'moments/add/', AddMomentsView.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


