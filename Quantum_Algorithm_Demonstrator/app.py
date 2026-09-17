import streamlit as st
from algorithms.deutsch_jozsa import run_deutsch_jozsa
from algorithms.bernstein_vazirani import run_bernstein_vazirani
from algorithms.simon import run_simon
from algorithms.grover import run_grover
from algorithms.qft import run_qft

st.set_page_config(page_title="Quantum Algorithm Demonstrator", page_icon="⚛️", layout="wide")

st.title("⚛️ Quantum Algorithm Demonstrator")
st.caption("Interactive Qiskit toolkit for demonstrating fundamental quantum algorithms.")

ALGORITHMS = {
    "Deutsch-Jozsa": run_deutsch_jozsa,
    "Bernstein-Vazirani": run_bernstein_vazirani,
    "Simon's Algorithm": run_simon,
    "Grover's Search": run_grover,
    "Quantum Fourier Transform (QFT)": run_qft,
}

algorithm = st.sidebar.selectbox("Select Algorithm", list(ALGORITHMS.keys()))
st.sidebar.markdown("---")
st.sidebar.info(
    "Each module shows the circuit, simulation results, detected result, "
    "and a classical-vs-quantum complexity comparison."
)

try:
    ALGORITHMS[algorithm]()
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.info("Check that the packages in requirements.txt are installed correctly.")
