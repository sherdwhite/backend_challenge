from django.urls import include, path, re_path

from quotes.views import AllQuotesViewSet, QuotesDetailViewSet, CreateQuoteViewSet
from backend_challenge import views

urlpatterns = [
    path('quotes/', AllQuotesViewSet.as_view({'get': 'list'})),
    path('quote/<int:pk>/', QuotesDetailViewSet.as_view()),
    path('create-quote/', CreateQuoteViewSet.as_view()),
]
