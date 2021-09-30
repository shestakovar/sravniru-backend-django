from django.db import models


class ProposalManager(models.QuerySet):
    def sort_rate(self):
        return self.annotate(minrate=models.Min('rate__periods__rate___from')).order_by('minrate')

    def sort_sum(self):
        return self.order_by('-rate__creditAmount__to', '-rate__creditAmount___from')
