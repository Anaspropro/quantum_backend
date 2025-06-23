from rest_framework import serializers

class QuantumSimulateSerializer(serializers.Serializer):
    numQubits = serializers.IntegerField(min_value=1, max_value=10)
    circuit = serializers.ListField()