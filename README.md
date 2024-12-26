
# QE_Flow: Preprocessing and Postprocessing Tools for Quantum Espresso

This repository provides high-throughput auxiliary preprocessing and postprocessing functions for Quantum Espresso simulations, designed for efficient and automated workflows.

---

## Table of Contents

1. [Installation](#installation)
2. [Features](#features)
   - [1. Element Substitution](#1-element-substitution)
   - [2. Add Adsorption](#2-add-adsorption)
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

### 1. Element Substitution <a name="1-element-substitution"></a>

This function replaces specific elements in a crystal structure with other elements to create new structural configurations. It is particularly useful for generating doped or substituted structures for high-throughput calculations.

#### Arguments
- `structure_path` (str): Path to the original structure file (relative path recommended).
- `output_folder` (str): Path to the folder where the new structures will be saved.
- `elements_to_replace` (list): List of elements to be replaced in the structure.
- `new_elements` (list): List of elements to substitute into the structure.
- `num_atoms_to_replace` (int): Number of atoms to replace per structure.
- `num_new_structures` (int): Number of new structures to generate.

#### Example Usage
```python
from QE_Flow import Modeling

# Define input parameters
structure_path = 'data2/structures/Mn2O4.cif'
output_folder = 'data2/structures'
elements_to_replace = ['Mn']
new_elements = ['Mn', 'Fe', 'Co', 'Ni']
num_atoms_to_replace = 2
num_new_structures = 15

# Run element substitution
Modeling.element_substitution(structure_path, output_folder, elements_to_replace, new_elements, num_atoms_to_replace, num_new_structures)
```

---

### 2. Add Adsorption <a name="2-add-adsorption"></a>

This function adds adsorbed atoms to specified adsorption sites on surfaces, generating multiple new configurations for analysis.

#### Arguments
- `surface_folder` (str): Path to the folder containing surface structure files (e.g., `.cif`).
- `output_folder` (str): Path to the folder where new structures with adsorbates will be saved.
- `add_atom` (str): The atom to be adsorbed onto the surface.
- `element_range` (list): Range of elements that define adsorption sites.
- `x_range` (list): Fractional x-coordinate range for adsorption sites.
- `y_range` (list): Fractional y-coordinate range for adsorption sites.
- `x_shift` (float): x-offset of the adsorbed atom relative to the adsorption site (in Ångströms).
- `y_shift` (float): y-offset of the adsorbed atom relative to the adsorption site (in Ångströms).
- `z_shift` (float): Vertical distance between the adsorbed atom and the adsorption site (in Ångströms).

#### Example Usage
```python
from QE_Flow import Modeling

# Define input parameters
surface_folder = "data/surfaces"
output_folder = "data/surfaces_added"
add_atom = 'H'
element_range = ['O', 'S']
x_range = [0.3, 0.4]
y_range = [0.3, 0.4]
x_shift = 0
y_shift = 0
z_shift = 1

# Run adsorption addition
Modeling.add_adsorption(surface_folder, output_folder, add_atom, element_range, x_range, y_range, x_shift, y_shift, z_shift)
```

---

## Usage Examples <a name="usage-examples"></a>

### Example 1: Element Substitution
To create 15 new structures by substituting 2 manganese atoms with a combination of Mn, Fe, Co, and Ni in the original structure:

```python
from QE_Flow import Modeling

structure_path = 'data2/structures/Mn2O4.cif'
output_folder = 'data2/structures'
elements_to_replace = ['Mn']
new_elements = ['Mn', 'Fe', 'Co', 'Ni']
num_atoms_to_replace = 2
num_new_structures = 15

Modeling.element_substitution(structure_path, output_folder, elements_to_replace, new_elements, num_atoms_to_replace, num_new_structures)
```

### Example 2: Add Adsorption
To add hydrogen atoms to surfaces with adsorption sites defined by oxygen and sulfur atoms:

```python
from QE_Flow import Modeling

surface_folder = "data/surfaces"
output_folder = "data/surfaces_added"
add_atom = 'H'
element_range = ['O', 'S']
x_range = [0.3, 0.4]
y_range = [0.3, 0.4]
x_shift = 0
y_shift = 0
z_shift = 1

Modeling.add_adsorption(surface_folder, output_folder, add_atom, element_range, x_range, y_range, x_shift, y_shift, z_shift)
```

---

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests to improve this repository.

---

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.

---

### Notes

- Make sure all file paths and dependencies are correctly configured.
- The examples provided here are simplified. Adjust parameters based on the specific requirements of your workflow.

---
