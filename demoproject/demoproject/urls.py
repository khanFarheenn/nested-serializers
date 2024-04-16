from django.contrib import admin
from django.urls import path, include
from singerapp import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register('singers', views.SingerViewSet, basename='singer')
# router.register('songs', views.SongViewSet, basename='song')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
# ]
#====== other way to use nestedserializer==============

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('singerapp.urls')),
]