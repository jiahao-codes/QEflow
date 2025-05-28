import os
import pandas as pd
import numpy as np

def vcrelax_status(QEfile_folder, filename, output_folder):

    results = []

    num = 0
    for name in os.listdir(QEfile_folder):
        structure_path = os.path.join(QEfile_folder, name)
        file_path = os.path.join(structure_path, filename)

        
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            result = {
                "Structure Name": name,
                "VC-Relax": 'Fail',
                "Total Energy": None,
                "Total Force": None,
                "Fermi Energy": None,
                "Running Time": None,
            }
                
            num = num + 1
            final_coord_index = content.find("End final coordinates")
            if final_coord_index != -1:
                
                self_consistent_index = content.find("End of self-consistent calculation", final_coord_index)
                if self_consistent_index != -1:
    
                    Fermi_energy_index = content.find("the Fermi energy is", self_consistent_index)
                    if Fermi_energy_index != -1:
                        Feimi_energy_line = content[Fermi_energy_index:content.find("\n", Fermi_energy_index)]
                        Feimi_energy = Feimi_energy_line.split()[4]  
                        result["Fermi Energy"] = Feimi_energy
                                
                        time_index = content.find("PWSCF        :", Fermi_energy_index)
                        if time_index != -1:
                            time_line = content[time_index:content.find("\n", time_index)]
                            running_time = time_line.split()[2]  
                            result["Running Time"] = running_time
                            result["VC-Relax"] = 'Success'
                                    
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
                                
            results.append(result)                            
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        
    results_df = pd.DataFrame(columns=["Structure Name", "Vc-relax", "Total Energy", "Total Force", "Fermi Energy", "Running Time"])    
    results_df = pd.concat([pd.DataFrame([r]) for r in results], ignore_index=True)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    result_path = os.path.join(output_folder, 'vc_relax_status.csv')
    
    results_df.to_csv(result_path, index=False)
    print(f"Processed {num} structures.")

def relax_status(QEfile_folder, filename, output_folder):

    results = []

    num = 0
    for name in os.listdir(QEfile_folder):
        structure_path = os.path.join(QEfile_folder, name)
        file_path = os.path.join(structure_path, filename)
        
        try:
            with open(file_path, 'r') as file:
                content = file.read()

            result = {
                "Structure Name": name,
                "Relax": 'Fail',
                "Total Energy": None,
                "Total Force": None,
                "Fermi Energy": None,
                "Running Time": None,
            }
                
            num = num + 1
            final_coord_index = content.find("End final coordinates")
            if final_coord_index != -1:

                Fermi_energy_index = content.find("the Fermi energy is", final_coord_index)
                if Fermi_energy_index != -1:
                    Feimi_energy_line = content[Fermi_energy_index:content.find("\n", Fermi_energy_index)]
                    Feimi_energy = Feimi_energy_line.split()[4]  
                    result["Fermi Energy"] = Feimi_energy
                            
                    time_index = content.find("PWSCF        :", Fermi_energy_index)
                    if time_index != -1:
                        time_line = content[time_index:content.find("\n", time_index)]
                        running_time = time_line.split()[2]  
                        result["Running Time"] = running_time                
                        result["Relax"] = 'Success'
                                                       
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
        
            results.append(result)
                    
        except FileNotFoundError:
            print(f"File {file_path} not found.")


    results_df = pd.DataFrame(columns=["Structure Name", "Relax", "Total Energy", "Total Force", "Fermi Energy", "Running Time"])    
    results_df = pd.concat([pd.DataFrame([r]) for r in results], ignore_index=True)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    result_path = os.path.join(output_folder, 'relax_status.csv')
    
    results_df.to_csv(result_path, index=False)
    print(f"Processed {num} structures.")

