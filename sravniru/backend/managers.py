from django.db import models


class ProposalManager(models.QuerySet):
    def sort_rate(self):
        return self.annotate(minrate=models.Min('rate__periods__rate___from')).order_by('minrate')

    def sort_sum(self):
        return self.order_by('-rate__creditAmount__to', '-rate__creditAmount___from')

    def filter_price(self, price):
        return self.filter(rate__creditAmount___from__lte=price).exclude(rate__creditAmount__to__lt=price)

    def filter_initial_amount(self, price, initialAmount):
        percentage = int(initialAmount) / int(price) * 100
        return self.filter(rate__initialAmount___from__lte=percentage).exclude(rate__initialAmount__to__lt=percentage)

    def filter_term(self, term):
        return self.annotate(minterm=models.Min('rate__periods__term___from')) \
            .annotate(maxterm=models.Max('rate__periods__term__to')) \
                .filter(minterm__lte=term).filter(maxterm__gte=term)
