from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from quotes.models import Quote
from quotes.serializers import QuotesSerializer


class AllQuotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all quotes to be viewed.
    """
    queryset = Quote.objects.all().order_by('-modified')
    serializer_class = QuotesSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class QuotesDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuotesSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CreateQuoteViewSet(generics.CreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuotesSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)
