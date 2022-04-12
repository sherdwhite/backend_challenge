import datetime
import random
import string

from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from backend_challenge.rates import SIX_MONTH_BASE
from quotes.models import Quote
from quotes.serializers import GetQuotesSerializer, PostQuotesSerializer


class AllQuotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all quotes to be viewed.
    """
    queryset = Quote.objects.all().order_by('-modified')
    serializer_class = GetQuotesSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class QuotesDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = GetQuotesSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CreateQuoteViewSet(generics.CreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = PostQuotesSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print('serializer before: {}'.format(serializer))
        serializer.save(quote_number=self.generate_quote_number(self),
                        effective_date=datetime.datetime.utcnow(),
                        base_premium=self.generate_base_premium(self))
        print('serializer after: {}'.format(serializer))

    @staticmethod
    def generate_quote_number(self):
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))

    @staticmethod
    def generate_base_premium(self):
        base_premium = 6 * SIX_MONTH_BASE
