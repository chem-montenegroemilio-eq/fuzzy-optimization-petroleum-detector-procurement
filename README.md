# Fuzzy Linear Programming and Fuzzy Systems for Gas Detector Procurement on Offshore Platforms

`fuzzy-optimization-petroleum-detector-procurement` contains the mathematical formulations, computational experiments, and results developed for a master's dissertation on fuzzy optimization applied to gas detector procurement on offshore platforms.

The repository includes implementations of linear and fuzzy optimization problems using different Python optimization tools, allowing the formulations and numerical results presented in the dissertation to be reproduced and compared.

---

## Quick start

### Running optimization problems

#### Linear Programming (LP)

Run the LP formulation using `otimizacao`:

```bash
python experiments/optimization/lp/lp-otimizacao.py
```

Run the LP formulation using SciPy:

```bash
python experiments/optimization/lp/lp-scipy.py
```

Run the LP formulation using PuLP:

```bash
python experiments/optimization/lp/lp-pulp.py
```

#### Fuzzy Linear Programming (FLP)

Run the FLP formulation using `otimizacao`:

```bash
python experiments/optimization/flp/flp-otimizacao.py
```

Run the FLP formulation using SciPy:

```bash
python experiments/optimization/flp/flp-scipy.py
```

Run the FLP formulation using PuLP:

```bash
python experiments/optimization/flp/flp-pulp.py
```

#### Integer Linear Programming (ILP)

Run the ILP formulation using SciPy:

```bash
python experiments/optimization/ilp/ilp-scipy.py
```

Run the ILP formulation using PuLP:

```bash
python experiments/optimization/ilp/ilp-pulp.py
```

#### Fuzzy Mixed-Integer Linear Programming (FMILP)

Run the FMILP formulation using SciPy:

```bash
python experiments/optimization/fmilp/fmilp-scipy.py
```

Run the FMILP formulation using PuLP:

```bash
python experiments/optimization/fmilp/fmilp-pulp.py
```

#### Relaxed Mixed-Integer Linear Programming (RMILP)

Run the RMILP formulation using PuLP:

```bash
python experiments/optimization/rmilp/rmilp-pulp.py
```

## Requirements

This repository was developed using Python 3.14.4.

The main Python packages used are:

- SciPy
- PuLP
- otimizacao

Install the required dependencies with:

```bash
python -m pip install -r requirements.txt
```

## Repository structure

```
.
├── README.md
├── CITATION.cff
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── data/
│
├── experiments/
│   └── optimization/
│       ├── lp/
│       ├── flp/
│       ├── ilp/
│       ├── fmilp/
│       └── rmilp/
│
└── thesis_results/
    ├── tables/
    └── figures/
```

## Citation

If you use this work, please cite the corresponding repository release.
Citation metadata are available in [CITATION.cff](CITATION.cff).

- Version: `v0.1.0`
- DOI: Not yet assigned.

On GitHub, the citation information can also be accessed through
Cite this repository.

Repository version:

v0.1.0

[DOI will be added when available.]