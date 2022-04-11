from django.urls import include, path, re_path

from backend_challenge import views
from rest_framework import routers

# template tagging
app_name = 'backend_challenge'

router = routers.DefaultRouter()
router.register(r'quotes', views.QuoteViewSet)

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
