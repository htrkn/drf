from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from API import views
urlpatterns = [
    url(r'^root/', admin.site.urls),
    url(r'^kurlar/', views.KurListesi.as_view()),
    url(r'^kurlar/', views.KurListesi.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)