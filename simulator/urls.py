from django.urls import path
from .views import QuantumSimulateView, UserRegisterView

urlpatterns = [
    path('simulate/', QuantumSimulateView.as_view(), name='quantum-simulate'),
    path('signup/', UserRegisterView.as_view(), name='signup'),
]