# ME300: Thermodynamics II - Python Code Examples

This repository contains Python code examples and computational tools for **ME300: Thermodynamics II** at Purdue University. These examples are designed to help students understand and apply intermediate thermodynamics concepts through practical programming exercises.

## About the Course

ME300 builds upon fundamental thermodynamics principles to explore more advanced topics in thermal-fluid systems. The course emphasizes the application of thermodynamic principles to real-world engineering problems, including power generation, refrigeration, and chemical processes.

## Topics Covered

This repository includes Python examples for key thermodynamics topics:

- **ME 200 Review**: Basic calculations to refresh on first and second law and get familiar with CoolProp property calls
- **Transient Analysis**: Transient analysis of control volumes: charging and discharging a tank
- **Exergy Analysis**: Calculations on exergy (availability) of various systems and components
- **Gas Mixtures**: Ideal and real gas mixture behavior, partial pressures, and psychrometrics
- **Psychrometrics**: Psychrometric calculations and applications to real HVAC systems
- **Cycles**: Various advanced power cycles and vapor compression cycles are presented
- **Real Gases**: Using Equations of State to solve for properties of fluids
- **Combustion**: Understand and calculate reacting mixtures of hydrocarbon fuels
- **Chemical Equilibrium**: Apply the equilibrium constant relationship, to relate pressure, temperature, and equilibrium constant for ideal gas mixtures involving individual and multiple reactions.

## Getting Started

### Prerequisites

- ME 200
- Python 3.8 or higher
- Basic knowledge of thermodynamics fundamentals
- Familiarity with Python programming

### Recommended Libraries

```bash
pip install numpy scipy matplotlib CoolProp pandas
```

- **CoolProp**: High-accuracy thermodynamic property library
- **NumPy**: Numerical computing
- **SciPy**: Scientific computing and optimization
- **Matplotlib**: Plotting and visualization
- **Pandas**: Data manipulation and analysis

## Usage

Each example is self-contained and includes:

- Clear problem statements
- Step-by-step solution methodology
- Commented code for educational purposes
- Visualizations where applicable

Run any example script directly:

```bash
python examples/rankine_cycle.py
```

Or explore interactive Jupyter notebooks:

```bash
jupyter notebook notebooks/
```

## Disclaimer

These examples are educational resources intended to supplement coursework. 

## License

This repository is provided for educational purposes. Please respect Purdue University's academic integrity policies when using these materials.

## Resources

1. **CoolProp Documentation:** http://www.coolprop.org/
2. **Course Materials:** 
    1. **Textbook:** "Fundamentals of Engineering Thermodynamics", M.J. Moran, H.N. Shapiro, D.N. Boettner, M.B. Bailey, Ver 7 or higher
    2. Syllabus to be provided

---

# **Boiler Up!** 🚂