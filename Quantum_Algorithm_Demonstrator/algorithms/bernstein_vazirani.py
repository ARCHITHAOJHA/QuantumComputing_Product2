import streamlit as st
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def run_bernstein_vazirani():
    st.header("Bernstein-Vazirani Algorithm")
    st.write("Finds a hidden binary string using a single oracle query.")

    n = st.slider("Length of hidden string", 2, 10, 4)
    secret = st.text_input("Secret string", "1011", max_chars=n)

    if len(secret) != n or any(c not in "01" for c in secret):
        st.warning(f"Enter exactly {n} binary digits.")
        return

    qc = QuantumCircuit(n + 1, n)
    qc.x(n)
    qc.h(range(n + 1))

    for i, bit in enumerate(reversed(secret)):
        if bit == "1":
            qc.cx(i, n)

    qc.h(range(n))
    qc.measure(range(n), range(n))

    st.subheader("Quantum Circuit")
    st.code(qc.draw(output="text"), language="text")

    sim = AerSimulator()
    result = sim.run(transpile(qc, sim), shots=1024).result()
    counts = result.get_counts()

    st.subheader("Simulation Results")
    st.bar_chart(counts)

    found = max(counts, key=counts.get)
    st.success(f"Recovered secret string: {found}")
    st.write(f"Expected secret string: **{secret}**")

    st.subheader("Complexity Comparison")
    c1, c2 = st.columns(2)
    c1.metric("Classical oracle queries", f"O({n})")
    c2.metric("Quantum oracle queries", "1")