def scf_status(QEfile_folder, filename, output_folder):

    results = []

    num = 0
    for name in os.listdir(QEfile_folder):
        structure_path = os.path.join(QEfile_folder, name)
        file_path = os.path.join(structure_path, filename)
        
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            result = {
                "Structure Name": name,
                "SCF": 'Fail',
                "Total Energy": None,
                "Total Force": None,
                "Fermi Energy": None,
                "Running Time": None,
            }
            
            num = num + 1
            self_consistent_index = content.find("End of self-consistent calculation")
            if self_consistent_index != -1:

                Fermi_energy_index = content.find("the Fermi energy is", self_consistent_index)
                if Fermi_energy_index != -1:
                    Feimi_energy_line = content[Fermi_energy_index:content.find("\n", Fermi_energy_index)]
                    Feimi_energy = Feimi_energy_line.split()[4]  
                    result["Fermi Energy"] = Feimi_energy
                            
                    time_index = content.find("PWSCF        :", Fermi_energy_index)
                    if time_index != -1:
                        time_line = content[time_index:content.find("\n", time_index)]
                        running_time = time_line.split()[2]  
                        result["Running Time"] = running_time
                        result["SCF"] = 'Success'
                        
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

            results.append(result)
           
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            
    results_df = pd.DataFrame(columns=["Structure Name", "Scf", "Total Energy", "Total Force", "Fermi Energy", "Running Time"])    
    results_df = pd.concat([pd.DataFrame([r]) for r in results], ignore_index=True)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    result_path = os.path.join(output_folder, 'scf_status.csv')
    
    results_df.to_csv(result_path, index=False)
    print(f"Processed {num} structures.")



def nscf_status(QEfile_folder, filename, output_folder):

    results = []

    num = 0
    for name in os.listdir(QEfile_folder):
        structure_path = os.path.join(QEfile_folder, name)
        file_path = os.path.join(structure_path, filename)
        
        try:
            with open(file_path, 'r') as file:
                content = file.read()

            result = {
                "Structure Name": name,
                "Nscf": 'Fail',
                "Total Energy": None,
                "Total Force": None,
                "Fermi Energy": None,
                "Running Time": None,
            }
                
            num = num + 1
            band_index = content.find("End of band structure calculation")
            if band_index != -1:

                Fermi_energy_index = content.find("the Fermi energy is", band_index)
                if Fermi_energy_index != -1:
                    Feimi_energy_line = content[Fermi_energy_index:content.find("\n", Fermi_energy_index)]
                    Feimi_energy = Feimi_energy_line.split()[4]  
                    result["Fermi Energy"] = Feimi_energy
                            
                    time_index = content.find("PWSCF        :", Fermi_energy_index)
                    if time_index != -1:
                        time_line = content[time_index:content.find("\n", time_index)]
                        running_time = time_line.split()[2]  
                        result["Running Time"] = running_time
                        result["Nscf"] = 'Success'
            
            results.append(result)                             
        except FileNotFoundError:
            print(f"File {file_path} not found.")

    results_df = pd.DataFrame(columns=["Structure Name", "Nscf", "Total Energy", "Total Force", "Fermi Energy", "Running Time"])    
    results_df = pd.concat([pd.DataFrame([r]) for r in results], ignore_index=True)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    result_path = os.path.join(output_folder, 'nscf_status.csv')
    
    results_df.to_csv(result_path, index=False)
    print(f"Processed {num} structures.")

import os
from pymatgen.core import Lattice, Structure
from pymatgen.io.cif import CifWriter

