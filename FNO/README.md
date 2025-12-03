# Fourier Neural Operators (FNO) Tutorial

This folder contains a comprehensive educational resource on Fourier Neural Operators - a revolutionary architecture for learning solution operators of partial differential equations.

## Contents

### Main Document
- **`FNO_breakdown.tex`** - Complete LaTeX source file for the tutorial
- **`FNO_breakdown.pdf`** - Compiled PDF document (generated via `pdflatex`)

### Supporting Files
- **`fno_architecture.png`** - Architecture diagram illustrating the FNO structure
- **`FNO_breakdown.aux`** - LaTeX auxiliary file (auto-generated)
- **`FNO_breakdown.log`** - LaTeX compilation log (auto-generated)
- **`FNO_breakdown.out`** - LaTeX hyperref output file (auto-generated)
- **`FNO_breakdown.toc`** - Table of contents file (auto-generated)

## What's Inside the Tutorial

This comprehensive tutorial covers:

### Part I: Theoretical Foundations
1. **Introduction to Operator Learning**
   - The classical problem of learning mappings between function spaces
   - PDE solution operators
   - The discretization challenge

2. **Fourier Neural Operators: Architecture**
   - High-level overview of FNO innovation
   - Architecture components: Lifting layer, Fourier layers, Projection layer
   - Detailed explanation of the Fourier layer mechanism

3. **Resolution Invariance**
   - Why traditional CNNs fail at different resolutions
   - Mathematical proof of FNO's resolution invariance
   - The key insight: learning in frequency domain

4. **Implementation Details and PyTorch Tricks**
   - SpectralConv1d layer deep dive
   - Complex parameters in PyTorch
   - Einstein summation for efficient computation
   - Real FFT (rfft) usage
   - Mode truncation implementation

5. **Example: Allen-Cahn Equation**
   - Data processing
   - Resolution invariance testing

6. **Extension to 2D: SpectralConv2d**
   - 2D Fourier transforms
   - Handling multiple weight matrices

### Part II: Hands-On Exercises

The tutorial includes 6 comprehensive exercise sets:

1. **Understanding Fourier Transforms**
   - Manual FFT computation
   - Mode truncation effects
   - Resolution invariance testing

2. **Implementing SpectralConv1d**
   - Complex parameter initialization
   - Einstein summation practice
   - Complete layer implementation

3. **Building the Full FNO**
   - Lifting and projection layers
   - Fourier layer module
   - Complete FNO1d assembly

4. **Training and Evaluation**
   - Data preparation
   - Training loop implementation
   - Resolution invariance experiments

5. **Advanced Topics**
   - SpectralConv2d implementation
   - Hyperparameter tuning
   - Applying to real PDEs

6. **Understanding Limitations**
   - When FNO fails
   - Comparison with other architectures

### Additional Content

- **Advanced Theoretical Topics**: Universal approximation, convergence analysis, connection to Green's functions
- **Implementation Best Practices**: Memory efficiency, numerical stability, debugging checklist
- **Appendices**: Mathematical background, PyTorch FFT functions, common errors and solutions

## Key Concepts Explained

The tutorial provides deep understanding of:

- **Why FNO is resolution-invariant**: By learning in the frequency domain and truncating to low Fourier modes, FNOs learn operators in continuous function space, independent of discretization
- **Global receptive fields**: Unlike local convolutions, FNO captures global dependencies efficiently
- **Convolution theorem**: How convolution in physical space becomes multiplication in Fourier space
- **PyTorch implementation tricks**: Complex tensors, einsum notation, rfft/irfft operations

## Use Cases

This tutorial is designed for:
- Students learning about neural operators and scientific machine learning
- Practitioners implementing FNO for PDE problems
- Researchers exploring operator learning architectures
- Anyone interested in the intersection of deep learning and scientific computing

## Compiling the Document

To generate the PDF from the LaTeX source:

```bash
pdflatex FNO_breakdown.tex
pdflatex FNO_breakdown.tex  # Run twice for proper cross-references
```

**Requirements:**
- LaTeX distribution (e.g., TeX Live, MiKTeX)
- Required packages: amsmath, tikz, tcolorbox, listings, algorithm, and others (see document preamble)

## Learning Path

Recommended approach:
1. Read through the theoretical sections to understand the mathematical foundations
2. Study the PyTorch implementation details and tricks
3. Work through the exercises sequentially (each builds on previous ones)
4. Implement your own FNO from scratch
5. Apply to your own PDE problem

## References

Based on the seminal paper:
- Li, Z., et al. (2020). "Fourier Neural Operator for Parametric Partial Differential Equations." arXiv:2010.08895

## Course Context

This tutorial is part of the **AI in the Sciences and Engineering** course materials (ETH, Fall 2025).

---

*For questions or issues with the tutorial content, please refer to the course resources or contact the course instructors.*
