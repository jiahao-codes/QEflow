
# QE_Flow: Postprocessing Tools for Quantum Espresso

This repository provides high-throughput auxiliary postprocessing functions for Quantum Espresso simulations, enabling efficient extraction and transformation of calculation results.

---

## Table of Contents

1. [Installation](#installation)
2. [Features](#features)
   - [1. Monitor Relaxation Status](#1-monitor-relaxation-status)
   - [2. Convert QE Output to CIF Format](#2-convert-qe-output-to-cif-format)
   - [3. Process PDOS Results](#3-process-pdos-results)
   - [4. Process Band Structure Results](#4-process-band-structure-results)
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

### 1. Monitor Relaxation Status <a name="1-monitor-relaxation-status"></a>

This function extracts and monitors the status of `vc-relax`, `relax`, `scf`, or `nscf` calculations from Quantum Espresso output files.

#### Arguments
- `QEfile_folder` (str): Folder containing Quantum Espresso calculation files.
- `name` (str): Name of the output file (e.g., `vc-relax.out`).
- `output_folder` (str): Path to save the status report.

#### Similar Functions
- `PostProcessing.relax_status`
- `PostProcessing.scf_status`
- `PostProcessing.nscf_status`

---

### 2. Convert QE Output to CIF Format <a name="2-convert-qe-output-to-cif-format"></a>

This function converts Quantum Espresso output files to `.cif` format, making them easier to analyze with structure visualization tools.

#### Arguments
- `calculation` (str): The type of calculation, e.g., `vc-relax` or `relax`.
- `QEfile_folder` (str): Folder containing Quantum Espresso calculation files.
- `filename` (str): Name of the output file (e.g., `vc-relax.out`).
- `output_folder` (str): Path to save the `.cif` files.

---

### 3. Process PDOS Results <a name="3-process-pdos-results"></a>

This function processes Projected Density of States (PDOS) results, with an option to adjust for Fermi level subtraction.

#### Arguments
- `QEfile_folder` (str): Folder containing Quantum Espresso calculation files.
- `output_folder` (str): Path to save the processed PDOS results.
- `Fermi_subtract` (bool): Whether to subtract the Fermi level.
- `Fermi_source` (str): Source of the Fermi level. Options: `vc-relax`, `relax`, `scf`, `nscf`.
- `filename` (str): Name of the output file (e.g., `scf.out`).

---

### 4. Process Band Structure Results <a name="4-process-band-structure-results"></a>

This function processes band structure results, with an option to adjust for Fermi level subtraction.

#### Arguments
- `QEfile_folder` (str): Folder containing Quantum Espresso calculation files.
- `result_prefix` (str): Prefix for the output file.
- `output_folder` (str): Path to save the processed band structure results.
- `Fermi_subtract` (bool): Whether to subtract the Fermi level.
- `Fermi_source` (str): Source of the Fermi level. Options: `vc-relax`, `relax`, `scf`, `nscf`.
- `filename` (str): Name of the output file (e.g., `scf.out`).

---

## Usage Examples <a name="usage-examples"></a>

### Example 1: Monitor Relaxation Status
```python
from QEflow import PostProcessing

QEfile_folder = "data3/calculation1"
name = 'vc-relax.out'
output_folder = 'data3/result'

PostProcessing.vcrelax_status(QEfile_folder, name, output_folder)
```

### Example 2: Convert QE Output to CIF Format
```python
from QEflow import PostProcessing

calculation = 'vc-relax'
QEfile_folder = 'data3/calculation1'
filename = 'vc-relax.out'
output_folder = 'data3/structures_vc_relaxed'

PostProcessing.qe_to_cif(calculation, QEfile_folder, filename, output_folder)
```

### Example 3: Process PDOS Results
```python
from QEflow import PostProcessing

QEfile_folder = "data3/calculation2"
output_folder = 'data3/result/pdos_processed'
Fermi_source = 'scf'
filename = 'scf.out'
Fermi_subtract = True

PostProcessing.pdos_process(QEfile_folder, output_folder, Fermi_source, filename, Fermi_subtract=True)
```

### Example 4: Process Band Structure Results
```python
from QEflow import PostProcessing

QEfile_folder = "data3/calculation2"
result_prefix = "QE_Flow"
output_folder = 'data3/result/band_processed'
Fermi_source = 'scf'
filename = 'scf.out'
Fermi_subtract = True

PostProcessing.band_process(QEfile_folder, result_prefix, output_folder, Fermi_source, filename, Fermi_subtract=True)
```

---

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests to improve this repository.

---

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.

---
