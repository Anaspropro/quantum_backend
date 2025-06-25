from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from .serializers import QuantumSimulateSerializer
from .quantum_core import run_quantum_circuit, build_quantum_circuit
from django.contrib.auth.models import User
from rest_framework import generics

class QuantumSimulateView(APIView):
    def post(self, request):
        serializer = QuantumSimulateSerializer(data=request.data)
        if serializer.is_valid():
            num_qubits = serializer.validated_data['numQubits']
            circuit = serializer.validated_data['circuit']
            try:
                result = run_quantum_circuit(num_qubits, circuit)
                return Response({'result': result})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
