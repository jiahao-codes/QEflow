import os
import random
import copy
from collections import Counter
from pymatgen.core import Structure
from pymatgen.io.ase import AseAtomsAdaptor
from pymatgen.io.cif import CifWriter

def element_substitution(structure_path, output_folder, elements_to_replace, new_elements, num_atoms_to_replace, num_new_structures):
    def generate_structure_name(new_atomic_positions):
        element_counts = Counter([atom[0] for atom in new_atomic_positions])
        structure_name = ''.join([f"{element}{count}" for element, count in sorted(element_counts.items())])
        return structure_name
    
    structure = Structure.from_file(structure_path)
    atomic_positions = []
    #structure = AseAtomsAdaptor.get_structure(structure)
    for site in structure:
        element = str(site.specie)
        element = element.replace('Element ','')
        coords = site.frac_coords
        position = list(map(float, coords))
        atomic_positions.append([element, position])
    
    replace_indices = [i for i, atom in enumerate(atomic_positions) if atom[0] in elements_to_replace]
    
    if num_atoms_to_replace > len(replace_indices):
        print(f"The number of atoms to be replaced: {num_atoms_to_replace}\n exceeds the number of replaceable atoms in the original structure: {len(replace_indices)}")
    
    new_structures = []
    structure_names = []

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    num = 0
    
    while len(new_structures) < num_new_structures:
        new_atomic_positions = copy.deepcopy(atomic_positions)
        
        indices_to_replace = random.sample(replace_indices, num_atoms_to_replace)

        for index in indices_to_replace:
            new_element = random.choice(new_elements)
            new_atomic_positions[index][0] = new_element

        new_structure = Structure(structure.lattice, [site[0] for site in new_atomic_positions], [site[1] for site in new_atomic_positions])
        
        if (new_structure not in new_structures) and (new_atomic_positions != atomic_positions):

            new_structures.append(new_structure)
            
            structure_name = generate_structure_name(new_atomic_positions)
            structure_names.append(structure_name)

            cif_writer = CifWriter(new_structure)
            structure_name = generate_structure_name(new_atomic_positions)        
            if structure_names.count(structure_name) > 1:
                output_structure = os.path.join(output_folder, f'{structure_name}({structure_names.count(structure_name)}).cif')
                cif_writer.write_file(output_structure)
            else:
                output_structure = os.path.join(output_folder, f'{structure_name}.cif')
            cif_writer.write_file(output_structure)
            num = num + 1
    print(f"Generated {num} structures.")



import numpy as np
import os
import pandas as pd
import pymatgen
from pymatgen.core import Lattice, Structure, Molecule, Element
from pymatgen.io.ase import AseAtomsAdaptor
from pymatgen.io.pwscf import PWInput
from pymatgen.io.cif import CifWriter

def add_adsorption(surface_folder, output_folder, add_atom, element_range, x_range, y_range, x_shift=0, y_shift=0, z_shift=1):
    def read_elements_positions(structure):
        structure = Structure.from_file(structure)
        atomic_positions = []
        #structure = AseAtomsAdaptor.get_structure(structure)
        for site in structure:
            element = str(site.specie)
            element = element.replace('Element ','')
            coords = site.frac_coords
            position = list(map(float, coords))
            atomic_positions.append([element, position])
        return atomic_positions

    num = 0
    for name in os.listdir(surface_folder):    
        if name.endswith('.cif'):
            surface_dir = os.path.join(surface_folder, name)
            surface = Structure.from_file(surface_dir)        

            max_z = -float('inf')
            max_position = None
            for site in surface.sites:
                frac_position = site.frac_coords
                position = site.coords
                if site.species_string in element_range and x_range[0] < frac_position[0] < x_range[1] and y_range[0] < frac_position[1] < y_range[1]:
                    if position[2] > max_z:
                        max_z = position[2]
                        max_position = position    
            if np.any(max_position == None):
                print(f'surface {name} fail')   
            atomic_positions = read_elements_positions(surface_dir)
            add_atom_positions = np.array(max_position) + np.array([x_shift, y_shift, z_shift])
            lattice = surface.lattice
            fractional_coords = lattice.get_fractional_coords(add_atom_positions)  
            atomic_positions.append([add_atom, list(fractional_coords)])
            surface_new = Structure(lattice, [site[0] for site in atomic_positions], [site[1] for site in atomic_positions])
            cif_writer = CifWriter(surface_new)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)     
            newname = name.replace('.cif','')
            output_surface = os.path.join(output_folder,f'{newname}-{add_atom}.cif')
            cif_writer.write_file(output_surface)
            num = num + 1 
    print(f"Processed {num} structures.")
