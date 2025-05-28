import os

def fix_atoms(QEfile_folder, input_file_prefix, num_atoms):
    def find_relax_in_files(folder_path):
        for name in os.listdir(folder_path):
            if name.endswith(input_file_prefix):
                relax_in_files = name
        return relax_in_files

    num = 0
    for name in os.listdir(QEfile_folder):
        try:
            structure_folder = os.path.join(QEfile_folder, name)
            input_filename = find_relax_in_files(structure_folder)
            input_file_dir = os.path.join(structure_folder, input_filename)
            with open(input_file_dir, 'r') as file:
                lines = file.readlines()
            
            start_index = None
            end_index = None
            atomic_positions = []
            
            for i, line in enumerate(lines):
                if "ATOMIC_POSITIONS" in line:
                    start_index = i + 1
                elif "K_POINTS" in line:
                    end_index = i
                    break

            if start_index == None or end_index == None:
                print(f"Structure {name} not found ATOMIC_POSITIONS.")
            else:
                for i in range(start_index, end_index):
                    parts = lines[i].split()
                    element = parts[0]
                    position = list(map(float, parts[1:]))
                    atomic_positions.append([i, element, position])
                            
                sorted_atoms = sorted(atomic_positions, key=lambda x: x[2][2])
                min_atoms_indices = [atom[0] for atom in sorted_atoms[:num_atoms]]
                
                for i in range(start_index, end_index):
                    if i in min_atoms_indices and not lines[i].endswith('0 0 0\n'):
                        lines[i] = lines[i].rstrip() + " 0 0 0\n"
        
                with open(input_file_dir, 'w') as file:
                    file.writelines(lines)    

                num = num + 1

        except FileNotFoundError:
            print(f"{name} not QE file.")
    print(f"Processed {num} structures.")


import os

def unfix_atoms(QEfile_folder, input_file_prefix):
    def find_relax_in_files(folder_path):
        for name in os.listdir(folder_path):
            if name.endswith(input_file_prefix):
                relax_in_files = name
        return relax_in_files

    num = 0
    for name in os.listdir(QEfile_folder):
        try:
            structure_folder = os.path.join(QEfile_folder, name)
            input_filename = find_relax_in_files(structure_folder)
            input_file_dir = os.path.join(structure_folder, input_filename)
            with open(input_file_dir, 'r') as file:
                lines = file.readlines()
            
            start_index = None
            end_index = None
            
            for i, line in enumerate(lines):
                if "ATOMIC_POSITIONS" in line:
                    start_index = i + 1
                elif "K_POINTS" in line:
                    end_index = i
                    break
                    
            if start_index == None or end_index == None:
                print(f"Structure {name} not found ATOMIC_POSITIONS.")
            else:            
                for i in range(start_index, end_index):
                    if lines[i].endswith(' 0 0 0\n'):
                        lines[i] = lines[i].replace(' 0 0 0\n',' \n')
            
                with open(input_file_dir, 'w') as file:
                    file.writelines(lines)    

                num = num + 1
        except FileNotFoundError:
            print(f"File {structure_folder} not QE file.")

    print(f"Processed {num} structures.")
