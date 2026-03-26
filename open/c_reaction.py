# -*- coding: utf-8 -*-
# Formation enthalpy data, corrected. Replace with your actual data.
enthalpy_data = {
    'U3Si2': -0.3941,   # eV/atom
    'Cr': 0.0,     # eV/atom
    'U': 0.0,        # eV/atom
    'CrSi': -0.3352,     # eV/atom
    'CrSi2': -0.2825,     # eV/atom
    'Cr3Si': -0.3543,     # eV/atom
    'Cr5Si3': -0.3161,     # eV/atom
    'USi': -0.4500,     # eV/atom
    'U3Si': -0.2357,     # eV/atom
    'U3Si5': -0.4778,     # eV/atom
    'UCr3': 0.0454,     # eV/atom
    'U2Cr3Si': -0.2318,      # eV/atom
    'UCr2Si2': -1.0658,        # eV/atom
    # Add more data
}

def atoms_count(material):
    # Define a dictionary storing the number of atoms for each material
    atomic_numbers = {
        'U3Si2': 5,
        'Cr': 1,
        'U': 1,
        'CrSi': 2,
        'CrSi2': 3,
        'Cr3Si': 4,
        'Cr5Si3': 8,
        'USi': 2,
        'U3Si': 4,
        'U3Si5': 8,
        'UCr3': 4,
        'U2Cr3Si': 6,
        'UCr2Si2': 5,
        # Add number of atoms for more materials
    }
    return atomic_numbers.get(material, 1)  # Default to 1 atom if not found

# All possible reactions
example_reactions = [
    ([('U3Si2', 1), ('Cr', 1)], [('U3Si', 1), ('CrSi', 1)]),
    ([('U3Si2', 2), ('Cr', 1)], [('U3Si', 2), ('CrSi2', 1)]),
    ([('U3Si2', 1), ('Cr', 3)], [('U3Si', 1), ('Cr3Si', 1)]),
    ([('U3Si2', 3), ('Cr', 5)], [('U3Si', 3), ('Cr5Si3', 1)]),
    ([('U3Si2', 5), ('Cr', 6)], [('UCr2Si2', 3), ('U3Si', 4)]),
    ([('U3Si2', 1), ('Cr', 2)], [('UCr2Si2', 1), ('U', 2)]),
    ([('U3Si2', 1), ('Cr', 8)], [('UCr2Si2', 1), ('UCr3', 2)]),
    ([('U3Si2', 7), ('Cr', 27)], [('U2Cr3Si', 9), ('U3Si5', 1)]),
    ([('U3Si2', 1), ('Cr', 3)], [('U2Cr3Si', 1), ('USi', 1)]),
    ([('U3Si2', 2), ('Cr', 10)], [('U2Cr3Si', 3), ('CrSi', 1)]),
    ([('U3Si2', 4), ('Cr', 19)], [('U2Cr3Si', 6), ('CrSi2', 1)]),
    ([('U3Si2', 2), ('Cr', 12)], [('U2Cr3Si', 3), ('Cr3Si', 1)]),
    ([('U3Si2', 3), ('Cr', 14)], [('U2Cr3Si', 4), ('UCr2Si2', 1)]),
    ([('U3Si2', 6), ('Cr', 32)], [('U2Cr3Si', 9), ('Cr5Si3', 1)])
]

# Calculate x value and ¦¤H_r for each reaction
def calculate_x_and_dH(reactants, products):
    total_atoms_reactants = sum([coeff for _, coeff in reactants])
    total_atoms_products = sum([coeff for _, coeff in products])
    total_reactants = sum([coeff * atoms_count(reactant) for reactant, coeff in reactants])

    x = sum([coeff for reactant, coeff in reactants if reactant == 'U3Si2']) / total_atoms_reactants

    dH_reactants = sum([enthalpy_data[reactant] * coeff * atoms_count(reactant) for reactant, coeff in reactants])
    dH_products = sum([enthalpy_data[product] * coeff * atoms_count(product) for product, coeff in products])

    dH_r = (1 / total_reactants) * (dH_products - dH_reactants)

    return x, dH_r

# Open a file to write the output
with open("output_jc.txt", "w") as f:  # Automatically creates or overwrites output_jc.txt
    for reactants, products in example_reactions:
        x, dH_r = calculate_x_and_dH(reactants, products)
        output_line = f"Reactants: {reactants}, Products: {products}, x: {x:.4f}, dH_r: {dH_r:.4f} eV/atom\n"
        f.write(output_line)
        print(output_line)  # Also print to console