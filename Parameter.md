
# QE_Flow: Parameter Testing for Quantum Espresso

This repository provides high-throughput auxiliary preprocessing and postprocessing functions for Quantum Espresso parameter testing, designed to efficiently determine optimal cutoff energies, k-point meshes, and other computational parameters.

---

## Table of Contents

1. [Installation](#installation)
2. [Features](#features)
   - [1. Cutoff Energy Test](#1-cutoff-energy-test)
   - [2. K-point Mesh Test](#2-k-point-mesh-test)
   - [3. Postprocessing Results](#3-postprocessing-results)
3. [Usage Examples](#usage-examples)

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

### 1. Cutoff Energy Test <a name="1-cutoff-energy-test"></a>

This function automates the generation of Quantum Espresso input files for testing different plane-wave cutoff energies (`ecutwfc`) and corresponding charge density cutoffs (`ecutrho`).

#### Arguments
- `structure_folder` (str): Path to the folder containing structural files (e.g., `.cif`).
- `QEfile_folder` (str): Path to the folder where the generated input files will be saved.
- `pseudo_folder` (str): Path to the folder containing pseudopotential files, named according to element symbols (e.g., `Mn.upf`).

##### QE Control Parameters
- `restart_mode`, `tstress`, `tprnfor`, `nstep`, `etot_conv_thr`, `forc_conv_thr`

##### QE System Parameters
- `ecutwfc_range` (list): Range of `ecutwfc` values to test.
- `ecutrho_to_ecutwfc` (int): Ratio of `ecutrho` to `ecutwfc`.
- `occupations`, `smearing`, `degauss`, `nspin`, `initial_magnetization`, `nosym`

##### QE Electrons Parameters
- `electron_maxstep`, `conv_thr`, `mixing_beta`, `diagonalization`

##### QE Ions Parameters
- `ion_dynamics`

##### QE Cell Parameters
- `cell_dynamics`, `cell_dofree`, `kpoints`

---

### 2. K-point Mesh Test <a name="2-k-point-mesh-test"></a>

This function automates the generation of Quantum Espresso input files for testing different k-point meshes.

#### Arguments
- `structure_folder`, `QEfile_folder`, `pseudo_folder` (as described above)

##### QE Control, System, Electrons, Ions, and Cell Parameters
- Same as the parameters for the cutoff test, but without `ecutwfc_range`.

##### K-point Range
- `kpoints_range` (list): Range of k-point meshes to test (e.g., `[(1,1,1), (2,2,2), ..., (6,6,6)]`).

---

### 3. Postprocessing Results <a name="3-postprocessing-results"></a>

#### Cutoff Test Results
Extracts the results of the cutoff energy test from the output files.

##### Arguments
- `QEfile_folder` (str): Folder of computational files.
- `filename` (str): Output file name (e.g., `"vc-relax.out"`).
- `ecutwfc_range` (list): Same as in the cutoff test.
- `output_folder` (str): Path to save the processed results.

#### K-point Test Results
Extracts the results of the k-point mesh test from the output files.

##### Arguments
- `QEfile_folder` (str): Folder of computational files.
- `filename` (str): Output file name (e.g., `"vc-relax.out"`).
- `kpoints_range` (list): Same as in the k-point test.
- `output_folder` (str): Path to save the processed results.

---

## Usage Examples <a name="usage-examples"></a>

### Example 1: Cutoff Energy Test
```python
from QEflow import Parameter

structure_folder = "data3/structures_parameter"
QEfile_folder = "data3/cutoff_test"
pseudo_folder = "data3/SSSP_1.3.0_PBE_efficiency"

# CONTROL
calculation = "vc-relax"
restart_mode = "from_scratch"
tstress = True
tprnfor = True
nstep = 50
etot_conv_thr = 1.0E-4
forc_conv_thr = 1.0E-3

# SYSTEM
ecutwfc_range = [40, 45, 50, 55, 60, 65]
ecutrho_to_ecutwfc = 8
occupations = "smearing"
smearing = "gauss"
degauss = 0.05
nspin = 2
initial_magnetization = {'Cr': 5, 'Mn': 5, 'Fe': 4, 'Ni': 2, 'Cu': 1}
nosym = True

# ELECTRONS
electron_maxstep = 100
conv_thr = 1e-6
mixing_beta = 0.5
diagonalization = "david"

# IONS
ion_dynamics = "bfgs"

# CELL
cell_dynamics = "bfgs"
cell_dofree = "all"
kpoints = (3, 3, 3)

Parameter.cutoff_test(structure_folder, QEfile_folder, pseudo_folder,
                      calculation, restart_mode, tstress, tprnfor, nstep, etot_conv_thr, forc_conv_thr,
                      ecutwfc_range, ecutrho_to_ecutwfc, occupations, smearing, degauss, nspin, initial_magnetization, nosym,
                      electron_maxstep, conv_thr, mixing_beta, diagonalization,
                      ion_dynamics, cell_dynamics, cell_dofree, kpoints)
```

### Example 2: K-point Mesh Test
```python
from QEflow import Parameter

structure_folder = "data3/structures_parameter"
QEfile_folder = "data3/kpoints_test"
pseudo_folder = "data3/SSSP_1.3.0_PBE_efficiency"

# CONTROL
calculation = "vc-relax"
restart_mode = "from_scratch"
tstress = True
tprnfor = True
nstep = 50
etot_conv_thr = 1.0E-4
forc_conv_thr = 1.0E-3

# SYSTEM
ecutwfc = 50
ecutrho = 400
occupations = "smearing"
smearing = "gauss"
degauss = 0.05
nspin = 2
initial_magnetization = {'Cr': 5, 'Mn': 5, 'Fe': 4, 'Ni': 2, 'Cu': 1}
nosym = True

# ELECTRONS
electron_maxstep = 100
conv_thr = 1e-6
mixing_beta = 0.5
diagonalization = "david"

# IONS
ion_dynamics = "bfgs"

# CELL
cell_dynamics = "bfgs"
cell_dofree = "all"

# K-point Range
kpoints_range = [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5), (6, 6, 6)]

Parameter.kpoint_test(structure_folder, QEfile_folder, pseudo_folder,
                      calculation, restart_mode, tstress, tprnfor, nstep, etot_conv_thr, forc_conv_thr,
                      ecutwfc, ecutrho, occupations, smearing, degauss, nspin, initial_magnetization, nosym,
                      electron_maxstep, conv_thr, mixing_beta, diagonalization,
                      ion_dynamics, cell_dynamics, cell_dofree, kpoints_range)
```

### Example 3: Postprocessing Cutoff Results
```python
from QEflow import Parameter

QEfile_folder = 'data3/cutoff_test'
filename = 'vc-relax.out'
ecutwfc_range = [40, 45, 50, 55, 60, 65]
output_folder = 'data3/result/cutoff_result'

Parameter.cutoff_result(QEfile_folder, filename, ecutwfc_range, output_folder)
```

### Example 4: Postprocessing K-point Results
```python
from QEflow import Parameter

QEfile_folder = 'data3/kpoints_test'
filename = 'vc-relax.out'
kpoints_range = [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5), (6, 6, 6)]
output_folder = 'data3/result/kpoints_result'

Parameter.kpoints_result(QEfile_folder, filename, kpoints_range, output_folder)
```

---

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests to improve this repository.

---

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.

---
