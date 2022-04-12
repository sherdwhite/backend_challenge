from django.urls import path

from quotes.views import AllQuotesViewSet, QuotesDetailViewSet, CreateQuoteViewSet

urlpatterns = [
    path('quotes/', AllQuotesViewSet.as_view({'get': 'list'})),
    path('quote/<int:pk>/', QuotesDetailViewSet.as_view()),
    path('create-quote/', CreateQuoteViewSet.as_view()),
]
