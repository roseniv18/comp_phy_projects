# comp_phy_projects

## Overview

This is my personal collection of numerical simulations, algorithms, and implementations for solving various physics problems based on Mark Newman's Computational Physics book. The code is primarily written in Python, with some C extensions for sections that I wanted to perform faster.

## Repository Structure

The repository currently has only 1 chapter of the book (Chapter 5 - Integrals and Derivatives). I will add more in the future.
I have organized the CH05 folder like this:

-   **numerical-methods/**: Basic numerical algorithms

    -   Integration methods (Simpson, trapezoidal, adaptive methods)
    -   Differential equation solvers
    -   Utilities for numerical computation

-   **classical-physics/**: Simulations of classical physics phenomena

    -   Mechanics (oscillators, gravity simulations)
    -   Electromagnetism

-   **quantum-physics/**: Quantum mechanics simulations

    -   Quantum harmonic oscillator
    -   Wave function calculations

-   **optics/**: Optics and wave phenomena

    -   Diffraction simulations
    -   Bessel function applications

-   **thermodynamics/**: Thermal physics

    -   Heat capacity calculations
    -   Stefan-Boltzmann law

-   **special-functions/**: Implementations of special mathematical functions

    -   Gamma function
    -   Bessel functions

-   **C_files/**: C implementations for performance

    -   Simpson's rule in C

-   **data/**: Data analysis programs

-   **performance-analysis/**: Comparisons of different numerical approaches

-   **resources/**: Files containing input data for some programs

## Demo

![Diffraction Grating](diffraction_grating.png?raw=true "Diffraction Grating")
![Electric Field with Continuous Charge Distribution](electric_field.png?raw=true "Electric Field with Continuous Charge Distribution")
![Quantum Harmonic Oscillator](quantum_harmonic_oscillator.png?raw=true "Quantum Harmonic Oscillator")
![Quantum Harmonic Oscillator Wavefunctions](quantum_harmonic_oscillator_wf.png?raw=true "Quantum Harmonic Oscillator Wavefunctions")

## Installation

1. Clone the repository:

```bash

git clone https://github.com/roseniv18/comp_phy_projects.git
cd comp_phy_projects/CH05_INTEGRALS_AND_DERIVATIVES

```

2. Install requirements:

```py
pip install -r requirements.txt
```

3. For C extensions, compile using the provided Makefile:

```bash

   cd C_files
   make

```
