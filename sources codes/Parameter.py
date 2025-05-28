import os
from pymatgen.io.pwscf import PWInput
from shutil import copy2
from pymatgen.core import Structure

def cutoff_test(structure_folder, QEfile_folder, pseudo_folder, 
            calculation, restart_mode, tstress, tprnfor, nstep, etot_conv_thr, forc_conv_thr,
            ecutwfc_range, ecutrho_to_ecutwfc, occupations, smearing, degauss, nspin, initial_magnetization, nosym, 
            electron_maxstep, conv_thr, mixing_beta, diagonalization, 
            ion_dynamics, cell_dynamics, cell_dofree, kpoints):

    if not os.path.exists(QEfile_folder):
        os.makedirs(QEfile_folder)

    num = 0
    for name in os.listdir(structure_folder):
        if name.endswith('.cif'):
            for ecutwfc in ecutwfc_range:
                structure_dir = os.path.join(structure_folder, name)
                structure = Structure.from_file(structure_dir)
                new_name = name.replace(".cif", "")
                
                prefix = new_name
    
                control = {
                    "calculation": calculation,
                    "restart_mode": restart_mode,
                    "pseudo_dir": "./",
                    "outdir": "./out",
                    "tstress": tstress,
                    "tprnfor": tprnfor,
                    "nstep": nstep,
                    "prefix": prefix,
                    "etot_conv_thr": etot_conv_thr,
                    "forc_conv_thr": forc_conv_thr
                }
                
                system = {
                    "ibrav": 0,
                    "nat": len(structure),
                    "ntyp": len(structure.symbol_set),
                    "ecutwfc": ecutwfc,
                    "ecutrho": ecutwfc*ecutrho_to_ecutwfc,
                    "occupations": occupations,
                    "smearing": smearing,
                    "degauss": degauss,
                    "nspin": nspin,
                    "nosym": nosym
                }
                
                if nspin == 2:
                    starting_magnetizations = {}
                    for i, element in enumerate(structure.symbol_set):
                        starting_magnetizations[f"starting_magnetization({i+1})"] = initial_magnetization.get(element, 0.0)
                    
                    system.update(starting_magnetizations)
                
                electrons = {
                    "electron_maxstep": electron_maxstep,
                    "conv_thr": conv_thr,
                    "mixing_beta": mixing_beta,
                    "diagonalization": diagonalization
                }
                
                ions = {
                    "ion_dynamics": ion_dynamics
                }
                
                cell = {
        
                }
                
                if calculation == "vc-relax":
                    cell.update(
                        {"cell_dynamics": cell_dynamics,
                        "cell_dofree": cell_dofree}
                                )     
                
                pseudo = {element: f"{element}.upf" for element in structure.symbol_set}
                
                pw_input = PWInput(
                    structure, pseudo=pseudo, control=control, system=system,
                    electrons=electrons, ions=ions, cell=cell, kpoints_grid=kpoints
                )   
                
                input_file_dir1 = os.path.join(QEfile_folder, new_name)
                if not os.path.exists(input_file_dir1):
                    os.makedirs(input_file_dir1)
                input_file_dir2 = os.path.join(input_file_dir1, f'{ecutwfc}Ry')
                if not os.path.exists(input_file_dir2):
                    os.makedirs(input_file_dir2)       
                input_file = os.path.join(input_file_dir2, f'{new_name}-{calculation}.in')
                pw_input.write_file(input_file)
                
                for element in structure.symbol_set:
                    pseudo_file = os.path.join(pseudo_folder, f'{element}.upf')
                    if os.path.exists(pseudo_file):
                        copy2(pseudo_file, input_file_dir2)
                    else:
                        print(f'{new_name} missing pseudo potential for {element}')
                num = num + 1
    print(f"Generated {num} computational files.")



from ase import Atoms
from ase.io import read
import os
from pymatgen.io.pwscf import PWInput
from shutil import copy2

def kpoint_test(structure_folder, QEfile_folder, pseudo_folder, 
            calculation, restart_mode, tstress, tprnfor, nstep, etot_conv_thr, forc_conv_thr,
            ecutwfc, ecutrho, occupations, smearing, degauss, nspin, initial_magnetization,nosym, 
            electron_maxstep, conv_thr, mixing_beta, diagonalization, 
            ion_dynamics, cell_dynamics, cell_dofree, kpoints_range):

    num = 0
    for name in os.listdir(structure_folder):
        if name.endswith('.cif'):
            for kpoints in kpoints_range:
                structure_dir = os.path.join(structure_folder, name)
                structure = Structure.from_file(structure_dir)
                new_name = name.replace(".cif", "")             
                prefix = new_name
    
                control = {
                    "calculation": calculation,
                    "restart_mode": restart_mode,
                    "pseudo_dir": "./",
                    "outdir": "./out",
                    "tstress": tstress,
                    "tprnfor": tprnfor,
                    "nstep": nstep,
                    "prefix": prefix,
                    "etot_conv_thr": etot_conv_thr,
                    "forc_conv_thr": forc_conv_thr
                }
                
                system = {
                    "ibrav": 0,
                    "nat": len(structure),
                    "ntyp": len(structure.symbol_set),
                    "ecutwfc": ecutwfc,
                    "ecutrho": ecutrho,
                    "occupations": occupations,
                    "smearing": smearing,
                    "degauss": degauss,
                    "nspin": nspin,
                    "nosym": nosym
                }
                
                if nspin == 2:
                    starting_magnetizations = {}
                    for i, element in enumerate(structure.symbol_set):
                        starting_magnetizations[f"starting_magnetization({i+1})"] = initial_magnetization.get(element, 0.0)
                    
                    system.update(starting_magnetizations)
                
                electrons = {
                    "electron_maxstep": electron_maxstep,
                    "conv_thr": conv_thr,
                    "mixing_beta": mixing_beta,
                    "diagonalization": diagonalization
                }
                
                ions = {
                    "ion_dynamics": ion_dynamics
                }
                
                cell = {
        
                }
                
                if calculation == "vc-relax":
                    cell.update(
                        {"cell_dynamics": cell_dynamics,
                        "cell_dofree": cell_dofree}
                                )     

                pseudo = {element: f"{element}.upf" for element in structure.symbol_set}
                
                pw_input = PWInput(
                    structure, pseudo=pseudo, control=control, system=system,
                    electrons=electrons, ions=ions, cell=cell, kpoints_grid=kpoints
                )   
                
                input_file_dir1 = os.path.join(QEfile_folder, new_name)
                if not os.path.exists(input_file_dir1):
                    os.makedirs(input_file_dir1)
                input_file_dir2 = os.path.join(input_file_dir1, f'kpoints{kpoints}')
                if not os.path.exists(input_file_dir2):
                    os.makedirs(input_file_dir2)       
                input_file = os.path.join(input_file_dir2, f'{new_name}-{calculation}.in')
                pw_input.write_file(input_file)
                
                for element in structure.symbol_set:
                    pseudo_file = os.path.join(pseudo_folder, f'{element}.upf')
                    if os.path.exists(pseudo_file):
                        copy2(pseudo_file, input_file_dir2)
                    else:
                        print(f'{new_name} missing pseudo potential for {element}')
                num = num + 1
    print(f"Generated {num} computational files.")

