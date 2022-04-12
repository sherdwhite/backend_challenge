import datetime
import random
import string

from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from backend_challenge.rates import SIX_MONTH_BASE, VOLCANO_STATES, VOLCANO_STATE_FEE_RATE, PROPERTY_OWNER_DISCOUNT
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

    # TODO Finish calculating rates.
    def perform_create(self, serializer):
        print('serializer.validated_data before: {}'.format(serializer.validated_data))
        serializer.save(quote_number=self.generate_quote_number(self),
                        effective_date=datetime.datetime.utcnow(),
                        base_premium=self.generate_base_premium(self, serializer),
                        total_term_premium=self.generate_base_premium(self, serializer),
                        monthly_term_premium=int(self.generate_base_premium(self, serializer))/6,
                        total_additional_fees=0,
                        total_monthly_fees=0,
                        total_discounts=0,
                        total_monthly_discounts=0)
        print('serializer.validated_data after: {}'.format(serializer.validated_data))

    @staticmethod
    def generate_quote_number(self):
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))

    @staticmethod
    def generate_base_premium(self, serializer):
        base_premium = 6 * SIX_MONTH_BASE
        # TODO Properly handle state logic.
        if serializer.validated_data['property_state'] in VOLCANO_STATES:
            base_premium += base_premium * VOLCANO_STATE_FEE_RATE
        if serializer.validated_data['is_property_owner']:
            base_premium = base_premium - (base_premium * PROPERTY_OWNER_DISCOUNT)

        return base_premium

# TODO Create Checkout Endpoint
