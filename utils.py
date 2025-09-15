import numpy as np
try:
    from rdkit import Chem
    from rdkit.Chem import (
        Descriptors, rdMolDescriptors, Lipinski, Crippen,
        rdFingerprintGenerator, DataStructs, Draw, rdDepictor, MACCSkeys
    )
    from rdkit.Chem.Draw import rdMolDraw2D
    from rdkit.Avalon import pyAvalonTools
    RDKIT_AVAILABLE = True
except ImportError:
    print("RDKit not available. Please install: pip install rdkit")
    RDKIT_AVAILABLE = False

_MORGAN4 = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048)

def props_and_fps_from_smiles(smiles: str, idx: int):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return {"molecule_id": idx, "smiles": smiles, "valid": False}, {"ECFP4": None, "AVALON": None}

    props = {
        "molecule_id": idx,
        "smiles": smiles,
        "mw": Descriptors.MolWt(mol),
        "logp": Descriptors.MolLogP(mol),
        "valid": True,
    }

    # ECFP4
    bv = _MORGAN4.GetFingerprint(mol)
    arr1 = np.zeros(2048, dtype=np.int8)
    DataStructs.ConvertToNumpyArray(bv, arr1)

    # Avalon
    bv = pyAvalonTools.GetAvalonFP(mol, nBits=2048)
    arr2 = np.zeros(2048, dtype=np.int8)
    DataStructs.ConvertToNumpyArray(bv, arr2)

    return props, {"ECFP4": arr1, "AVALON": arr2}
