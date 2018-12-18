#! /usr/bin/env python

from QUBEKit.engines import PSI4, Gaussian, Chargemol
from QUBEKit.ligand import Ligand
from QUBEKit.dihedrals import TorsionScan
from QUBEKit.lennard_jones import LennardJones as LJ
from QUBEKit.modseminario import ModSeminario
from QUBEKit import smiles, decorators
from QUBEKit.helpers import get_mol_data_from_csv, generate_config_csv

import os
from subprocess import call as sub_call


# def gather_charges():
#     """Takes the TheoryTests files and extracts the net charge as a tuple with the molecule + functional
#     For example, opens the benzene_PBE0_001 folder, finds the charges file from DDEC6,
#     finds the net charge from the carbon atoms and finally returns them as:
#     {net charge, benzene_PBE0}
#
#     These charges can then be output to a graph."""
#
#     from operator import itemgetter
#
#     molecules = ['/benzene', '/methane', '/ethane', '/acetone', '/methanol']
#     charges_list = []
#
#     for root, dirs, files in os.walk('./TheoryTests'):
#         for file in files:
#             for i in range(len(molecules)):
#                 if molecules[i] in root:
#                     if file.startswith('DDEC6_even_tempered_net'):
#                         name = file
#                         # print(root + '/' + name)
#                         with open(root + '/' + name, 'r') as charge_file:
#                             net_charge = 0
#                             lines = charge_file.readlines()
#                             for count, line in enumerate(lines):
#                                 if line[0:2] == 'C ':
#                                     net_charge += float(line.split()[4])
#                             # Find average charge
#                             #         net_charge /= (count + 1)
#                         charges_list.append([molecules[i][1:], root.split('_')[-2], round(net_charge, 4)])
#                         # Sort list by molecule
#                         charges_list = sorted(charges_list, key=itemgetter(0))
#                         # Sort list by functional
#                         charges_list = sorted(charges_list, key=itemgetter(1))
#
#     return np.array(charges_list)
#
#
# def plot_charges(charges=gather_charges()):
#
#     import numpy as np
#     import matplotlib.pyplot as plt
#
#     N = 5
#     ind = np.arange(N)  # The x locations for the groups
#     width = 0.18  # The width of the bars
#
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#
#     # Segregate data according to molecule and functional
#     charges = [float(charge[2]) for charge in charges]
#     B3LYP = charges[0:5]
#     BB1K = charges[5:10]
#     PBE = charges[10:15]
#     wB97X_D = charges[15:20]
#
#     # Set group separation
#     rects1 = ax.bar(ind, B3LYP, width)
#     rects2 = ax.bar(ind + width, BB1K, width)
#     rects3 = ax.bar(ind + width * 2, PBE, width)
#     rects4 = ax.bar(ind + width * 3, wB97X_D, width)
#
#     plt.title('Net Charges Across Carbon Atoms')
#     ax.set_ylabel('Net Charges')
#     ax.set_xticks(ind + width)
#     ax.set_xticklabels(('Acetone', 'benzene', 'ethane', 'methane', 'methanol'))
#     ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('B3LYP', 'BB1K', 'PBE', 'wB97X-D'))
#
#     ax.yaxis.grid(which="both", linewidth=0.7)
#
#     plt.show()
#

file = 'methanol.pdb'
mol = Ligand(file)

test_dict = {'a': {'1': 1, '2': 2}, 'b': {'one': 'o', 'two': 't'}}

print(list(test_dict.keys()))