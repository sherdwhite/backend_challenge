from rest_framework import serializers

from quotes.models import Quote


class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
