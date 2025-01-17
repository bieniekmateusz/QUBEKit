import pytest

from qubekit.molecules import Ligand, TorsionDriveData
from qubekit.nonbonded import VirtualSites
from qubekit.parametrisation import XML, AnteChamber, OpenFF
from qubekit.utils.file_handling import get_data
from qubekit.workflow.workflow import QCOptions, WorkFlow


@pytest.fixture()
def acetone():
    """
    Make a ligand class from the acetone pdb.
    """
    return Ligand.from_file(file_name=get_data("acetone.sdf"))


@pytest.fixture()
def water():
    """Make a qube water molecule."""
    w = Ligand.from_file(file_name=get_data("water.pdb"))
    w.name = "water"
    return w


@pytest.fixture()
def antechamber():
    return AnteChamber(force_field="gaff2")


@pytest.fixture()
def openff():
    return OpenFF(force_field="openff_unconstrained-2.0.0.offxml")


@pytest.fixture()
def xml():
    return XML()


@pytest.fixture()
def coumarin():
    return Ligand.parse_file(get_data("coumarin_hess_wbo.json"))


@pytest.fixture()
def coumarin_with_rb():
    return Ligand.parse_file(get_data("coumarin_with_rb.json"))


@pytest.fixture()
def mol_47():
    return Ligand.from_smiles("CC(C)(O)CCC(C)(C)O", "mol_47")


@pytest.fixture()
def rdkit_workflow():
    rdkit_spec = QCOptions(program="rdkit", method="uff", basis=None)
    workflow = WorkFlow(qc_options=rdkit_spec)
    return workflow


@pytest.fixture()
def rfree_data():
    return {
        "H": {"v_free": 7.6, "b_free": 6.5, "r_free": 1.738},
        "X": {"v_free": 7.6, "b_free": 6.5, "r_free": 1.083},
        "C": {"v_free": 34.4, "b_free": 46.6, "r_free": 2.008},
        "N": {"v_free": 25.9, "b_free": 24.2, "r_free": 1.765},
        "O": {"v_free": 22.1, "b_free": 15.6, "r_free": 1.499},
        "F": {"v_free": 18.2, "b_free": 9.5, "r_free": 1.58},
        "Cl": {"v_free": 65.1, "b_free": 94.6, "r_free": 1.88},
        "Br": {"v_free": 95.7, "b_free": 162.0, "r_free": 1.96},
        "S": {"v_free": 75.2, "b_free": 134.0, "r_free": 2.0},
        "alpha": 1,
        "beta": 0.5,
    }


@pytest.fixture()
def methanol():
    return Ligand.parse_file(get_data("methanol.json"))


@pytest.fixture()
def bace_fragmented():
    # ie CN1C(=O)C(c2cccc(-c3cccnc3)c2)(C2CC2)[NH+]=C1N
    """
    Load the freshly fragmented BACE molecule with the fragments before deduplication
    """
    return Ligand.parse_file(get_data("bace17d_with_fragments.json"))


@pytest.fixture()
def symmetry_fragments():
    """The raw result of fragmenting a symmetric molecule CCC(C)CC"""
    return Ligand.parse_file(get_data("symmetry_fragments.json"))


@pytest.fixture()
def vs():
    """
    Initialise the VirtualSites class to be used for the following tests
    """
    virtual_sites = VirtualSites()
    return virtual_sites


@pytest.fixture()
def ethanol():
    return Ligand.parse_file(get_data("ethanol_sites.json"))


@pytest.fixture()
def biphenyl_fragments():
    return Ligand.parse_file(get_data("ring_test.json"))


@pytest.fixture()
def biphenyl():
    """
    Load up a biphenyl molecule with some torsiondrive data.
    """
    mol = Ligand.from_file(file_name=get_data("biphenyl.sdf"))
    # load the torsiondrive data
    td_data = TorsionDriveData.from_qdata(
        qdata_file=get_data("biphenyl_qdata.txt"), dihedral=(6, 10, 11, 8)
    )
    mol.add_qm_scan(scan_data=td_data)
    return mol
