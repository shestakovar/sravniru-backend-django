from rest_framework import viewsets
from .models import Proposal
from .serializers import ProposalSerializer


class ProposalApiView(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def get_queryset(self):
        list_proposals = self.queryset

        creditAmount = self.request.query_params.get('creditAmount')
        if (creditAmount is not None and creditAmount.isdigit()):
            list_proposals = list_proposals.filter_price(creditAmount)
        
        initialAmount = self.request.query_params.get('initialAmount')
        if (creditAmount is not None and initialAmount is not None and creditAmount.isdigit() and initialAmount.isdigit()):
            list_proposals = list_proposals.filter_initial_amount(creditAmount, initialAmount)
        
        term = self.request.query_params.get('term')
        if (term is not None and term.isdigit()):
            list_proposals = list_proposals.filter_term(term)



        sort = self.request.query_params.get('sort')
        if (sort is not None):
            if (sort == 'rate'):
                list_proposals = list_proposals.sort_rate()
            if (sort == 'sum'):
                list_proposals = list_proposals.sort_sum()
        return list_proposals
