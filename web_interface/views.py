import requests
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProposalForm
from .models import Proposal
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, UpdateAPIView
from .serializers import ProposalSerializer
from rest_framework.parsers import FormParser

# Função para enviar uma solicitação de empréstimo à API de Análise de Crédito
def send_loan_request(document, name):
    api_url = "https://loan-processor.digitalsys.com.br/api/loan-request/"
    payload = {
        "document": document,
        "name": name,
    }
    response = requests.post(api_url, data=payload)
    if response.status_code == status.HTTP_200_OK:
        response_data = response.json()
        approved = response_data.get("approved", False)
        return approved
    else:
        return False

# Visualização para criar uma nova proposta
class CreateProposalView(APIView):
    parser_classes = [FormParser]

    def post(self, request):
            document = request.data.get("document")
            name = request.data.get("name")
            approved = send_loan_request(document, name)
            proposal = Proposal.objects.create(
                document=document,
                name=name,
                approved=approved,
            )
            serializer = ProposalSerializer(proposal)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# Visualização para listar todas as propostas
class ProposalListView(ListAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

# Visualização para aprovar uma proposta
class ApproveProposalView(UpdateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def perform_update(self, serializer):
        serializer.save(approved=True)

# Visualização para negar uma proposta
class DenyProposalView(UpdateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def perform_update(self, serializer):
        serializer.save(approved=False)

# Visualização para criar uma nova proposta usando formulário
def create_proposal(request):
    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-proposals')
    else:
        form = ProposalForm()
    return render(request, 'create_proposal.html', {'form': form})

# Visualização para a página de criação de proposta
def create_proposal_page(request):
    form = ProposalForm()
    return render(request, 'create_proposal.html', {'form': form})