def qe_to_cif(calculation, QEfile_folder, filename, output_folder):
    def extract_cell_parameters(text):
        lines = text.strip().split('\n')
        cell_params = []
        in_cell_parameters = False
        for line in lines:
            if "CELL_PARAMETERS" in line:
                in_cell_parameters = True
                continue
            if in_cell_parameters:
                if line.strip() == "":
                    break
                cell_params.append(list(map(float, line.split())))
        return cell_params
    
    def extract_atomic_positions(text):
        lines = text.strip().split('\n')
        atomic_positions = []
        in_atomic_positions = False
        for line in lines:
            if "ATOMIC_POSITIONS" in line:
                in_atomic_positions = True
                continue
            if in_atomic_positions:
                if line.strip() == "":
                    break
                parts = line.split()
                element = parts[0]
                position = list(map(float, parts[1:4]))
                atomic_positions.append([element, position])
        return atomic_positions

    results = []
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if calculation == 'vc-relax':
        num = 0
        for name in os.listdir(QEfile_folder):
            input_file_dir = os.path.join(QEfile_folder, name)
            out_dir = os.path.join(input_file_dir, filename)
            #if os.path.exists(out_dir): 
            try:
                with open(out_dir, 'r') as file:
                    content = file.read()

                final_coord_index1 = content.find("Begin final coordinates")
                final_coord_index2 = content.find("End final coordinates")
                if final_coord_index2 != -1:
                    self_consistent_index = content.find("End of self-consistent calculation", final_coord_index2)
                    if self_consistent_index != -1:
                        start_index = content.find("CELL_PARAMETERS", final_coord_index1)
                        end_index = content.find("End final coordinates", start_index)
                        extracted_content = content[start_index:end_index]
                        CELL_PARAMETERS = extract_cell_parameters(extracted_content)
                        ATOMIC_POSITIONS = extract_atomic_positions(extracted_content)
                        lattice = Lattice(CELL_PARAMETERS)
                        structure = Structure(lattice, [atom[0] for atom in ATOMIC_POSITIONS], [atom[1] for atom in ATOMIC_POSITIONS])
                        cif_writer = CifWriter(structure)
                        output_structure = os.path.join(output_folder, f'{name}.cif')
                        cif_writer.write_file(output_structure)

                        num = num + 1
                    else:
                        print(f"{name} relax Fail×")
                else:
                    print(f"{name} relax Fail×")

            except FileNotFoundError:
                print(f"File {out_dir} not found.")
            #else:
                #print(f"{name} not structure.")
    
        print(f"Successfully processed {num} structures.")

    if calculation == 'relax':
        num = 0
        for name in os.listdir(QEfile_folder):
            input_file_dir = os.path.join(QEfile_folder, name)
            for f in os.listdir(input_file_dir):
                if f.endswith('relax.in'):
                    in_dir = os.path.join(input_file_dir, f)
                    
            out_dir = os.path.join(input_file_dir, filename)
            #if os.path.exists(out_dir): 
            try:
                with open(in_dir, 'r') as file1:
                    content1 = file1.read()
                try:
                    with open(out_dir, 'r') as file2:
                        content2 = file2.read()
    
                    final_coord_index1 = content2.find("Begin final coordinates")
                    final_coord_index2 = content2.find("End final coordinates")
                    if final_coord_index2 != -1:
                        start_index = content2.find("ATOMIC_POSITIONS (crystal)", final_coord_index1)
                        end_index = content2.find("End final coordinates", start_index)
                        extracted_content2 = content2[start_index:end_index]
                        ATOMIC_POSITIONS = extract_atomic_positions(extracted_content2)
                        
                        index = content1.find("CELL_PARAMETERS angstrom")
                        extracted_content1 = content1[index:]
                        CELL_PARAMETERS = extract_cell_parameters(extracted_content1)
                        
                        lattice = Lattice(CELL_PARAMETERS)
                        structure = Structure(lattice, [atom[0] for atom in ATOMIC_POSITIONS], [atom[1] for atom in ATOMIC_POSITIONS])
                        cif_writer = CifWriter(structure)
                        output_structure = os.path.join(output_folder, f'{name}.cif')
                        cif_writer.write_file(output_structure)
    
                        num = num + 1
    
                    else:
                        print(f"{name} relax Fail×")
                        
                except FileNotFoundError:
                    print(f"File {out_dir} not found.")
            
            except FileNotFoundError:
                print(f"File {in_dir} not found.")
            #else:
                #print(f"{name} not structure.")
    
        print(f"Successfully processed {num} structures.")

    
import os
import csv
import pandas as pd
import numpy as np


