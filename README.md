# QEflow Introduction
**QEflow** was developed by Dr. Jiahao Wu from the University of Chinese Academy of Sciences as a high-throughput Python toolkit for the Quantum ESPRESSO (QE) density functional theory (DFT) software. It is built on open-source libraries such as **pymatgen**, **numpy**, **pandas** and **scipy** .
It features modules for modeling, parameter testing files preparation, atom fixing, generation of input files for calculations, and post-processing. Its modular architecture enables researchers to streamline preprocessing and postprocessing tasks with simple commands, eliminating the need for tedious and time-consuming manual preparation of input files and parsing of output files. 
With ongoing updates, the developers of QEflow aim to further expand its functionality,  facilitating the broader application of Quantum ESPRESSO. This will ultimately accelerate progress in fields that rely on high-throughput calculations, such as the construction of machine learning datasets.



# QEflow Installation Guide

This guide explains how to install the QEflow package.

## Installation Steps

Follow the steps below to install QE_Flow:

1. Extract the package:
   ```bash
   tar -xvzf QEflow-1.0.tar.gz
   ```

2. Change to the extracted directory:
   ```bash
   cd QEflow-1.0
   ```

3. Install the package:
   ```bash
   pip install . --no-binary :all:
   ```
    or
   ```bash
   python setup.py install
   ```

## Requirements

- **Python version**: Ensure you have Python 3.x installed.
- **Dependencies**: Any dependencies required by the package will be automatically installed during the setup process. If not, refer to the `requirements.txt` file and install them manually:
   ```bash
   pip install -r requirements.txt
   ```


## Verifying Installation

Once the installation is complete, you can verify it by running:
```bash
python -c "import QEflow; print('QEflow installed successfully!')"
```

If the installation is successful, you should see the message:
```
QEflow installed successfully!
```


## Uninstallation

To uninstall QEflow, you can use the following command:
```bash
pip uninstall QEflow
```


## Support

If you encounter any issues during installation, please refer to the repository documentation or open an issue in the repository.

---
