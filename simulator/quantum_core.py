from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

def build_quantum_circuit(num_qubits, circuit_ops):
    qc = QuantumCircuit(num_qubits)
    for op in circuit_ops:
        gate = op.get('gate')
        targets = op.get('targets', [])
        params = op.get('params', [])
        if gate == 'H':
            qc.h(targets[0])
        elif gate == 'X':
            qc.x(targets[0])
        elif gate == 'Y':
            qc.y(targets[0])
        elif gate == 'Z':
            qc.z(targets[0])
        elif gate == 'S':
            qc.s(targets[0])
        elif gate == 'T':
            qc.t(targets[0])
        elif gate == 'CX' or (gate == 'CNOT' and len(targets) == 2):
            qc.cx(targets[0], targets[1])
        elif gate == 'CCX' and len(targets) == 3:
            qc.ccx(targets[0], targets[1], targets[2])
        elif gate == 'RX' and params:
            qc.rx(params[0], targets[0])
        elif gate == 'RY' and params:
            qc.ry(params[0], targets[0])
        elif gate == 'RZ' and params:
            qc.rz(params[0], targets[0])
        elif gate == 'SWAP' and len(targets) == 2:
            qc.swap(targets[0], targets[1])
        # Add more gates as needed
    return qc

def run_quantum_circuit(num_qubits, circuit_ops, return_statevector=False):
    qc = QuantumCircuit(num_qubits, num_qubits)
    for op in circuit_ops:
        gate = op['gate']
        targets = op['targets']
        params = op.get('params', [])
        if gate == 'H':
            for t in targets:
                qc.h(t)
        elif gate == 'X':
            for t in targets:
                qc.x(t)
        elif gate == 'Y':
            for t in targets:
                qc.y(t)
        elif gate == 'Z':
            for t in targets:
                qc.z(t)
        elif gate == 'S':
            for t in targets:
                qc.s(t)
        elif gate == 'T':
            for t in targets:
                qc.t(t)
        elif gate == 'CX' or (gate == 'CNOT' and len(targets) == 2):
            qc.cx(targets[0], targets[1])
        elif gate == 'CCX' and len(targets) == 3:
            qc.ccx(targets[0], targets[1], targets[2])
        elif gate == 'RX' and params:
            for t in targets:
                qc.rx(params[0], t)
        elif gate == 'RY' and params:
            for t in targets:
                qc.ry(params[0], t)
        elif gate == 'RZ' and params:
            for t in targets:
                qc.rz(params[0], t)
        elif gate == 'SWAP' and len(targets) == 2:
            qc.swap(targets[0], targets[1])
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