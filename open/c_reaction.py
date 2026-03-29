# -*- coding: utf-8 -*-
# Formation enthalpy data, corrected. Replace with your actual data.
enthalpy_data = {
    'phase1': formation energy,   # eV/atom
    'phase2': formation energy,   # eV/atom
    'phase3': formation energy,   # eV/atom
    'phase4': formation energy,   # eV/atom
    'phase5': formation energy,   # eV/atom
    'phase6': formation energy,   # eV/atom

    # Add more data
}

def atoms_count(material):
    # Define a dictionary storing the number of atoms for each material(How many atoms are in this phase)
    atomic_numbers = {
        'phase1': atomic number,
        'phase2': atomic number,
        'phase3': atomic number,
        'phase4': atomic number,
        'phase5': atomic number,
        'phase6': atomic number,
     
        # Add number of atoms for more materials
    }
    return atomic_numbers.get(material, 1)  # Default to 1 atom if not found

# All possible reactions£¨use this format and add it blow£©
example_reactions = [
    ([('phase1', 1), ('phase2', 1)], [('phase3', 1), ('phase5', 1)]),
    ([('phase1', 1), ('phase2', 3)], [('phase3', 5), ('phase4', 3)]),
    ([('phase1', 2), ('phase2', 7)], [('phase5', 3), ('phase6', 5)]),

   ]

# Calculate x value and ¦¤H_r for each reaction
def calculate_x_and_dH(reactants, products):
    total_atoms_reactants = sum([coeff for _, coeff in reactants])
    total_atoms_products = sum([coeff for _, coeff in products])
    total_reactants = sum([coeff * atoms_count(reactant) for reactant, coeff in reactants])

    x = sum([coeff for reactant, coeff in reactants if reactant == 'phase1']) / total_atoms_reactants

    dH_reactants = sum([enthalpy_data[reactant] * coeff * atoms_count(reactant) for reactant, coeff in reactants])
    dH_products = sum([enthalpy_data[product] * coeff * atoms_count(product) for product, coeff in products])

    dH_r = (1 / total_reactants) * (dH_products - dH_reactants)

    return x, dH_r

# Open a file to write the output
with open("output_equation.txt", "w") as f:  # Automatically creates or overwrites output_equation.txt
    for reactants, products in example_reactions:
        x, dH_r = calculate_x_and_dH(reactants, products)
        output_line = f"Reactants: {reactants}, Products: {products}, x: {x:.4f}, dH_r: {dH_r:.4f} eV/atom\n"
        f.write(output_line)
        print(output_line)  # Also print to console