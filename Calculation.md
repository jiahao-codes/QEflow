
# QE_Flow: Preprocessing and Postprocessing Tools for Quantum Espresso

This repository provides high-throughput auxiliary preprocessing and postprocessing functions for Quantum Espresso simulations, designed for efficient and automated workflows.

---

## Table of Contents

1. [Installation](#installation)
2. [Features](#features)
   - [1. VC Relax Calculations](#1-vc-relax-calculations)
   - [2. projwfcx Analysis](#2-projwfcx-analysis)
   - [3. Band Structure Calculations](#3-band-structure-calculations)
4. [Usage Examples](#usage-examples)

---

## Installation <a name="installation"></a>

To use the `QE_Flow` package, you first need to install it. You can do so by cloning the repository and running the setup script (if provided). For example:

```bash
git clone https://github.com/your-repo/qe_flow.git
cd qe_flow
python setup.py install
```

Ensure that all dependencies, such as Python libraries and Quantum Espresso, are properly installed.

---

## Features <a name="features"></a>

### 1. VC Relax Calculations <a name="1-vc-relax-calculations"></a>

This function automates the generation of Quantum Espresso input files for variable-cell relaxation (`vc-relax`) calculations.

#### Arguments
- `structure_folder` (str): Path to the folder containing structural files (e.g., `.cif`).
- `QEfile_folder` (str): Path to the folder where the generated input files will be saved.
- `pseudo_folder` (str): Path to the folder containing pseudopotential files, named according to element symbols (e.g., `Mn.upf`).

##### QE Control Parameters
- `restart_mode` (str): Restart mode (e.g., `"from_scratch"`).
- `tstress` (bool): Enable stress tensor calculation.
- `tprnfor` (bool): Enable force calculation.
- `nstep` (int): Maximum number of steps.
- `etot_conv_thr` (float): Convergence threshold for total energy.
- `forc_conv_thr` (float): Convergence threshold for forces.

##### QE System Parameters
- `ecutwfc` (int): Plane-wave cutoff energy.
- `ecutrho` (int): Charge density cutoff energy.
- `occupations` (str): Type of occupation (e.g., `"smearing"`).
- `smearing` (str): Type of smearing (e.g., `"gauss"`).
- `degauss` (float): Smearing width.
- `nspin` (int): Number of spin components.
- `initial_magnetization` (dict): Initial magnetization for each element.
- `nosym` (bool): Disable symmetry operations.

##### QE Electrons Parameters
- `electron_maxstep` (int): Maximum number of electronic iterations.
- `conv_thr` (float): Convergence threshold for electronic self-consistency.
- `mixing_beta` (float): Mixing parameter for electronic density.
- `diagonalization` (str): Type of diagonalization algorithm.

##### QE Ions Parameters
- `ion_dynamics` (str): Dynamics for ionic minimization.

##### QE Cell Parameters
- `cell_dynamics` (str): Dynamics for cell optimization.
- `cell_dofree` (str): Degrees of freedom for cell optimization.
- `kpoints` (tuple): K-point mesh for Brillouin zone sampling.

---

### 2. projwfcx Analysis <a name="2-projwfcx-analysis"></a>

This function performs post-processing analysis of projected wavefunctions (`projwfc.x`) results.

#### Arguments
- `QEfile_folder` (str): Path to the folder containing Quantum Espresso calculation files.
- `ngauss` (int): Gaussian smearing type.
- `degauss` (float): Gaussian smearing width.
- `Emin` (float): Minimum energy for projected states.
- `Emax` (float): Maximum energy for projected states.
- `DeltaE` (float): Energy step size.
- `result_prefix` (str): Prefix for the output file name.

---

### 3. Band Structure Calculations <a name="3-band-structure-calculations"></a>

#### Band Structure Input Generation
This function automates the generation of Quantum Espresso input files for band structure calculations.

#### Arguments
- `structure_folder` (str): Path to the folder containing structural files (e.g., `.cif`).
- `QEfile_folder` (str): Path to the folder where the generated input files will be saved.
- `pseudo_folder` (str): Path to the folder containing pseudopotential files.

##### Additional Parameters
- `restart_mode`, `ecutwfc`, `ecutrho`, `occupations`, `smearing`, `degauss`, `nspin`, `initial_magnetization`, `nosym`, `diagonalization` (as described above).
- `kpoints_path` (list): Custom K-point path. If not provided, the function will use pymatgen's K-point path generation.
- `line_density` (int): Number of K-points inserted along each path segment.

---

## Usage Examples <a name="usage-examples"></a>

### Example 1: VC Relax Calculations
```python
from QEflow import Calculation

structure_folder = "data3/surfaces_added"
QEfile_folder = "data3/surfaces_added_calculation"
pseudo_folder = "data3/SSSP_1.3.0_PBE_efficiency"

# Control parameters
restart_mode = "from_scratch"
tstress = True
tprnfor = True
nstep = 50
etot_conv_thr = 1.0E-4
forc_conv_thr = 1.0E-3

# System parameters
ecutwfc = 50
ecutrho = 400
occupations = "smearing"
smearing = "gauss"
degauss = 0.05
nspin = 2
initial_magnetization = {'Cr':5, 'Mn':5, 'Fe':4, 'Ni':2, 'Cu':1}
nosym = True

# Electrons parameters
electron_maxstep = 100
conv_thr = 1e-6
mixing_beta = 0.5
diagonalization = "david"

# Ions and Cell parameters
ion_dynamics = "bfgs"
cell_dynamics = "bfgs"
cell_dofree = "all"
kpoints = (3, 3, 3)

Calculation.pwx_vc_relax(structure_folder, QEfile_folder, pseudo_folder, 
                         restart_mode, tstress, tprnfor, nstep, etot_conv_thr, forc_conv_thr,
                         ecutwfc, ecutrho, occupations, smearing, degauss, 
                         nspin, initial_magnetization, nosym, electron_maxstep, conv_thr, mixing_beta, diagonalization, 
                         ion_dynamics, cell_dynamics, cell_dofree, kpoints)
```

### Example 2: projwfcx Analysis
```python
from QEflow import Calculation

QEfile_folder = "data3/calculation2"
ngauss = 0
degauss = 0.01
Emin = -10
Emax = 20
DeltaE = 0.01
result_prefix = 'QE_Flow'

Calculation.projwfcx(QEfile_folder, ngauss, degauss, Emin, Emax, DeltaE, result_prefix)
```

### Example 3: Band Structure Calculations
```python
from QEflow import Calculation

structure_folder = "data3/structures_vc_relaxed"
QEfile_folder = "data3/calculation2"
pseudo_folder = "data3/SSSP_1.3.0_PBE_efficiency"

restart_mode = "from_scratch"
ecutwfc = 50
ecutrho = 400
occupations = "smearing"
smearing = "gauss"
degauss = 0.05
nspin = 2
initial_magnetization = {'Cr':5, 'Mn':5, 'Fe':4, 'Ni':2, 'Cu':1}
nosym = True
diagonalization = "david"
kpoints_path = None
line_density = 5

Calculation.pwx_bands(structure_folder, QEfile_folder, pseudo_folder, restart_mode,
                      ecutwfc, ecutrho, occupations, smearing, degauss, 
                      nspin, initial_magnetization, nosym, diagonalization, kpoints_path, line_density)
```

---

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests to improve this repository.

---

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.

---
