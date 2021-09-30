from django.db.models import fields
from rest_framework import serializers
from .models import CreditAmount, CustomerRequirement, InitialAmount, Period, Proposal, Rate, RateField, TermField


class FixNameSerializer(serializers.ModelSerializer):
    def get_fields(self):
        result = super().get_fields()
        result.pop('_from')
        return result


class FixNameIntSerializer(FixNameSerializer):
    pass


class FixNameFloatSerializer(FixNameSerializer):
    pass


FixNameIntSerializer._declared_fields["from"] = serializers.IntegerField(
    source="_from")
FixNameFloatSerializer._declared_fields["from"] = serializers.DecimalField(
    source="_from", max_digits=5, decimal_places=2)


class CreditAmountSerializer(FixNameIntSerializer):
    class Meta:
        model = CreditAmount
        exclude = ('id', )


class InitialAmountSerializer(FixNameIntSerializer):
    class Meta:
        model = InitialAmount
        exclude = ('id', )


class RateFieldSerializer(FixNameFloatSerializer):
    class Meta:
        model = RateField
        exclude = ('id', )


class TermFieldSerializer(FixNameIntSerializer):
    class Meta:
        model = TermField
        exclude = ('id', )


class PeriodSerializer(serializers.ModelSerializer):
    rate = RateFieldSerializer()
    term = TermFieldSerializer()

    class Meta:
        model = Period
        exclude = ('rate_upper', )
        depth = 1


class RateSerializer(serializers.ModelSerializer):
    periods = PeriodSerializer(many=True)
    creditAmount = CreditAmountSerializer()
    initialAmount = InitialAmountSerializer()

    class Meta:
        model = Rate
        exclude = ('id', )


class CustomerRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequirement
        exclude = ('id',)


class ProposalSerializer(serializers.ModelSerializer):
    rate = RateSerializer()
    customerRequirements = CustomerRequirementSerializer()

    class Meta:
        model = Proposal
        fields = ('id', 'name', 'alias', 'organization',
                  'customerRequirements', 'rate')
        depth = 1
