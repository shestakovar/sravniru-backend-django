from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import ProposalManager


class CreditAmount(models.Model):
    _from = models.IntegerField(db_column='from')
    to = models.IntegerField(blank=True, null=True)


class InitialAmount(models.Model):
    _from = models.IntegerField(db_column='from')
    to = models.IntegerField(blank=True, null=True)


class Rate(models.Model):
    class Currency(models.TextChoices):
        RUB = 'RUB', ('RUB')
    currency = models.CharField(choices=Currency.choices, max_length=16)
    creditAmount = models.OneToOneField(CreditAmount, on_delete=models.PROTECT)
    initialAmount = models.OneToOneField(
        InitialAmount, on_delete=models.PROTECT)




class RateField(models.Model):
    _from = models.DecimalField(
        db_column='from', max_digits=5, decimal_places=2)
    to = models.DecimalField(max_digits=5, decimal_places=2)


class TermField(models.Model):
    _from = models.IntegerField(db_column='from')
    to = models.IntegerField()


class Period(models.Model):
    class Terms(models.TextChoices):
        MONTH = 'month', _('month')

    rate = models.OneToOneField(RateField, on_delete=models.PROTECT)
    termUnit = models.CharField(choices=Terms.choices, max_length=5)
    term = models.OneToOneField(TermField, on_delete=models.PROTECT)
    isFloatingRate = models.BooleanField()
    rate_upper = models.ForeignKey(
        Rate, on_delete=models.PROTECT, related_name='periods')




class Organization(models.Model):
    name = models.CharField(max_length=255)
    license = models.CharField(max_length=255)
    logo = models.URLField(max_length=255)

    def __str__(self):
        return self.name


class CustomerRequirement(models.Model):
    documents = models.IntegerField()
    age = models.IntegerField()
    manAgeAtRepayment = models.IntegerField()
    femaleAgeAtRepayment = models.IntegerField()
    lastExperience = models.IntegerField()
    fullExperience = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return '%d %d %d %d %d %d %d' % (self.documents, self.age, self.manAgeAtRepayment, self.femaleAgeAtRepayment, self.lastExperience, self.fullExperience, self. salary)


class Proposal(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    customerRequirements = models.ForeignKey(
        CustomerRequirement, on_delete=models.PROTECT)
    rate = models.OneToOneField(Rate, on_delete=models.PROTECT)
    objects = ProposalManager.as_manager()
