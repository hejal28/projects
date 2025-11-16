# ==============================================================================
# FILE: assignment3.py
# ==============================================================================
# Assignment 3
# This file provides functions to create quantum circuits that generate entanglement.
# Learners are expected to implement the logic for the `ghz_circuit` function within
# the specified section of the function.
#
# Instructions:
# - Complete the `ghz_circuit` function as described in its docstring.

# - You are only allowed to to use the Hadamard gate and the 2 qubit CNOT gate.
#
# Testing:
# - To verify your implementation, run the provided test file:
#   test_assignment3.py, using the command:
#   python -m unittest test_assignment3.py
# ------------------------------------------------------------------------------
from qiskit import QuantumCircuit


def bell_pair_circuit() -> QuantumCircuit:
    """
    This functions creates and returns a quantum circuit that generates entanglement
    between 2 parties. It does not measure the circuit, so do not call the `measure`
    or `measure_all` functions here.

    :returns:   The quantum circuit that creates entanglement between 3 qubits.
    :rtype:     QuantumCircuit
    """
  
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    return qc


def ghz_circuit() -> QuantumCircuit:
    """
    This functions creates and returns a quantum circuit that generates entanglement
    between 3 parties. It does not measure the circuit, so do not call the `measure`
    or `measure_all` functions here. As an example take a look at the function
    `bell_pair_circuit()` above.
    The final state of the circuit should be 1/√2(|000> + |111>).

    :returns:   The quantum circuit that creates entanglement between 3 qubits.
    :rtype:     QuantumCircuit
    """
    qc = QuantumCircuit(3)
  
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
   
    return qc
