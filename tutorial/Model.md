
# QEflow.Model
This module provides high-throughput auxiliary for cell modeling.

## Function
1. [Element Substitution](#aa)
   - [Arguments](#aa1)
   - [Example Usage1](#aa2)
   - [Example Usage2](#aa3)
2. [Add Adsorption](#bb)
   - [Arguments](#bb1)
   - [Example Usage](#bb2)
---

## Function

### 1. Element Substitution <a name="aa"></a>

This function replaces specific elements in a crystal structure with other elements to create new structural configurations. It is particularly useful for generating doped or element substituted structures for high-throughput calculations. 
**Only structure of '.cif' format are supported.**

#### Arguments <a name="aa1"></a>
- `structure_path` (str): Path to the original structure file ( `.cif`).
- `output_folder` (str): Path to the folder where the new structures will be saved.
- `elements_to_replace` (list): List of elements to be replaced in the structure.
- `new_elements` (list): List of elements to substitute into the structure.
- `num_atoms_to_replace` (int): Number of atoms to replace per structure.
- `num_new_structures` (int): Number of new structures to generate.

#### Example Usage1 <a name="aa2"></a>
To create 15 new structures by randomly substituting 2 manganese atoms in the original structure, with a combination of Mn, Fe, Co, and Ni:
```python
from QEflow import Model

# Define input parameters
structure_path = 'data/structures/Mn2O4.cif'
output_folder = 'data/structures'
elements_to_replace = ['Mn']
new_elements = ['Mn', 'Fe', 'Co', 'Ni']
num_atoms_to_replace = 2
num_new_structures = 15

# Run element substitution
Model.element_substitution(structure_path, output_folder, elements_to_replace, new_elements, num_atoms_to_replace, num_new_structures)
```
#### Example Usage2 <a name="aa3"></a>
Perform element substitution at the octahedral sites (occupied by Co) in the spinel ZnCo₂O₄ structure, generating other spinel-type structures.
```python
from QEflow import Model
for i in ['Cr', 'Mn', 'Fe', 'Ni', 'Cu']:
    structure_path = 'data/structures/Zn2Co4O8.cif'   # Path of the original structure, using relative paths (ubsequent examples follow the same format)
    output_folder = 'data/structures'   # The folder path of the generated structure
    elements_to_replace = ['Co']   # Type of element to be replaced
    new_elements = [i]   # New element type
    num_atoms_to_replace = 4   # Number of atoms to be replaced
    num_new_structures = 1   # Number of new structures to be generated
    
    Model.element_substitution(structure_path, output_folder, elements_to_replace, new_elements, num_atoms_to_replace, num_new_structures)
```
---

### 2. Add Adsorption <a name="bb"></a>

This function adds adsorbed atoms to specified adsorption sites on surfaces.
**Only structure of '.cif' format are supported.**
#### Arguments<a name="bb1"></a>
- `surface_folder` (str): Path to the folder containing surface structure files ( `.cif`).
- `output_folder` (str): Path to the folder where new structures with adsorbates will be saved.
- `add_atom` (str): The atom to be adsorbed onto the surface.
- `element_range` (list): Range of elements that define adsorption sites.
- `x_range` (list): Fractional x-coordinate range for adsorption sites.
- `y_range` (list): Fractional y-coordinate range for adsorption sites.
- `x_shift` (float): x-offset of the adsorbed atom relative to the adsorption site (in Ångströms).
- `y_shift` (float): y-offset of the adsorbed atom relative to the adsorption site (in Ångströms).
- `z_shift` (float): Vertical distance between the adsorbed atom and the adsorption site (in Ångströms).

#### Example Usage<a name="bb2"></a>
Adds a hydrogen atom to the adsorption position in the specified fractional coordinate range.
```python
from QEflow import Model

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
Model.add_adsorption(surface_folder, output_folder, add_atom, element_range, x_range, y_range, x_shift, y_shift, z_shift)
```

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests to improve this repository.
## License
This repository is licensed under the MIT License. See the `LICENSE` file for details.
## Notes
- Make sure all file paths and dependencies are correctly configured.
- The examples provided here are simplified. Adjust parameters based on the specific requirements of your workflow.

