

# QEflow.Calculation
This module provides high-throughput auxiliary generation of input files for pw.x and so on.

## Function
1. [pw.x: scf](#aa)
   - [Arguments](#aa1)
   - [Example Usage](#aa2)
2. [pw.x: vc-relax](#bb)
   - [Arguments](#bb1)
   - [Example Usage](#bb2)
3. [pw.x: relax](#cc)
   - [Arguments](#cc1)
   - [Example Usage](#cc1)
4. [pw.x: nscf](#dd)
   - [Arguments](#dd1)
   - [Example Usage](#dd2)
5. [pw.x: bands](#ee)
   - [Arguments](#ee1)
   - [Example Usage](#ee2)
   - [Implementation Details](#ee3)
6. [bands.x](#ff)
   - [Arguments](#ff1)
   - [Example Usage](#ff2)
7. [projwfc.x](#gg)
   - [Arguments](#gg1)
   - [Example Usage](#gg2)



---

## Function

### 1. pw.x: scf <a name="aa"></a>
Automates the generation of input files for SCF (self-consistent field) calculations.

#### Arguments<a name="aa1"></a>
- `structure_folder` (str): Path to the folder containing structural files (e.g., `.cif`).
- `QEfile_folder` (str): Path to the folder where the generated input files will be saved.
- `pseudo_folder` (str): Path to the folder containing pseudopotential files, named according to element symbols (e.g., `Mn.upf, Co.upf`).

##### QE Control Parameters
- `restart_mode` (str): Restart mode (e.g., `"from_scratch"`).
- `tstress` (bool): Enable stress tensor calculation.
- `tprnfor` (bool): Enable force calculation.

##### QE System Parameters
- `ecutwfc` (int): Plane-wave cutoff energy.
- `ecutrho` (int): Charge density cutoff energy.
- `occupations` (str): Type of occupation (e.g., `"smearing"`).
- `smearing` (str): Type of smearing (e.g., `"gauss"`).
- `degauss` (float): Smearing width.
- `nspin` (int): Number of spin components.
- `initial_magnetization` (dict): Initial magnetization for each element.
- `nosym` (bool): Disable symmetry operations.

##### QE Electrons Parameters
- `electron_maxstep` (int): Maximum number of electronic iterations.
- `conv_thr` (float): Convergence threshold for electronic self-consistency.
- `mixing_beta` (float): Mixing parameter for electronic density.
- `diagonalization` (str): Type of diagonalization algorithm.

##### QE K-points
- `kpoints` (tuple): K-point mesh for Brillouin zone sampling.

#### Example Usage<a name="aa2"></a>
```python
from QEflow import Calculation

structure_folder = "data3/surfaces_added"
QEfile_folder = "data3/surfaces_added_calculation"
pseudo_folder = "data3/SSSP_1.3.0_PBE_efficiency"

Calculation.pwx_scf(structure_folder, QEfile_folder, pseudo_folder, 
                    restart_mode="from_scratch", tstress=True, tprnfor=True, 
                    ecutwfc=50, ecutrho=400, occupations="smearing", smearing="gauss", 
                    degauss=0.05, nspin=2, initial_magnetization={'Cr':5, 'Mn':5, 'Fe':4}, 
                    nosym=True, electron_maxstep=100, conv_thr=1e-6, mixing_beta=0.5, 
                    diagonalization="david", kpoints=(3, 3, 3))
```

### 2. pw.x: vc-relax <a name="bb"></a>
Automates the generation of input files for variable-cell relaxation calculations.

#### Arguments <a name="bb1"></a>
- `structure_folder` (str): Path to the folder containing structural files (e.g., `.cif`).
- `QEfile_folder` (str): Path to the folder where the generated input files will be saved.
- `pseudo_folder` (str): Path to the folder containing pseudopotential files, named according to element symbols (e.g., `Mn.upf, Co.upf`).

##### QE Control Parameters
- `restart_mode` (str): Restart mode (e.g., `"from_scratch"`).
- `tstress` (bool): Enable stress tensor calculation.
- `tprnfor` (bool): Enable force calculation.
- `nstep` (int): Maximum number of relaxation steps.
- `etot_conv_thr` (float): Convergence threshold for total energy.
- `forc_conv_thr` (float): Convergence threshold for forces.

##### QE System Parameters
- `ecutwfc` (int): Plane-wave cutoff energy.
- `ecutrho` (int): Charge density cutoff energy.
- `occupations` (str): Type of occupation (e.g., `"smearing"`).
- `smearing` (str): Type of smearing (e.g., `"gauss"`).
- `degauss` (float): Smearing width.
- `nspin` (int): Number of spin components.
- `initial_magnetization` (dict): Initial magnetization for each element (e.g., `{"Fe": 5.0}`).
- `nosym` (bool): Disable symmetry operations.

##### QE Electrons Parameters
- `electron_maxstep` (int): Maximum number of electronic iterations.
- `conv_thr` (float): Convergence threshold for electronic self-consistency.
- `mixing_beta` (float): Mixing parameter for electronic density.
- `diagonalization` (str): Type of diagonalization algorithm (e.g., `"david"`).

##### QE Ions Parameters
- `ion_dynamics` (str): Dynamics for ionic minimization (e.g., `"bfgs"`).

##### QE Cell Parameters
- `cell_dynamics` (str): Dynamics for cell optimization (e.g., `"bfgs"`).
- `cell_dofree` (str): Degrees of freedom for cell optimization (e.g., `"all"`).
- `kpoints` (tuple): K-point mesh for Brillouin zone sampling (e.g., `(3, 3, 3)`).

#### Example Usage <a name="bb2"></a>
```python
from QEflow import Calculation

structure_folder = "data/structures"
QEfile_folder = "data/calculations"
pseudo_folder = "data/pseudopotentials"

Calculation.pwx_vc_relax(structure_folder, QEfile_folder, pseudo_folder, 
                         restart_mode="from_scratch", tstress=True, tprnfor=True, nstep=100, 
                         etot_conv_thr=1.0E-4, forc_conv_thr=1.0E-3, ecutwfc=60, ecutrho=480, 
                         occupations="smearing", smearing="gauss", degauss=0.02, nspin=2, 
                         initial_magnetization={'Fe': 4, 'Ni': 2}, nosym=True, 
                         electron_maxstep=200, conv_thr=1e-6, mixing_beta=0.7, 
                         diagonalization="david", ion_dynamics="bfgs", cell_dynamics="bfgs", 
                         cell_dofree="all", kpoints=(4, 4, 4))
```


### 3. pw.x: relax <a name="cc"></a>
Automates the generation of input files for relaxation calculations using Quantum ESPRESSO.

#### Arguments <a name="cc1"></a>
- `structure_folder` (str): same as vc-relax.
- `QEfile_folder` (str): same as vc-relax.
- `pseudo_folder` (str): same as vc-relax.

##### QE Control Parameters
- same as vc-relax.

##### QE System Parameters
- same as vc-relax.

##### QE Electrons Parameters
- same as vc-relax.

##### QE Ions Parameters
- same as vc-relax.

##### QE K-Points Parameters
- same as vc-relax.

#### Example Usage <a name="bb2"></a>
```python
from QEflow import Calculation

structure_folder = "data/structures"
QEfile_folder = "data/calculations"
pseudo_folder = "data/pseudopotentials"

Calculation.pwx_relax(structure_folder, QEfile_folder, pseudo_folder, 
                      restart_mode="from_scratch", tstress=True, tprnfor=True, nstep=100, 
                      etot_conv_thr=1.0E-4, forc_conv_thr=1.0E-3, ecutwfc=60, ecutrho=480, 
                      occupations="smearing", smearing="gauss", degauss=0.02, nspin=2, 
                      initial_magnetization={'Fe': 4, 'Ni': 2}, nosym=True, 
                      electron_maxstep=200, conv_thr=1e-6, mixing_beta=0.7, 
                      diagonalization="david", ion_dynamics="bfgs", kpoints=(4, 4, 4))
```

                         
### 4. pw.x: nscf <a name="dd"></a>
Automates the generation of input files for NSCF (non-self-consistent field) calculations.

#### Arguments<a name="dd1"></a>
- `structure_folder` (str): Path to the folder containing structural files (e.g., `.cif`).
- `QEfile_folder` (str): Path to the folder where the generated input files will be saved.
- `pseudo_folder` (str): Path to the folder containing pseudopotential files.

##### QE Control Parameters
- `restart_mode` (str): Restart mode (e.g., `"from_scratch"`).

##### QE System Parameters
- `ecutwfc` (int): Plane-wave cutoff energy.
- `ecutrho` (int): Charge density cutoff energy.
- `occupations` (str): Type of occupation (e.g., `"smearing"`).
- `smearing` (str): Type of smearing (e.g., `"gauss"`).
- `degauss` (float): Smearing width.
- `nspin` (int): Number of spin components.
- `nosym` (bool): Disable symmetry operations.

##### QE K-points
- `kpoints` (tuple): K-point mesh for Brillouin zone sampling.

#### Example Usage<a name="dd2"></a>
```python
from QEflow import Calculation

structure_folder = "data/structures"
QEfile_folder = "data/calculations"
pseudo_folder = "data/pseudopotentials"

Calculation.pwx_nscf(structure_folder, QEfile_folder, pseudo_folder, 
                     restart_mode="from_scratch", ecutwfc=50, ecutrho=400, 
                     occupations="smearing", smearing="gauss", degauss=0.02, 
                     nspin=2, nosym=True, kpoints=(6, 6, 6))
```


### 5. pw.x: bands <a name="ee"></a>
Automates the generation of input files for band structure calculations using Quantum ESPRESSO.

#### Arguments<a name="ee1"></a>
- `structure_folder` (str): Path to the folder containing structural files (e.g., `.cif`).
- `QEfile_folder` (str): Path to the folder where the generated input files will be saved.
- `pseudo_folder` (str): Path to the folder containing pseudopotential files.

##### QE Control Parameters
- `restart_mode` (str): Restart mode (e.g., `"from_scratch"`).

##### QE System Parameters
- `ecutwfc` (int): Plane-wave cutoff energy.
- `ecutrho` (int): Charge density cutoff energy.
- `occupations` (str): Type of occupation (e.g., `"smearing"`).
- `smearing` (str): Type of smearing (e.g., `"gauss"`).
- `degauss` (float): Smearing width.
- `nspin` (int): Number of spin components.
- `initial_magnetization` (dict): Initial magnetization for each element (e.g., `{"Fe": 5.0}`).
- `nosym` (bool): Disable symmetry operations.

##### QE Electrons Parameters
- `diagonalization` (str): Type of diagonalization algorithm (e.g., `"david"`).

##### QE K-Points
- `kpoints_path` (list): High-symmetry k-point path for band structure calculations. If not provided, it will be generated automatically.
- `line_density` (int): Density of k-points along each line segment in the k-point path.

#### Example Usage<a name="ee2"></a>
```python
from QEflow import Calculation

structure_folder = "data/structures"
QEfile_folder = "data/calculations"
pseudo_folder = "data/pseudopotentials"

Calculation.pwx_bands(structure_folder, QEfile_folder, pseudo_folder, 
                      restart_mode="from_scratch", ecutwfc=60, ecutrho=480, 
                      occupations="smearing", smearing="gauss", degauss=0.02, 
                      nspin=2, initial_magnetization={'Fe': 4}, nosym=True, 
                      diagonalization="david", kpoints_path=None, line_density=20)
```
#### Implementation Details<a name="ee3"></a>
 **kpoints_path**: -   The `kpoints_path` argument allows the use of a custom k-point path. If set to `None` or `False`, the program will call the pymatgen library's K-point path-finding function to generate the path automatically.
    
-   The format of the k-point path should be a list, such as:
```python
kpoints_path = [
    [0.0, 0.0, 0.0],
    [0.5, 0.0, 0.0],
    [0.5, 0.5, 0.0],
    [0.5, 0.5, 0.5],
    [0.0, 0.0, 0.5]
]
```
---

### 6. bands.x <a name="ff"></a>
Automates the generation of input files for band analysis using Quantum ESPRESSO's `bands.x`.

#### Arguments <a name="ff1"></a>
- `QEfile_folder` (str): Path to the folder containing QE calculation folders.
- `result_prefix` (str): Prefix for the output band structure file.

#### Example Usage<a name="ff2"></a>
```python
from QEflow import Calculation

QEfile_folder = "data/calculations"
Calculation.bandsx(QEfile_folder, result_prefix="band_structure")
```



### 7. projwfc.x <a name="gg"></a>
Automates the generation of input files for PDOS (projected density of states) calculations using Quantum ESPRESSO.

#### Arguments <a name="gg1"></a>
- `QEfile_folder` (str): Path to the folder containing QE calculation folders.
- `ngauss` (int): Type of Gaussian smearing.
- `degauss` (float): Smearing width.
- `Emin` (float): Minimum energy for DOS calculations.
- `Emax` (float): Maximum energy for DOS calculations.
- `DeltaE` (float): Energy interval for DOS calculations.
- `result_prefix` (str): Prefix for the output PDOS file.

#### Example Usage<a name="gg2"></a>
```python
from QEflow import Calculation

QEfile_folder = "data/calculations"
Calculation.projwfcx(QEfile_folder, ngauss=1, degauss=0.01, Emin=-10, Emax=10, DeltaE=0.1, result_prefix="pdos_result")
```