import numpy as np
import os
import pandas as pd

def cutoff_result(QEfile_folder, filename, ecutwfc_range, output_folder):

    def analyze_file(file_path):
        result = {
            "Cutoff Energy": None,
            "Total Energy": None,
            "Total Force": None,   
        }
        
        try:
            with open(file_path, 'r') as file:
                content = file.read()       
                
                # Find energy cutoff
                cutoff_index = content.find("kinetic-energy cutoff")
                if cutoff_index != -1:
                    cutoff_line = content[cutoff_index:content.find("\n", cutoff_index)]
                    cutoff_energy = cutoff_line.split()[3]  
                    result["Cutoff Energy"] = cutoff_energy
                    
                final_coord_index = content.find("End final coordinates")
                if final_coord_index != -1:
    
                    Fermi_energy_index = content.find("the Fermi energy is", final_coord_index)
                    if Fermi_energy_index != -1:
                                                       
                        energy_index = content.find("!    total energy", Fermi_energy_index)
                        if energy_index != -1:
                            energy_line = content[energy_index:content.find("\n", energy_index)]
                            total_energy = energy_line.split()[4]  
                            result["Total Energy"] = total_energy
                            
                            force_index = content.find("Total force", energy_index)
                            if force_index != -1:
                                force_line = content[force_index:content.find("\n", force_index)]
                                total_force = force_line.split()[3] 
                                result["Total Force"] = total_force
                                        
    
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            
        return result

    num = 0
    for name in os.listdir(QEfile_folder):

        results = []

        results_df = pd.DataFrame(columns=["Cutoff Energy", "Total Energy", "Total Force"])   

        ecutwfc_range_str = [str(i)+'Ry' for i in ecutwfc_range]

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        for cut_off in ecutwfc_range_str:
            structure_path = os.path.join(QEfile_folder, name)
            file_path1 = os.path.join(structure_path, cut_off)
            file_path2 = os.path.join(file_path1, filename)
            file_result = analyze_file(file_path2)
            results.append(file_result)

            results_df = pd.concat([pd.DataFrame([r]) for r in results], ignore_index=True)

            result_dir = os.path.join(output_folder, f'{name}.csv')
            results_df.to_csv(result_dir, index=False)

            num = num + 1
    print(f"Processed {num} computational files.")



def kpoints_result(QEfile_folder, filename, kpoints_range, output_folder):

    def analyze_file(file_path):
        result = {
            "Kpoints": None,
            "Total Energy": None,
            "Total Force": None,   
        }
        
        try:
            with open(file_path, 'r') as file:
                content = file.read()       
                    
                final_coord_index = content.find("End final coordinates")
                if final_coord_index != -1:
    
                    Fermi_energy_index = content.find("the Fermi energy is", final_coord_index)
                    if Fermi_energy_index != -1:
                                                       
                        energy_index = content.find("!    total energy", Fermi_energy_index)
                        if energy_index != -1:
                            energy_line = content[energy_index:content.find("\n", energy_index)]
                            total_energy = energy_line.split()[4]  
                            result["Total Energy"] = total_energy
                            
                            force_index = content.find("Total force", energy_index)
                            if force_index != -1:
                                force_line = content[force_index:content.find("\n", force_index)]
                                total_force = force_line.split()[3] 
                                result["Total Force"] = total_force
                                        
    
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            
        return result

    num = 0
    for name in os.listdir(QEfile_folder):

        results = []

        results_df = pd.DataFrame(columns=["Kpoints", "Total Energy", "Total Force"])   

        kpoints_range_str = ['kpoints'+str(i) for i in kpoints_range]

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)        
        
        for kpoints in kpoints_range_str:
            structure_path = os.path.join(QEfile_folder, name)
            file_path1 = os.path.join(structure_path, kpoints)
            file_path2 = os.path.join(file_path1, filename)
            file_result = analyze_file(file_path2)
            file_result["Kpoints"] = kpoints.replace('kpoints','')
            results.append(file_result)

            results_df = pd.concat([pd.DataFrame([r]) for r in results], ignore_index=True)

            result_dir = os.path.join(output_folder, f'{name}.csv')
            results_df.to_csv(result_dir, index=False)
            num = num + 1
    print(f"Processed {num} computational files.")
