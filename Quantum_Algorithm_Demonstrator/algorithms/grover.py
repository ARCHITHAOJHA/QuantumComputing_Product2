import streamlit as st
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import math

def run_grover():
    st.header("Grover's Search Algorithm")
    st.write("Searches an unstructured space using amplitude amplification.")

    n = st.slider("Number of search qubits", 2, 5, 3)
    target = st.number_input("Target state (decimal)", 0, 2**n - 1, 5)

    qc = QuantumCircuit(n, n)
    qc.h(range(n))

    iterations = max(1, round((math.pi / 4) * math.sqrt(2**n)))

    # Mark target state using phase oracle.
    bits = format(target, f"0{n}b")
    for i, bit in enumerate(reversed(bits)):
        if bit == "0":
            qc.x(i)

    if n == 1:
        qc.z(0)
    elif n == 2:
        qc.h(n-1)
        qc.cx(0, n-1)
        qc.h(n-1)
    else:
        qc.h(n-1)
        qc.mcx(list(range(n-1)), n-1)
        qc.h(n-1)

    for i, bit in enumerate(reversed(bits)):
        if bit == "0":
            qc.x(i)

    # Diffusion operator.
    qc.h(range(n))
    qc.x(range(n))
    if n == 1:
        qc.z(0)
    elif n == 2:
        qc.h(n-1); qc.cx(0, n-1); qc.h(n-1)
    else:
        qc.h(n-1); qc.mcx(list(range(n-1)), n-1); qc.h(n-1)
    qc.x(range(n))
    qc.h(range(n))

    qc.measure(range(n), range(n))

    st.subheader("Quantum Circuit")
    st.code(qc.draw(output="text"), language="text")
    st.write(f"Approximate Grover iterations for N={2**n}: **{iterations}** (one iteration is demonstrated in this compact circuit).")

    sim = AerSimulator()
    result = sim.run(transpile(qc, sim), shots=1024).result()
    counts = result.get_counts()

    st.subheader("Simulation Results")
    st.bar_chart(counts)

    found = max(counts, key=counts.get)
    st.success(f"Most frequent measured state: {found} (target = {format(target, f'0{n}b')})")

    st.subheader("Complexity Comparison")
    c1, c2 = st.columns(2)
    c1.metric("Classical search", "O(N)")
    c2.metric("Grover search", "O(√N)")
