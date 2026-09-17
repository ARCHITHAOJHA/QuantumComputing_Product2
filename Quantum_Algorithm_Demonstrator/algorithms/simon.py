import streamlit as st
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def build_simon_oracle(n, secret):
    qc = QuantumCircuit(2*n)
    # Simple periodic oracle construction for demonstration.
    # For each i>0, if secret bit is 1, connect output i to output 0.
    # Then copy input bits to output bits.
    for i in range(n):
        qc.cx(i, n+i)
    for i, bit in enumerate(secret):
        if bit == "1" and i != 0:
            qc.cx(0, n+i)
    return qc

def run_simon():
    st.header("Simon's Algorithm")
    st.write("Demonstrates how a hidden XOR period can be identified with exponentially fewer oracle queries in the idealized query model.")

    n = st.slider("Number of input qubits", 2, 5, 3)
    secret = st.text_input("Hidden string", "110", max_chars=n)

    if len(secret) != n or any(c not in "01" for c in secret) or secret == "0"*n:
        st.warning(f"Enter a non-zero binary string of length {n}.")
        return

    qc = QuantumCircuit(2*n, n)
    qc.h(range(n))
    qc.compose(build_simon_oracle(n, secret), inplace=True)
    qc.h(range(n))
    qc.measure(range(n), range(n))

    st.subheader("Quantum Circuit")
    st.code(qc.draw(output="text"), language="text")

    sim = AerSimulator()
    result = sim.run(transpile(qc, sim), shots=1024).result()
    counts = result.get_counts()

    st.subheader("Simulation Results")
    st.bar_chart(counts)

    st.info("Simon measurement strings satisfy y · s = 0 (mod 2). Multiple independent samples are normally collected and solved as linear equations over GF(2).")
    st.write(f"Demonstration hidden string: **{secret}**")

    st.subheader("Complexity Comparison")
    c1, c2 = st.columns(2)
    c1.metric("Classical queries", "O(2^n)")
    c2.metric("Quantum queries", "O(n)")
