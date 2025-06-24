from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

def build_quantum_circuit(num_qubits, circuit_ops):
    qc = QuantumCircuit(num_qubits)
    for op in circuit_ops:
        gate = op.get('gate')
        targets = op.get('targets', [])
        if gate == 'H':
            qc.h(targets[0])
        elif gate == 'X':
            qc.x(targets[0])
        elif gate == 'Y':
            qc.y(targets[0])
        elif gate == 'Z':
            qc.z(targets[0])
        elif gate == 'CX' or (gate == 'CNOT' and len(targets) == 2):
            qc.cx(targets[0], targets[1])
    return qc

def run_quantum_circuit(num_qubits, circuit_ops, return_statevector=False):
    qc = QuantumCircuit(num_qubits, num_qubits)
    for op in circuit_ops:
        gate = op['gate']
        targets = op['targets']
        if gate in ['H', 'X', 'Y', 'Z']:
            # Single-qubit gates: require exactly one target
            if not isinstance(targets, list) or len(targets) != 1:
                raise ValueError(f"Gate {gate} requires exactly one target qubit.")
            t = targets[0]
            if gate == 'H':
                qc.h(t)
            elif gate == 'X':
                qc.x(t)
            elif gate == 'Y':
                qc.y(t)
            elif gate == 'Z':
                qc.z(t)
        elif gate in ['CX', 'CNOT']:
            # Two-qubit gates: require exactly two targets
            if not isinstance(targets, list) or len(targets) != 2:
                raise ValueError(f"Gate {gate} requires exactly two target qubits.")
            qc.cx(targets[0], targets[1])
        else:
            raise ValueError(f"Unsupported gate: {gate}")
    qc.measure(range(num_qubits), range(num_qubits))
    backend = AerSimulator()
    tqc = transpile(qc, backend)
    job = backend.run(tqc, shots=1)
    result = job.result()
    counts = result.get_counts(qc)
    statevector = None
    if return_statevector:
        qc_sv = qc.remove_final_measurements(inplace=False)
        statevector = Statevector.from_instruction(qc_sv)
    return {'counts': counts, 'statevector': statevector} if return_statevector else counts