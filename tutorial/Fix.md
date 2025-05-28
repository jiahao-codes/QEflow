

# QEflow.Fix
Modules for fixing and unfixing atoms in QE cell relax input files.

## Functions

1. [Fix Atoms](#fix-atoms)
   - [Arguments](#fix-atoms-args)
   - [Example Usage](#fix-atoms-example)
2. [Unfix Atoms](#unfix-atoms)
   - [Arguments](#unfix-atoms-args)
   - [Example Usage](#unfix-atoms-example)

---

### 1. Fix Atoms <a name="fix-atoms"></a>
Fixes atoms in QE input files. This function applies fixed constraints to the atoms based on the provided parameters.

#### Arguments <a name="fix-atoms-args"></a>
- `QEfile_folder` (str): Path to the folder containing Quantum Espresso input files.
- `input_file_prefix` (str): Prefix of the input files to process (e.g., 'vc-relax.in').
- `num_atoms` (int): The number of atoms to apply the fix constraints to.

#### Example Usage <a name="fix-atoms-example"></a>
```python
from QEflow import Fix
# Folder containing QE input files
QEfile_folder = 'data/surfaces_added_calculation'
input_file_prefix = 'vc-relax.in'
num_atoms = 8

# Apply fixed constraints to atoms
Fixing.fix_atoms(QEfile_folder, input_file_prefix, num_atoms)
```

---

### 2. Unfix Atoms <a name="unfix-atoms"></a>
Removes fixed constraints from atoms in QE input files. This function undoes the constraints applied using `fix_atoms`.

#### Arguments <a name="unfix-atoms-args"></a>
- `QEfile_folder` (str): Path to the folder containing Quantum Espresso input files.
- `input_file_prefix` (str): Prefix of the input files to process (e.g., 'vc-relax.in').

#### Example Usage <a name="unfix-atoms-example"></a>
```python
from QEflow import Fix
# Folder containing QE input files
QEfile_folder = 'data/surfaces_added_calculation'
input_file_prefix = 'vc-relax.in'

# Remove fixed constraints from atoms
Fixing.unfix_atoms(QEfile_folder, input_file_prefix)
```

---

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests to improve this repository.

## License
This repository is licensed under the MIT License. See the `LICENSE` file for details.

## Notes
- Ensure that all file paths and dependencies are correctly configured before running the functions.
- The examples provided here are simplified. Adjust parameters based on the specific requirements of your workflow.
