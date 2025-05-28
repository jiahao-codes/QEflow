import os
from pymatgen.io.pwscf import PWInput
from shutil import copy2
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.core import Structure

def pwx_scf(structure_folder, QEfile_folder, pseudo_folder, restart_mode,
            tstress, tprnfor, ecutwfc, ecutrho, occupations, smearing, degauss, 
            nspin, initial_magnetization, nosym, electron_maxstep, conv_thr, mixing_beta, diagonalization, kpoints):

    if not os.path.exists(QEfile_folder):
        os.makedirs(QEfile_folder)

    num = 0
    for name in os.listdir(structure_folder):
        if name.endswith('.cif'):
    
            structure_dir = os.path.join(structure_folder, name)
            structure = Structure.from_file(structure_dir)
            #structure = AseAtomsAdaptor.get_structure(structure)
            new_name = name.replace(".cif", "")             
            prefix = new_name
    
            control = {
                "calculation": 'scf',
                "restart_mode": restart_mode,
                "pseudo_dir": "./",
                "outdir": "./out",
                "prefix": prefix,
                "tstress": tstress,
                "tprnfor": tprnfor
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
    
            }
                
            cell = {
    
            }
                       
            pseudo = {element: f"{element}.upf" for element in structure.symbol_set}
            
            pw_input = PWInput(
                structure, pseudo=pseudo, control=control, system=system,
                electrons=electrons, ions=ions, cell=cell, kpoints_grid=kpoints
            )   
            
            input_file_fold = os.path.join(QEfile_folder, f'{new_name}')
            if not os.path.exists(input_file_fold):
                os.makedirs(input_file_fold)
                
            input_file_dir = os.path.join(input_file_fold, f'{new_name}-scf.in')    
            pw_input.write_file(input_file_dir)
            
            for element in structure.symbol_set:
                pseudo_file = os.path.join(pseudo_folder, f'{element}.upf')
                if os.path.exists(pseudo_file):
                    copy2(pseudo_file, input_file_fold)
                else:
                    print(f'{new_name} missing pseudo potential for {element}')
            num = num + 1

    print(f"Successfully processed {num} structures.")


import os
from ase.io import read
from pymatgen.io.pwscf import PWInput
from shutil import copy2

