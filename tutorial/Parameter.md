
# QEflow.Parameter
This module provides high-throughput auxiliary preprocessing and postprocessing functions for parameter testing.

## Function

1. [Cutoff Energy Test](#cutoff-test)
   - [Arguments](#cutoff-test-args)
   - [Example Usage](#cutoff-test-example)
2. [K-point Mesh Test](#kpoint-test)
   - [Arguments](#kpoint-test-args)
   - [Example Usage](#kpoint-test-example)
3. [Postprocessing Results](#postprocessing)
   - [Cutoff Test Results](#cutoff-results)
   - [K-point Mesh Results](#kpoint-results)

---

## Function

### 1. Cutoff Energy Test <a name="cutoff-test"></a>
Generating testing files of various cutoff energies.

#### Arguments <a name="cutoff-test-args"></a>
- `structure_folder` (str): Path to the folder containing structural files (e.g., `.cif`).
- `QEfile_folder` (str): Path to the folder where the generated input files will be saved.
- `pseudo_folder` (str): Path to the folder containing pseudopotential files, named according to element symbols (e.g., `Mn.upf`).

##### QE Control Parameters
- `restart_mode`, `tstress`, `tprnfor`, `nstep`, `etot_conv_thr`, `forc_conv_thr`

##### QE System Parameters
- `ecutwfc_range` (list): Range of `ecutwfc` values to test.
- `ecutrho_to_ecutwfc` (int): Ratio of `ecutrho` to `ecutwfc`.
- `occupations`, `smearing`, `degauss`, `nspin`, `initial_magnetization`, `nosym`

##### QE Electrons Parameters
- `electron_maxstep`, `conv_thr`, `mixing_beta`, `diagonalization`

##### QE Ions Parameters
- `ion_dynamics`

##### QE Cell Parameters
- `cell_dynamics`, `cell_dofree`, `kpoints`

#### Example Usage <a name="cutoff-test-example"></a>
```python
from QEflow import Parameter

structure_folder = "data3/structures_parameter"
QEfile_folder = "data3/cutoff_test"
pseudo_folder = "data3/SSSP_1.3.0_PBE_efficiency"

Parameter.cutoff_test(
    structure_folder, QEfile_folder, pseudo_folder,
    calculation="vc-relax", restart_mode="from_scratch", tstress=True, tprnfor=True, nstep=50,
    etot_conv_thr=1.0E-4, forc_conv_thr=1.0E-3, ecutwfc_range=[40, 45, 50, 55, 60, 65],
    ecutrho_to_ecutwfc=8, occupations="smearing", smearing="gauss", degauss=0.05,
    nspin=2, initial_magnetization={'Cr': 5, 'Mn': 5, 'Fe': 4, 'Ni': 2, 'Cu': 1},
    nosym=True, electron_maxstep=100, conv_thr=1e-6, mixing_beta=0.5, diagonalization="david",
    ion_dynamics="bfgs", cell_dynamics="bfgs", cell_dofree="all", kpoints=(3, 3, 3)
)
```

### 2. K-point Mesh Test <a name="kpoint-test"></a>
Generating testing files of various k-point meshes.

#### Arguments <a name="kpoint-test-args"></a>
- `structure_folder` (str): Path to the folder containing structural files (e.g., `.cif`).
- `QEfile_folder` (str): Path to the folder where the generated input files will be saved.
- `pseudo_folder` (str): Path to the folder containing pseudopotential files, named according to element symbols.

##### QE Parameters
- `kpoints_range` (list): Range of k-point meshes to test (e.g., `[(1,1,1), (2,2,2), ..., (6,6,6)]`).
- Other QE parameters are similar to those used in the Cutoff Energy Test.

#### Example Usage <a name="kpoint-test-example"></a>
```python
from QEflow import Parameter

structure_folder = "data3/structures_parameter"
QEfile_folder = "data3/kpoints_test"
pseudo_folder = "data3/SSSP_1.3.0_PBE_efficiency"

Parameter.kpoint_test(
    structure_folder, QEfile_folder, pseudo_folder,
    calculation="vc-relax", restart_mode="from_scratch", tstress=True, tprnfor=True, nstep=50,
    etot_conv_thr=1.0E-4, forc_conv_thr=1.0E-3, ecutwfc=50, ecutrho=400, occupations="smearing",
    smearing="gauss", degauss=0.05, nspin=2, initial_magnetization={'Cr': 5, 'Mn': 5, 'Fe': 4, 'Ni': 2, 'Cu': 1},
    nosym=True, electron_maxstep=100, conv_thr=1e-6, mixing_beta=0.5, diagonalization="david",
    ion_dynamics="bfgs", cell_dynamics="bfgs", cell_dofree="all", kpoints_range=[(1,1,1), (2,2,2), (3,3,3), (4,4,4), (5,5,5), (6,6,6)]
)
```

### 3. Postprocessing Results <a name="postprocessing"></a>

#### Cutoff Test Results <a name="cutoff-results"></a>
Automatically extract results from the outputs of cutoff energy test.
```python
from QEflow import Parameter

QEfile_folder = "data3/cutoff_test"
filename = "vc-relax.out"
output_folder = "data3/result/cutoff_result"

Parameter.cutoff_result(QEfile_folder, filename, [40, 45, 50, 55, 60, 65], output_folder)
```

#### K-point Mesh Results <a name="kpoint-results"></a>
Automatically extract results from the outputs of  k-point mesh test.
```python
from QEflow import Parameter

QEfile_folder = "data3/kpoints_test"
filename = "vc-relax.out"
output_folder = "data3/result/kpoints_result"

Parameter.kpoints_result(QEfile_folder, filename, [(1,1,1), (2,2,2), (3,3,3), (4,4,4), (5,5,5), (6,6,6)], output_folder)
```

---

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests to improve this repository.

## License
This repository is licensed under the MIT License. See the `LICENSE` file for details.

## Notes
- Make sure all file paths and dependencies are correctly configured.
- The examples provided here are simplified. Adjust parameters based on the specific requirements of your workflow.

---