def pdos_process(QEfile_folder, output_folder, Fermi_source, filename, Fermi_subtract = True):


    def readmatrix(folder_path, file):
        file_path = os.path.join(folder_path, file)

        try:

            with open(file_path, 'r') as file:
                lines = file.readlines()[1:]  
            array = np.array([line.split() for line in lines], dtype=float)
            return array
        except (IsADirectoryError, IOError) as e:
            print(f"{file} not dos")
            return None      

    def find_penultimate_char(s):
        return s[-2]
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)    

    if Fermi_source == 'relax' or Fermi_source == 'vc-relax':
        num = 0
        for name in os.listdir(QEfile_folder):

            output_folder2 = os.path.join(output_folder, name)
                
            if not os.path.exists(output_folder2):
                os.makedirs(output_folder2)        
            input_file_dir = os.path.join(QEfile_folder, name)
            relaxout_dir = os.path.join(input_file_dir, filename)
            if os.path.exists(relaxout_dir): 
                try:
                    with open(relaxout_dir, 'r') as file:
                        content = file.read()
    
                    final_coord_index = content.find("End final coordinates")
                    if final_coord_index != -1:
    
                        self_consistent_index = content.find("End of self-consistent calculation", final_coord_index)
                        if self_consistent_index != -1:
                            
                            Fermi_energy_index = content.find("the Fermi energy is", self_consistent_index)
                            if Fermi_energy_index != -1:
                                Feimi_energy_line = content[Fermi_energy_index:content.find("\n", Fermi_energy_index)]
                                Feimi_energy = Feimi_energy_line.split()[4]  
                                
                                pdos_dir = os.path.join(input_file_dir, 'pdos')                      
                    
                                for file in os.listdir(pdos_dir):
    
                                    array = readmatrix(pdos_dir, file)
                                    if array is not None:
                                        if Fermi_subtract == True:
                                            array[:,0] = array[:,0] - float(Feimi_energy)
                                            
                                        
                                        output_file = os.path.join(output_folder2, f"{file}.csv")
                                        with open(output_file, mode='w', newline='') as csvfile:
                                            csvwriter = csv.writer(csvfile)
        
                                            for idx in range(array.shape[0]):
                                                csvwriter.writerow(array[idx])
    
    
                                for file in os.listdir(pdos_dir):
                                    if 'tot' in file:
                                        array = readmatrix(pdos_dir, file)
                                        if Fermi_subtract == True:
                                            energy = array[:,0] - float(Feimi_energy)
                                        else:
                                            energy = array[:,0]
                                        count_rows = len(energy)
         
                                element_orbitals = {'s': np.zeros((count_rows, 1)), 'p': np.zeros((count_rows, 1)), 'd': np.zeros((count_rows, 1)), 'f': np.zeros((count_rows, 1))}
    
                                for file in os.listdir(pdos_dir):
                                    orbital_type = find_penultimate_char(file)
                
                                    if orbital_type in ['s', 'p', 'd', 'f']:
                                        array = readmatrix(pdos_dir, file)
                                        
                                        # Get the number of columns in element_orbitals[orbital_type]
                                        target_columns = array[:, 1:].shape[1]
                                        
                                        # Get the number of columns in element_orbitals[orbital_type]
                                        current_columns = element_orbitals[orbital_type].shape[1]
                                        
                                        # If element_orbitals[orbital_type] has fewer columns, pad it with zeros
                                        if current_columns < target_columns:
                                            # Calculate how many columns to pad
                                            padding_columns = target_columns - current_columns
                                            # Pad element_orbitals[orbital_type] with zeros
                                            padding = np.zeros((element_orbitals[orbital_type].shape[0], padding_columns))
                                            # Concatenate the padding to element_orbitals[orbital_type]
                                            element_orbitals[orbital_type] = np.hstack((element_orbitals[orbital_type], padding))
                                        
                                        # Now add array[:, 1:] to element_orbitals[orbital_type]
                                        element_orbitals[orbital_type] += array[:, 1:]
    
                                element_orbitals['s'] = np.insert(element_orbitals['s'], 0, energy, axis=1)
                                element_orbitals['p'] = np.insert(element_orbitals['p'], 0, energy, axis=1)
                                element_orbitals['d'] = np.insert(element_orbitals['d'], 0, energy, axis=1)
                                element_orbitals['f'] = np.insert(element_orbitals['f'], 0, energy, axis=1)
                                
                                for orbital in ['s', 'p', 'd', 'f']:
                                    output_file = os.path.join(output_folder2, f"{name}_{orbital}.csv")                                       
    
                                    with open(output_file, mode='w', newline='') as csvfile:
                                        csvwriter = csv.writer(csvfile)
                                        for idx in range(array.shape[0]):
                                            csvwriter.writerow(element_orbitals[orbital][idx])
                                                  
                                num = num + 1
     
                except FileNotFoundError:
                    print(f"{name} calculation failed.")
            else:
                print(f"{name} not structure.")
    
        print(f"Successfully processed {num} structures.")

    if Fermi_source == 'scf':
        num = 0
        for name in os.listdir(QEfile_folder):

            input_file_dir = os.path.join(QEfile_folder, name)
            scfout_dir = os.path.join(input_file_dir, filename)
            output_folder2 = os.path.join(output_folder, name)
                
            if not os.path.exists(output_folder2):
                os.makedirs(output_folder2)    
            
            if os.path.exists(scfout_dir): 
                try:
                    with open(scfout_dir, 'r') as file:
                        content = file.read()
    
                    self_consistent_index = content.find("End of self-consistent calculation")
                    if self_consistent_index != -1:
                        
                        Fermi_energy_index = content.find("the Fermi energy is", self_consistent_index)
                        if Fermi_energy_index != -1:
                            Feimi_energy_line = content[Fermi_energy_index:content.find("\n", Fermi_energy_index)]
                            Feimi_energy = Feimi_energy_line.split()[4]  
                            
                            pdos_dir = os.path.join(input_file_dir, 'pdos')                      
   
                            for file in os.listdir(pdos_dir):

                                array = readmatrix(pdos_dir, file)
                                if array is not None:
                                    if Fermi_subtract == True:
                                        array[:,0] = array[:,0] - float(Feimi_energy)
                                        
                                    
                                    output_file = os.path.join(output_folder2, f"{file}.csv")
                                    with open(output_file, mode='w', newline='') as csvfile:
                                        csvwriter = csv.writer(csvfile)
    
                                        for idx in range(array.shape[0]):
                                            csvwriter.writerow(array[idx])


                            for file in os.listdir(pdos_dir):
                                if 'tot' in file:
                                    array = readmatrix(pdos_dir, file)
                                    if Fermi_subtract == True:
                                        energy = array[:,0] - float(Feimi_energy)
                                    else:
                                        energy = array[:,0]
                                    count_rows = len(energy)
     
                            element_orbitals = {'s': np.zeros((count_rows, 1)), 'p': np.zeros((count_rows, 1)), 'd': np.zeros((count_rows, 1)), 'f': np.zeros((count_rows, 1))}

                            for file in os.listdir(pdos_dir):
                                orbital_type = find_penultimate_char(file)
            
                                if orbital_type in ['s', 'p', 'd', 'f']:
                                    array = readmatrix(pdos_dir, file)
                                    
                                    # Get the number of columns in element_orbitals[orbital_type]
                                    target_columns = array[:, 1:].shape[1]
                                    
                                    # Get the number of columns in element_orbitals[orbital_type]
                                    current_columns = element_orbitals[orbital_type].shape[1]
                                    
                                    # If element_orbitals[orbital_type] has fewer columns, pad it with zeros
                                    if current_columns < target_columns:
                                        # Calculate how many columns to pad
                                        padding_columns = target_columns - current_columns
                                        # Pad element_orbitals[orbital_type] with zeros
                                        padding = np.zeros((element_orbitals[orbital_type].shape[0], padding_columns))
                                        # Concatenate the padding to element_orbitals[orbital_type]
                                        element_orbitals[orbital_type] = np.hstack((element_orbitals[orbital_type], padding))
                                    
                                    # Now add array[:, 1:] to element_orbitals[orbital_type]
                                    element_orbitals[orbital_type] += array[:, 1:]

                            element_orbitals['s'] = np.insert(element_orbitals['s'], 0, energy, axis=1)
                            element_orbitals['p'] = np.insert(element_orbitals['p'], 0, energy, axis=1)
                            element_orbitals['d'] = np.insert(element_orbitals['d'], 0, energy, axis=1)
                            element_orbitals['f'] = np.insert(element_orbitals['f'], 0, energy, axis=1)
                            
                            for orbital in ['s', 'p', 'd', 'f']:
                                output_file = os.path.join(output_folder2, f"{name}_{orbital}.csv")                                       

                                with open(output_file, mode='w', newline='') as csvfile:
                                    csvwriter = csv.writer(csvfile)
                                    for idx in range(array.shape[0]):
                                        csvwriter.writerow(element_orbitals[orbital][idx])


                                            
                            num = num + 1
     
                except FileNotFoundError:
                    print(f"{name} calculation failed.")
            else:
                print(f"{name} not structure.")
    
        print(f"Successfully processed {num} structures.")

    if Fermi_source == 'nscf':
        num = 0
        for name in os.listdir(QEfile_folder):
            input_file_dir = os.path.join(QEfile_folder, name)
            scfout_dir = os.path.join(input_file_dir, filename)
            output_folder2 = os.path.join(output_folder, name)
                
            if not os.path.exists(output_folder2):
                os.makedirs(output_folder2)        

            if os.path.exists(scfout_dir): 
                try:
                    with open(scfout_dir, 'r') as file:
                        content = file.read()
                        
                    band_index = content.find("End of band structure calculation")
                    if band_index != -1:
                    
                        Fermi_energy_index = content.find("the Fermi energy is", band_index)
                        if Fermi_energy_index != -1:
                            Feimi_energy_line = content[Fermi_energy_index:content.find("\n", Fermi_energy_index)]
                            Feimi_energy = Feimi_energy_line.split()[4]  
                            
                            pdos_dir = os.path.join(input_file_dir, 'pdos')                      
    
                            for file in os.listdir(pdos_dir):

                                array = readmatrix(pdos_dir, file)
                                if array is not None:
                                    if Fermi_subtract == True:
                                        array[:,0] = array[:,0] - float(Feimi_energy)
                                        
                                    
                                    output_file = os.path.join(output_folder2, f"{file}.csv")
                                    with open(output_file, mode='w', newline='') as csvfile:
                                        csvwriter = csv.writer(csvfile)
    
                                        for idx in range(array.shape[0]):
                                            csvwriter.writerow(array[idx])


                            for file in os.listdir(pdos_dir):
                                if 'tot' in file:
                                    array = readmatrix(pdos_dir, file)
                                    if Fermi_subtract == True:
                                        energy = array[:,0] - float(Feimi_energy)
                                    else:
                                        energy = array[:,0]
                                    count_rows = len(energy)
     
                            element_orbitals = {'s': np.zeros((count_rows, 1)), 'p': np.zeros((count_rows, 1)), 'd': np.zeros((count_rows, 1)), 'f': np.zeros((count_rows, 1))}

                            for file in os.listdir(pdos_dir):
                                orbital_type = find_penultimate_char(file)
            
                                if orbital_type in ['s', 'p', 'd', 'f']:
                                    array = readmatrix(pdos_dir, file)
                                    
                                    # Get the number of columns in element_orbitals[orbital_type]
                                    target_columns = array[:, 1:].shape[1]
                                    
                                    # Get the number of columns in element_orbitals[orbital_type]
                                    current_columns = element_orbitals[orbital_type].shape[1]
                                    
                                    # If element_orbitals[orbital_type] has fewer columns, pad it with zeros
                                    if current_columns < target_columns:
                                        # Calculate how many columns to pad
                                        padding_columns = target_columns - current_columns
                                        # Pad element_orbitals[orbital_type] with zeros
                                        padding = np.zeros((element_orbitals[orbital_type].shape[0], padding_columns))
                                        # Concatenate the padding to element_orbitals[orbital_type]
                                        element_orbitals[orbital_type] = np.hstack((element_orbitals[orbital_type], padding))
                                    
                                    # Now add array[:, 1:] to element_orbitals[orbital_type]
                                    element_orbitals[orbital_type] += array[:, 1:]

                            element_orbitals['s'] = np.insert(element_orbitals['s'], 0, energy, axis=1)
                            element_orbitals['p'] = np.insert(element_orbitals['p'], 0, energy, axis=1)
                            element_orbitals['d'] = np.insert(element_orbitals['d'], 0, energy, axis=1)
                            element_orbitals['f'] = np.insert(element_orbitals['f'], 0, energy, axis=1)
                            
                            for orbital in ['s', 'p', 'd', 'f']:
                                output_file = os.path.join(output_folder2, f"{name}_{orbital}.csv")                                       

                                with open(output_file, mode='w', newline='') as csvfile:
                                    csvwriter = csv.writer(csvfile)
                                    for idx in range(array.shape[0]):
                                        csvwriter.writerow(element_orbitals[orbital][idx])
                                            
                            num = num + 1
     
                except FileNotFoundError:
                    print(f"{name} calculation failed.")
            else:
                print(f"{name} not structure.")
    
        print(f"Successfully processed {num} structures.")

