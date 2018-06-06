from .. import *
from ..utils import file_path
import numpy as np

# path for test_atom_list
pth = file_path('test_atom_list.txt', 'tests/test_files')


def test_order_atoms():
    # list of atoms
    atoms = order_atoms(pth)
    assert sum(line.isspace() for line in atoms) == 0, 'order_atoms function failed to eliminate whitespace'
    actual_length = len(atoms)
    assert len(atoms) == 47, 'molecule should have 47 atoms,' + str(actual_length) + ' was counted'
    return True



def test_add_atoms():
    result = add_atoms(pth)
    assert type(result) == Chem.rdchem.RWMol
    return True


def test_build_molecule():
    bond_matrix1 = np.array([[2, 0, 'a'], [1, 1, 0], [0, 2, 1]])
    bond_matrix2 = np.array([[1, 1, 0], [0, 2, 1]])
    bond_matrix3 = np.array([[1, 0, 1.2], [0, 2, 0], [0, 0, 1]])
    bond_matrix4 = np.array([[1, 0, 0], [0, 1, 0], [0, 2, 0]])
    mol = add_atoms(pth)
    # try string value
    try:
        build_molecule(bond_matrix1)
    except Exception as err:
        print(err)
    else:
        raise Exception('did not catch string input in bonding matrix')
    # try non-square matrix
    try:
        build_molecule(bond_matrix2)
    except Exception as err:
        print(err)
    else:
        raise Exception('did not catch non-square matrix')
    # try float value
    try:
        build_molecule(bond_matrix3)
    except Exception as err:
        print(err)
    else:
        raise Exception('did not catch float value not close to an integer')
    # try 0 value diagonal
    try:
        build_molecule(bond_matrix4)
    except Exception as err:
        print(err)
    else:
        for i in range(bonding_matrix.shape[0]):
            print(bonding_matrix[i, i])
    # raise Exception('did not catch diagonal value of 0')

    return True

