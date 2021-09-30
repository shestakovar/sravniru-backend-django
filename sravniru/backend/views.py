from rest_framework import viewsets
from .models import Proposal
from .serializers import ProposalSerializer


class ProposalApiView(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