def pwx_relax(structure_folder, QEfile_folder, pseudo_folder, 
            restart_mode, tstress, tprnfor, nstep, etot_conv_thr, forc_conv_thr,
            ecutwfc, ecutrho, occupations, smearing, degauss, 
            nspin, initial_magnetization, nosym, electron_maxstep, conv_thr, mixing_beta, diagonalization, 
            ion_dynamics, kpoints):

    if not os.path.exists(QEfile_folder):
        os.makedirs(QEfile_folder)

    num = 0
    for name in os.listdir(structure_folder):
        if name.endswith('.cif'):
    
            structure_dir = os.path.join(structure_folder, name)
            structure = Structure.from_file(structure_dir)
            #structure = AseAtomsAdaptor.get_structure(structure)
            new_name = name.replace(".cif", "")             
            prefix = new_name
    
            control = {
                "calculation": 'relax',
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
            
           
            pseudo = {element: f"{element}.upf" for element in structure.symbol_set}
            
            pw_input = PWInput(
                structure, pseudo=pseudo, control=control, system=system,
                electrons=electrons, ions=ions, cell=cell, kpoints_grid=kpoints
            )   
            
            input_file_fold = os.path.join(QEfile_folder, f'{new_name}')
            if not os.path.exists(input_file_fold):
                os.makedirs(input_file_fold)
                
            input_file_dir = os.path.join(input_file_fold, f'{new_name}-relax.in')    
            pw_input.write_file(input_file_dir)
            
            for element in structure.symbol_set:
                pseudo_file = os.path.join(pseudo_folder, f'{element}.upf')
                if os.path.exists(pseudo_file):
                    copy2(pseudo_file, input_file_fold)
                else:
                    print(f'{new_name} missing pseudo potential for {element}')

            num = num + 1

    print(f"Successfully processed {num} structures.")



def pwx_vc_relax(structure_folder, QEfile_folder, pseudo_folder, 
            restart_mode, tstress, tprnfor, nstep, etot_conv_thr, forc_conv_thr,
            ecutwfc, ecutrho, occupations, smearing, degauss, 
            nspin, initial_magnetization, nosym, electron_maxstep, conv_thr, mixing_beta, diagonalization, 
            ion_dynamics, cell_dynamics, cell_dofree, kpoints):

    if not os.path.exists(QEfile_folder):
        os.makedirs(QEfile_folder)

    num = 0
    for name in os.listdir(structure_folder):
        if name.endswith('.cif'):
    
            structure_dir = os.path.join(structure_folder, name)
            structure = Structure.from_file(structure_dir)
            #structure = AseAtomsAdaptor.get_structure(structure)
            new_name = name.replace(".cif", "")             
            prefix = new_name
    
            control = {
                "calculation": 'vc-relax',
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
                "cell_dynamics": cell_dynamics,
                "cell_dofree": cell_dofree
            }
            
            pseudo = {element: f"{element}.upf" for element in structure.symbol_set}
            
            pw_input = PWInput(
                structure, pseudo=pseudo, control=control, system=system,
                electrons=electrons, ions=ions, cell=cell, kpoints_grid=kpoints
            )   
            
            input_file_fold = os.path.join(QEfile_folder, f'{new_name}')
            if not os.path.exists(input_file_fold):
                os.makedirs(input_file_fold)
                
            input_file_dir = os.path.join(input_file_fold, f'{new_name}-vc-relax.in')    
            pw_input.write_file(input_file_dir)
            
            for element in structure.symbol_set:
                pseudo_file = os.path.join(pseudo_folder, f'{element}.upf')
                if os.path.exists(pseudo_file):
                    copy2(pseudo_file, input_file_fold)
                else:
                    print(f'{new_name} missing pseudo potential for {element}')

            num = num + 1

    print(f"Successfully processed {num} structures.")





import os
from ase.io import read
from pymatgen.io.pwscf import PWInput
from shutil import copy2

def pwx_nscf(structure_folder, QEfile_folder, pseudo_folder, restart_mode,
            ecutwfc, ecutrho, occupations, smearing, degauss, 
            nspin, initial_magnetization, nosym, diagonalization, kpoints):

    if not os.path.exists(QEfile_folder):
        os.makedirs(QEfile_folder)

    num = 0
    for name in os.listdir(structure_folder):
        if name.endswith('.cif'):
            structure_dir = os.path.join(structure_folder, name)
            structure = Structure.from_file(structure_dir)
            #structure = AseAtomsAdaptor.get_structure(structure)
            new_name = name.replace(".cif", "")             
            prefix = new_name

            control = {
                "calculation": "nscf",
                "restart_mode": restart_mode,
                "pseudo_dir": "./",
                "outdir": "./out",
                "prefix": prefix
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
                "diagonalization": diagonalization
            }

            pseudo = {element: f"{element}.upf" for element in structure.symbol_set}
            
            pw_input = PWInput(
                structure, pseudo=pseudo, control=control, system=system,
                electrons=electrons, kpoints_grid=kpoints
            )

            input_file_fold = os.path.join(QEfile_folder, f'{new_name}')
            if not os.path.exists(input_file_fold):
                os.makedirs(input_file_fold)
                
            input_file_dir = os.path.join(input_file_fold, f'{new_name}-nscf.in')    
            pw_input.write_file(input_file_dir)
            
            for element in structure.symbol_set:
                pseudo_file = os.path.join(pseudo_folder, f'{element}.upf')
                if os.path.exists(pseudo_file):
                    copy2(pseudo_file, input_file_fold)
                else:
                    print(f'{new_name} missing pseudo potential for {element}')
            num = num + 1
    print(f"Successfully processed {num} structures.")


import os
from ase.io import read
from pymatgen.io.pwscf import PWInput
from pymatgen.symmetry.bandstructure import HighSymmKpath
from shutil import copy2

def pwx_bands(structure_folder, QEfile_folder, pseudo_folder, restart_mode,
          ecutwfc, ecutrho, occupations, smearing, degauss, 
          nspin, initial_magnetization, nosym, diagonalization, kpoints_path, line_density):

    if not os.path.exists(QEfile_folder):
        os.makedirs(QEfile_folder)

    num = 0
    for name in os.listdir(structure_folder):
        if name.endswith('.cif'):
            structure_dir = os.path.join(structure_folder, name)
            structure = Structure.from_file(structure_dir)
            #structure = AseAtomsAdaptor.get_structure(structure)
            new_name = name.replace(".cif", "")             
            prefix = new_name

            control = {
                "calculation": "bands",
                "restart_mode": restart_mode,
                "pseudo_dir": "./",
                "outdir": "./out",
                "prefix": prefix
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
                "diagonalization": diagonalization
            }

            pseudo = {element: f"{element}.upf" for element in structure.symbol_set}

            pw_input = PWInput(
                structure, pseudo=pseudo, control=control, system=system,
                electrons=electrons
            )

            input_file_fold = os.path.join(QEfile_folder, f'{new_name}')
            if not os.path.exists(input_file_fold):
                os.makedirs(input_file_fold)
                
            input_file_dir = os.path.join(input_file_fold, f'{new_name}-bands.in')    
            pw_input.write_file(input_file_dir)

            kpoints_list = []
            labels = []
            
            if not kpoints_path:
                #symm_structure = SpacegroupAnalyzer(structure).get_symmetrized_structure()
                kpath = HighSymmKpath(structure)
                for k, v in kpath.kpath["kpoints"].items():
                    kpoints_list.append(v)
                    labels.append(str(k))
                
            else:

                kpoints_list = kpoints_path
                labels = [None] * len(kpoints_path)  
        
            with open(input_file_dir, 'r') as file:
                content = file.read()
        
            # 找到文件中特定的块并进行替换
            first_index = content.find("ATOMIC_POSITIONS crystal")
            second_index = content.find("K_POINTS automatic")
            third_index = content.find("CELL_PARAMETERS angstrom")
        
            if second_index != -1 and third_index != -1 and second_index < third_index:
                content = content[:second_index] + content[third_index:]
        
        
            # 写入新的 K_POINTS 文件
            with open(input_file_dir, "w") as f:
                f.write(content + '\n')
                f.write("K_POINTS crystal_b\n")
                f.write(f"{len(kpoints_list)}\n")
                for kpt, label in zip(kpoints_list, labels):
                    if label:
                        f.write(f"{kpt[0]:.8f} {kpt[1]:.8f} {kpt[2]:.8f} {line_density}  # {label}\n")
                    else:
                        f.write(f"{kpt[0]:.8f} {kpt[1]:.8f} {kpt[2]:.8f} {line_density}\n")

            
            for element in structure.symbol_set:
                pseudo_file = os.path.join(pseudo_folder, f'{element}.upf')
                if os.path.exists(pseudo_file):
                    copy2(pseudo_file, input_file_fold)

            num = num + 1

    print(f"Successfully processed {num} structures.")



import os

def projwfcx(QEfile_folder, ngauss, degauss, 
            Emin, Emax, DeltaE, result_prefix): 

    num = 0    
    for name in os.listdir(QEfile_folder):

        content = (
            "&PROJWFC\n"
            "    prefix = '" + name + "',\n"
            "    outdir = './out',\n"
            f"    ngauss = {ngauss},\n"
            f"    degauss = {degauss},\n"
            f"    Emin = {Emin},\n"
            f"    Emax = {Emax},\n"
            f"    DeltaE = {DeltaE},\n"
            "    filpdos = './pdos/" + result_prefix + "',\n"
            "/\n"
        )
        input_file_folder = os.path.join(QEfile_folder, name)
        pdos_dir = os.path.join(input_file_folder, 'pdos')
        if not os.path.exists(pdos_dir):
            os.makedirs(pdos_dir)                        
        input_file = os.path.join(input_file_folder, f'{name}-pdos.in')
        with open(input_file, 'w') as file:
            file.write(content)

        num = num + 1
    print(f"Successfully processed {num} structures.")


import os


def bandsx(QEfile_folder, result_prefix):
    
    num = 0    
    for name in os.listdir(QEfile_folder):

        content = (
            "&BANDS\n"
            "    prefix = '" + name + "',\n"
            "    outdir = './out',\n"
            "    filband = './band/" + result_prefix + "',\n"
            "/\n"
        )
        input_file_folder = os.path.join(QEfile_folder, name)
        bands_folder = os.path.join(input_file_folder, 'band')
        if not os.path.exists(bands_folder):
            os.makedirs(bands_folder)                        
        input_file = os.path.join(input_file_folder, f'{name}-bandsx.in')
        with open(input_file, 'w') as file:
            file.write(content)
        num = num + 1

    print(f"Successfully processed {num} structures.")

                



