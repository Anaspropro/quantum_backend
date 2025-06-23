from django.urls import path
from .views import QuantumSimulateView

urlpatterns = [
    path('simulate/', QuantumSimulateView.as_view(), name='quantum-simulate'),
]