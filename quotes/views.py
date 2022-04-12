from rest_framework import viewsets, generics

from quotes.serializers import QuotesSerializer
from quotes.models import Quote


class AllQuotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all quotes to be viewed.
    """
    queryset = Quote.objects.all().order_by('-modified')
    serializer_class = QuotesSerializer


class QuotesDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuotesSerializer


class CreateQuoteViewSet(generics.CreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuotesSerializer

    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)
