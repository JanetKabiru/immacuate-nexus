from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from . import views


urlpatterns=[
    re_path('^$',views.home,name = 'home'),
    re_path('^events$',views.events,name = 'events'),
    re_path('^contacts$', views.ContactFormView.as_view(), name='contacts'),
    re_path('^contactpush$', views.contactPush, name='contactpush'),    
    re_path('^courses$',views.courses,name = 'courses'),
    re_path('^admissions$',views.admissions,name = 'admissions'),
    re_path('^about$',views.about,name = 'about'),
    re_path('^business',views.business,name = 'business'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)