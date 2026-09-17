import streamlit as st
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from collections import Counter

def run_deutsch_jozsa():
    st.header("Deutsch-Jozsa Algorithm")
    st.write("Determines whether a Boolean oracle is constant or balanced with one quantum query.")

    n = st.slider("Number of input qubits", 2, 8, 3)
    oracle_type = st.selectbox("Oracle type", ["Constant", "Balanced"])

    qc = QuantumCircuit(n + 1, n)
    qc.x(n)
    qc.h(range(n + 1))

    if oracle_type == "Constant":
        # Constant-0 oracle: do nothing.
        pass
    else:
        # Balanced oracle: f(x) = x[0] XOR ... XOR x[n-1]
        for q in range(n):
            qc.cx(q, n)

    qc.h(range(n))
    qc.measure(range(n), range(n))

    st.subheader("Quantum Circuit")
    st.code(qc.draw(output="text"), language="text")

    sim = AerSimulator()
    result = sim.run(transpile(qc, sim), shots=1024).result()
    counts = result.get_counts()

    st.subheader("Simulation Results")
    st.bar_chart(counts)

    observed = list(counts.keys())
    detected = "Constant" if observed == ["0" * n] else "Balanced"

    st.success(f"Detected oracle: {detected}")
    st.write(f"Expected oracle: **{oracle_type}**")

    st.subheader("Complexity Comparison")
    col1, col2 = st.columns(2)
    col1.metric("Classical deterministic queries", f"2^{n-1} + 1")
    col2.metric("Quantum queries", "1")
    st.caption("The algorithm demonstrates a query-complexity advantage, not necessarily an end-to-end runtime speedup.")
