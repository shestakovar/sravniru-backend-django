from rest_framework import viewsets
from .models import Proposal
from .serializers import ProposalSerializer


class ProposalApiView(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def get_queryset(self):
        list_proposals = self.queryset
        query = self.request.query_params.get('sort')
        if (query is not None):
            if (query == 'rate'):
                list_proposals = list_proposals.sort_rate()
            if (query == 'sum'):
                list_proposals = list_proposals.sort_sum()
        return list_proposals
