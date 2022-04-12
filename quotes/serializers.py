from rest_framework import serializers

from quotes.models import Quote


class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['quote_number', 'effective_date', 'has_previous_cancelled_policy',  'is_property_owner',
                  'property_address', 'property_state', 'zip_code', 'base_premium', 'total_term_premium',
                  'monthly_term_premium', 'total_additional_fees', 'total_monthly_fees', 'total_discounts',
                  'total_monthly_discounts']
