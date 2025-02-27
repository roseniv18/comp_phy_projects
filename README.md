<<<<<<< HEAD

# comp_phy_projects

# This repo contains solved problems and projects from Mark Newman's Computational Physics book

# Computational Physics Repository

This is my personla collection of numerical simulations, algorithms, and implementations for solving various physics problems based on Mark Newman's Computational Physics book.

## Overview

This repository contains implementations of various numerical methods and simulations for physics problems, ranging from classical mechanics to quantum physics. The code is primarily written in Python, with some C extensions for performance-critical sections.

## Repository Structure

The repository currently has only 1 chapter of the book. In future, I will add more.
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

-   **c-extensions/**: C implementations for performance

    -   Simpson's rule in C

-   **data/**: Data analysis programs

-   **performance-analysis/**: Comparisons of different numerical approaches

-   **resources/**: Files containing input data for some programs

## Installation

1. Clone the repository:

```bash

git clone https://github.com/roseniv18/comp_phy_projects.git
cd comp_phy_projects

```

2. Install requirements:

```py
pip install -r requirements.txt
```

3. For C extensions, compile using the provided Makefile:

```bash

   cd c-extensions
   make

```

> > > > > > > bc2b4bb (first commit)
