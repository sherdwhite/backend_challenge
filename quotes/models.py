from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db.models import CharField, PositiveIntegerField, DecimalField, DateField, BooleanField
from model_utils.models import TimeStampedModel


class Quote(TimeStampedModel):
    quote_number = CharField(db_index=True, max_length=10)
    effective_date = DateField()
    has_previous_cancelled_policy = BooleanField("Previous Cancelled Policy", default=False)
    is_property_owner = BooleanField("Property Owner", default=False)
    name = CharField(max_length=150)
    property_address = CharField(max_length=150)
    property_state = CharField(max_length=50)
    zip_code = CharField(max_length=5)
    base_premium = DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    total_term_premium = DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    monthly_term_premium = DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    total_additional_fees = DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    total_monthly_fees = DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    total_discounts = DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    total_monthly_discounts = DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
