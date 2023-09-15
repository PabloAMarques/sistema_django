from django.urls import path
from .views import ProposalListView, CreateProposalView, create_proposal_page  # Importe a função create_proposal_page

urlpatterns = [
    path('create-proposal/', CreateProposalView.as_view(), name='create-proposal'),
    path('', create_proposal_page, name='create-proposal-page'),
]
