from django.contrib import admin
from .models import CreditAmount, InitialAmount, Rate, RateField, TermField, Period, Organization, CustomerRequirement, Proposal

admin.site.register(CreditAmount)
admin.site.register(InitialAmount)
admin.site.register(Rate)
admin.site.register(RateField)
admin.site.register(TermField)
admin.site.register(Period)
admin.site.register(Organization)
admin.site.register(CustomerRequirement)
admin.site.register(Proposal)
