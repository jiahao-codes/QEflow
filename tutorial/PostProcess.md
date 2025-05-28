

# QEflow.PostProcess

This module provides auxiliary postprocessing functions for Quantum Espresso.

## Function

1. [Convert to CIF](#convert-to-cif)
   - [Arguments](#qe-to-cif-arguments)
   - [Example Usage](#qe-to-cif-example)
2. [Vcrelax Status](#vcrelax-status)
   - [Arguments](#vcrelax-arguments)
   - [Example Usage](#vcrelax-example)
3. [Relax, SCF, and NSCF Status](#relax-status)
   - [Relax Status Example](#relax-status-example)
   - [SCF Status Example](#scf-status-example)
   - [NSCF Status Example](#nscf-status-example)
4. [Pdos Processing](#pdos-process)
   - [Arguments](#pdos-process-arguments)
   - [Example Usage](#pdos-process-example)
5. [Band Processing](#band-process)
   - [Arguments](#band-process-arguments)
   - [Example Usage](#band-process-example)

---

## Function

### 1. Convert to CIF <a name="convert-to-cif"></a>

This function converts Quantum Espresso relax output files into `.cif` format for structural analysis.

#### Arguments <a name="qe-to-cif-arguments"></a>
- `calculation` (str): The calculation task type, can be `vc-relax` or `relax`.
- `QEfile_folder` (str): Folder containing the computational files.
- `filaname` (str): Result file name.
- `output_folder` (str): Path to the folder where the output file (.cif) will be saved.

#### Example Usage <a name="qe-to-cif-example"></a>
```python
from QEflow import PostProcess

# Define input parameters
calculation = "vc-relax"
QEfile_folder = "data3/calculations"
filaname = "vc-relax.out"
output_folder = "data3/structures_vc_relaxed"

# Convert QE output to CIF format
PostProcess.qe_to_cif(calculation, QEfile_folder, filaname, output_folder)
```

---

### 2. Vcrelax Status <a name="vcrelax-status"></a>

This function retrieves the status of a vc-relax calculation from Quantum Espresso output files.

#### Arguments <a name="vcrelax-arguments"></a>
- `QEfile_folder` (str): Folder containing the computational files.
- `name` (str): Result file name.
- `output_folder` (str): Path to the folder where the output result file will be saved.

#### Example Usage <a name="vcrelax-example"></a>
```python
from QEflow import PostProcess

# Define input parameters
QEfile_folder = "data3/calculations"
name = "vc-relax.out"
output_folder = "data3/result"

# Run vc-relax status check
PostProcess.vcrelax_status(QEfile_folder, name, output_folder)
```

---

### 3. Relax, SCF, and NSCF Status <a name="relax-status"></a>

These functions retrieve the status of relax, SCF, or NSCF calculations from Quantum Espresso output files.

#### Relax Status Example <a name="relax-status-example"></a>
```python
from QEflow import PostProcess

# Define input parameters
QEfile_folder = "data/calculations"
filename = "relax.out"
output_folder = "data/result"

# Run relax status check
PostProcess.relax_status(QEfile_folder, filename, output_folder)
```

#### SCF Status Example <a name="scf-status-example"></a>
```python
from QEflow import PostProcess

# Define input parameters
QEfile_folder = "data/calculations"
filename = "scf.out"
output_folder = "data/result"

# Run SCF status check
PostProcess.scf_status(QEfile_folder, filename, output_folder)
```

#### NSCF Status Example <a name="nscf-status-example"></a>
```python
from QEflow import PostProcess

# Define input parameters
QEfile_folder = "data/calculations"
filename = "nscf.out"
output_folder = "data/result"

# Run NSCF status check
PostProcess.nscf_status(QEfile_folder, filename, output_folder)
```

---


### 4. Pdos Processing <a name="pdos-process"></a>

This function processes the projected density of states (PDOS) from the outputs.

#### Arguments <a name="pdos-process-arguments"></a>
- `QEfile_folder` (str): Folder containing the computational files.
- `output_folder` (str): Path to the folder where the processed PDOS output file will be saved.
- `Fermi_subtract` (bool): Whether Fermi levels need to be subtracted.
- `Fermi_source` (str): Specify which calculated Fermi level to use (`vc-relax`, `relax`, `scf`, `nscf`).
- `filename` (str): Result file name.

#### Example Usage <a name="pdos-process-example"></a>
```python
from QEflow import PostProcess

# Define input parameters
QEfile_folder = "data/calculations"
output_folder = "data/result/pdos_processed"
Fermi_source = "scf"
filename = "scf.out"
Fermi_subtract = True

# Run PDOS processing
PostProcess.pdos_process(QEfile_folder, output_folder, Fermi_source, filename, Fermi_subtract=Fermi_subtract)
```

---

### 5. Band Processing <a name="band-process"></a>

This function processes band structure data from the outputs.

#### Arguments <a name="band-process-arguments"></a>
- `QEfile_folder` (str): Folder containing the computational files.
- `result_prefix` (str): Prefix for the output result files.
- `output_folder` (str): Path to the folder where the processed band structure output will be saved.
- `Fermi_source` (str): Specify which calculated Fermi level to use (`vc-relax`, `relax`, `scf`, `nscf`).
- `filename` (str): Result file name.
- `Fermi_subtract` (bool): Whether Fermi levels need to be subtracted.

#### Example Usage <a name="band-process-example"></a>
```python
from QEflow import PostProcess

# Define input parameters
QEfile_folder = "data/calculations"
result_prefix = "QEflow"
output_folder = "data/result/band_processed"
Fermi_source = "scf"
filename = "scf.out"
Fermi_subtract = True

# Run band structure processing
PostProcess.band_process(QEfile_folder, result_prefix, output_folder, Fermi_source, filename, Fermi_subtract=Fermi_subtract)
```

---

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests to improve this repository.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.

## Notes

- Ensure all file paths and dependencies are correctly configured.
- The examples provided here are simplified. Adjust parameters based on the specific requirements of your workflow.
