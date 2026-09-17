import streamlit as st
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import QFT

def run_qft():
    st.header("Quantum Fourier Transform (QFT)")
    st.write("Applies the quantum analogue of the discrete Fourier transform to a quantum state.")

    n = st.slider("Number of qubits", 2, 6, 3)
    input_state = st.number_input("Input computational basis state (decimal)", 0, 2**n - 1, 1)

    qc = QuantumCircuit(n, n)
    bits = format(input_state, f"0{n}b")
    for i, bit in enumerate(reversed(bits)):
        if bit == "1":
            qc.x(i)

    qc.append(QFT(n, do_swaps=True), range(n))
    qc.measure(range(n), range(n))

    st.subheader("Quantum Circuit")
    st.code(qc.draw(output="text"), language="text")

    sim = AerSimulator()
    result = sim.run(transpile(qc, sim), shots=1024).result()
    counts = result.get_counts()

    st.subheader("Measurement Results")
    st.bar_chart(counts)

    st.subheader("Complexity Comparison")
    c1, c2 = st.columns(2)
    c1.metric("Classical FFT", "O(n log n)")
    c2.metric("QFT gate count", "O(n²)")
    st.caption("QFT's main importance is as a quantum subroutine; comparing gate counts directly with classical FFT runtime is not an apples-to-apples comparison.")
