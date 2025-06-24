from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuantumSimulateSerializer
from .quantum_core import run_quantum_circuit, build_quantum_circuit

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
