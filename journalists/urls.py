from django.urls import path
from journalists import views
from rest_framework.routers import DefaultRouter


app_name = 'journalists'


router = DefaultRouter()
router.register(r'journalists',
                views.JournalistModelViewSet,
                basename='journalists_model')

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('apiview/journalists/',
         views.JournalistAPIView.as_view(),
         name='journalists_api'),
]

urlpatterns += router.urls
