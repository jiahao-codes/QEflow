
# QE_Flow: Preprocessing and Postprocessing Tools for Quantum Espresso

This repository provides high-throughput auxiliary preprocessing and postprocessing functions for Quantum Espresso simulations, designed for efficient and automated workflows.

---

## Table of Contents

1. [Installation](#installation)
2. [Features](#features)
   - [1. Fix Atoms in Input Files](#1-fix-atoms-in-input-files)
   - [2. Unfix Atoms in Input Files](#2-unfix-atoms-in-input-files)
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

### 1. Fix Atoms in Input Files <a name="1-fix-atoms-in-input-files"></a>

This function modifies Quantum Espresso input files to fix a specified number of atoms in the structure, making them immobile during structural relaxation.

#### Arguments
- `QEfile_folder` (str): Path to the folder containing Quantum Espresso input files.
- `input_file_prefix` (str): The prefix of the `.in` input files to process.
- `num_atoms` (int): The number of atoms to fix in the structure.

#### Example Usage
```python
from QEflow import Fixing

# Define input parameters
QEfile_folder = 'data3/surfaces_calculation'
input_file_prefix = 'vc-relax.in'
num_atoms = 8

# Fix atoms in input files
Fixing.fix_atoms(QEfile_folder, input_file_prefix, num_atoms)
```

---

### 2. Unfix Atoms in Input Files <a name="2-unfix-atoms-in-input-files"></a>

This function removes the fixed status of atoms in Quantum Espresso input files, allowing all atoms to relax during the calculation.

#### Arguments
- `QEfile_folder` (str): Path to the folder containing Quantum Espresso input files.
- `input_file_prefix` (str): The prefix of the `.in` input files to process.

#### Example Usage
```python
from QEflow import Fixing

# Define input parameters
QEfile_folder = 'data3/surfaces_added_calculation'
input_file_prefix = 'vc-relax.in'

# Unfix atoms in input files
Fixing.unfix_atoms(QEfile_folder, input_file_prefix)
```

---

## Usage Examples <a name="usage-examples"></a>

### Example 1: Fixing Atoms in Input Files
Suppose you have a set of Quantum Espresso input files stored in the folder `data3/surfaces_calculation`, and you want to fix the positions of 8 atoms in these files. You can use the following script:

```python
from QEflow import Fixing

QEfile_folder = 'data3/surfaces_calculation'
input_file_prefix = 'vc-relax.in'
num_atoms = 8

Fixing.fix_atoms(QEfile_folder, input_file_prefix, num_atoms)
```

### Example 2: Unfixing Atoms in Input Files
If you want to unfix the atoms in the input files located in the folder `data3/surfaces_added_calculation`, use the following script:

```python
from QEflow import Fixing

QEfile_folder = 'data3/surfaces_added_calculation'
input_file_prefix = 'vc-relax.in'

Fixing.unfix_atoms(QEfile_folder, input_file_prefix)
```

---

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests to improve this repository.

---

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.

---

### Notes

- Ensure that the folder paths and input file prefixes are correctly configured before running the scripts.
- Adjust the number of fixed atoms (`num_atoms`) based on the specific requirements of your simulations.

---
