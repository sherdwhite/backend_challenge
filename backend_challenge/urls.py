from django.urls import include, path, re_path

from backend_challenge import views

# template tagging
app_name = 'backend_challenge'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    path('', include('quotes.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