import csv
import os
import pandas as pd
import numpy as np


def band_process(QEfile_folder, result_prefix, output_folder, Fermi_source, filename, Fermi_subtract = True):

    def calculate_bandpath_interval(kpoints_path):

        interval = [0]
        
        for i in range(1, len(kpoints_path)):
            dist = np.linalg.norm(np.array(kpoints_path[i]) - np.array(kpoints_path[i - 1]))
            interval.append(interval[-1] + dist)
        return interval
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)    
    if Fermi_source == 'relax' or Fermi_source == 'vc-relax':
        num = 0
        for name in os.listdir(QEfile_folder):
            input_file_dir = os.path.join(QEfile_folder, name)
            relaxout_dir = os.path.join(input_file_dir, filename)
            if os.path.exists(relaxout_dir): 
                try:
                    with open(relaxout_dir, 'r') as file:
                        content = file.read()
    
                    final_coord_index = content.find("End final coordinates")
                    if final_coord_index != -1:
    
                        self_consistent_index = content.find("End of self-consistent calculation", final_coord_index)
                        if self_consistent_index != -1:
                            
                            Fermi_energy_index = content.find("the Fermi energy is", self_consistent_index)
                            if Fermi_energy_index != -1:
                                Feimi_energy_line = content[Fermi_energy_index:content.find("\n", Fermi_energy_index)]
                                Feimi_energy = Feimi_energy_line.split()[4]  
                                
                                
                                bands_dir = os.path.join(input_file_dir, 'band')
                                data_dir = os.path.join(bands_dir, f'{result_prefix}')
                
                            
                                with open(data_dir, 'r') as file:
                                    lines = file.readlines()  
                                    lines = lines[1:]    
                                 
                                k_points = []
                                y_data = []
                                
                                current_y_data = []
                                
                                for line in lines:
                                        values = line.split()
                                    
                                        if len(values) == 3:
    
                                            if current_y_data:
                                                y_data.append(current_y_data)
                                                current_y_data = []
                                            
                                            k_points.append([float(val) for val in values])
                                        
                                        else:
                                            current_y_data.extend([float(val) for val in values])
                                
                                if current_y_data:
                                    y_data.append(current_y_data)
                            
                                if Fermi_subtract == True:
                                    y_data = np.array(y_data) - float(Feimi_energy)
    
                                output_file = os.path.join(output_folder, f'{name}.csv')
                                
                                with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                                    writer = csv.writer(csvfile)
                                    
                                    for idx in range(y_data.shape[0]):
                                        writer.writerow(y_data[idx])        

                                output_file2 = os.path.join(output_folder, f'{name}-k-coordinate.csv')
                                with open(output_file2, 'w', newline='', encoding='utf-8') as csvfile:
                                    writer = csv.writer(csvfile)
                                    
                                    for idx in range(y_data.shape[0]):
                                        writer.writerow(k_points[idx])    
                                        
                                x_coords = calculate_bandpath_interval(k_points)        
                                output_file3 = os.path.join(output_folder, f'{name}-k-interval.csv')
                                with open(output_file3, 'w', newline='', encoding='utf-8') as csvfile:
                                    writer = csv.writer(csvfile)
                                    
                                    for idx in range(len(x_coords)):
                                        writer.writerow([x_coords[idx]])    
                                        
                                num = num + 1
                                
                except FileNotFoundError:
                    print(f"{name} calculation failed.")
            else:
                print(f"{name} not structure.")
        print(f"Successfully processed {num} structures.")
    
    if Fermi_source == 'scf':
        num = 0
        for name in os.listdir(QEfile_folder):
            input_file_dir = os.path.join(QEfile_folder, name)
            scfout_dir = os.path.join(input_file_dir, filename)
            if os.path.exists(scfout_dir): 
                try:
                    with open(scfout_dir, 'r') as file:
                        content = file.read()

                    self_consistent_index = content.find("End of self-consistent calculation")
                    if self_consistent_index != -1:
                        
                        Fermi_energy_index = content.find("the Fermi energy is", self_consistent_index)
                        if Fermi_energy_index != -1:
                            Feimi_energy_line = content[Fermi_energy_index:content.find("\n", Fermi_energy_index)]
                            Feimi_energy = Feimi_energy_line.split()[4]  
                            
                            
                            bands_dir = os.path.join(input_file_dir, 'band')
                            data_dir = os.path.join(bands_dir, f'{result_prefix}')
            
                        
                            with open(data_dir, 'r') as file:
                                lines = file.readlines()  
                                lines = lines[1:]    
                             
                            k_points = []
                            y_data = []
                            
                            current_y_data = []
                            
                            for line in lines:
                                    values = line.split()
                                
                                    if len(values) == 3:

                                        if current_y_data:
                                            y_data.append(current_y_data)
                                            current_y_data = []
                                        
                                        k_points.append([float(val) for val in values])
                                    
                                    else:
                                        current_y_data.extend([float(val) for val in values])
                            
                            if current_y_data:
                                y_data.append(current_y_data)
                        
                            if Fermi_subtract == True:
                                y_data = np.array(y_data) - float(Feimi_energy)

                            output_file = os.path.join(output_folder, f'{name}.csv')
                            
                            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                                writer = csv.writer(csvfile)
                                
                                for idx in range(y_data.shape[0]):
                                    writer.writerow(y_data[idx])        

                            output_file2 = os.path.join(output_folder, f'{name}-k-coordinate.csv')
                            with open(output_file2, 'w', newline='', encoding='utf-8') as csvfile:
                                writer = csv.writer(csvfile)
                                
                                for idx in range(y_data.shape[0]):
                                    writer.writerow(k_points[idx])    
                                    
                            x_coords = calculate_bandpath_interval(k_points)        
                            output_file3 = os.path.join(output_folder, f'{name}-k-interval.csv')
                            with open(output_file3, 'w', newline='', encoding='utf-8') as csvfile:
                                writer = csv.writer(csvfile)
                                
                                for idx in range(len(x_coords)):
                                    writer.writerow([x_coords[idx]])    
                            num = num + 1
                                
                except FileNotFoundError:
                    print(f"{name} calculation failed.")
            else:
                print(f"{name} not structure.")
        print(f"Successfully processed {num} structures.")
    

    if Fermi_source == 'nscf':
        num = 0
        for name in os.listdir(QEfile_folder):
            input_file_dir = os.path.join(QEfile_folder, name)
            nscfout_dir = os.path.join(input_file_dir, filename)
            if os.path.exists(nscfout_dir): 
                try:
                    with open(nscfout_dir, 'r') as file:
                        content = file.read()
                    band_index = content.find("End of band structure calculation")
                    if band_index != -1:
                               
                        Fermi_energy_index = content.find("the Fermi energy is", band_index)
                        if Fermi_energy_index != -1:
                            Feimi_energy_line = content[Fermi_energy_index:content.find("\n", Fermi_energy_index)]
                            Feimi_energy = Feimi_energy_line.split()[4]  
                            
                            
                            bands_dir = os.path.join(input_file_dir, 'band')
                            data_dir = os.path.join(bands_dir, f'{result_prefix}')
            
                        
                            with open(data_dir, 'r') as file:
                                lines = file.readlines()  
                                lines = lines[1:]    
                             
                            k_points = []
                            y_data = []
                            
                            current_y_data = []
                            
                            for line in lines:
                                    values = line.split()
                                
                                    if len(values) == 3:

                                        if current_y_data:
                                            y_data.append(current_y_data)
                                            current_y_data = []
                                        
                                        k_points.append([float(val) for val in values])
                                    
                                    else:
                                        current_y_data.extend([float(val) for val in values])
                            
                            if current_y_data:
                                y_data.append(current_y_data)
                        
                            if Fermi_subtract == True:
                                y_data = np.array(y_data) - float(Feimi_energy)

                            output_file = os.path.join(output_folder, f'{name}.csv')
                            
                            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                                writer = csv.writer(csvfile)
                                
                                for idx in range(y_data.shape[0]):
                                    writer.writerow(y_data[idx])        

                            output_file2 = os.path.join(output_folder, f'{name}-k-coordinate.csv')
                            with open(output_file2, 'w', newline='', encoding='utf-8') as csvfile:
                                writer = csv.writer(csvfile)
                                
                                for idx in range(y_data.shape[0]):
                                    writer.writerow(k_points[idx])    
                                    
                            x_coords = calculate_bandpath_interval(k_points)        
                            output_file3 = os.path.join(output_folder, f'{name}-k-interval.csv')
                            with open(output_file3, 'w', newline='', encoding='utf-8') as csvfile:
                                writer = csv.writer(csvfile)
                                
                                for idx in range(len(x_coords)):
                                    writer.writerow([x_coords[idx]])    
                                        
                            num = num + 1
                                
                except FileNotFoundError:
                    print(f"{name} calculation failed.")
            else:
                print(f"{name} not structure.")
        print(f"Successfully processed {num} structures.")