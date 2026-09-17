# QuantumComputing_Product2

An interactive Qiskit + Streamlit toolkit for demonstrating:

Deutsch-Jozsa
Bernstein-Vazirani
Simon's Algorithm
Grover's Search
Quantum Fourier Transform (QFT)
Features
Select an algorithm from the sidebar.
Configure algorithm inputs.
Display the Qiskit circuit.
Run the circuit on a local Aer simulator.
Visualize measurement counts.
Show the detected/result state.
Compare quantum and classical query/gate complexity.
Installation
Use Python 3.10+.

python -m venv .venv
Windows:

.venv\Scripts\activate
Linux/macOS:

source .venv/bin/activate
Install packages:

pip install -r requirements.txt
Run:

streamlit run app.py
Then open the local Streamlit address shown in the terminal.

Project Structure
Quantum_Algorithm_Demonstrator/
├── app.py
├── algorithms/
│   ├── deutsch_jozsa.py
│   ├── bernstein_vazirani.py
│   ├── simon.py
│   ├── grover.py
│   └── qft.py
├── requirements.txt
└── README.md
Notes
This is an educational demonstrator. Complexity figures describe standard query/gate-complexity models and should not be interpreted as direct wall-clock speedups on a classical simulator.
