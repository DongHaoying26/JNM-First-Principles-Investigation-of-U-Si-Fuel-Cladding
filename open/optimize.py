# -*- coding: utf-8 -*-

import os
import re

def extract_energy(outcar_file):
    # Use errors='ignore' to prevent encoding errors due to special characters
    with open(outcar_file, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    # Find lines matching the energy pattern
    energy_lines = [line for line in lines if 'energy(sigma->0)' in line and not line.strip().startswith('#')]

    if energy_lines:
        # Get the last matching line
        last_energy_line = energy_lines[-1]

        # Extract the energy value from the line
        energy_match = re.search(r'energy\(sigma->0\) =\s+(-?\d+\.\d+)', last_energy_line)

        if energy_match:
            energy = float(energy_match.group(1))
            return energy
    return None

if __name__ == "__main__":
    directory = "."  # Current directory
    extracted_data = []

    # Traverse folders in the current directory
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            outcar_path = os.path.join(folder_path, 'OUTCAR')
            if os.path.exists(outcar_path):
                energy = extract_energy(outcar_path)
                if energy is not None:
                    extracted_data.append((folder, energy))

    if extracted_data:
        # Sort by folder name (comment out the next line if sorting is not desired)
        extracted_data.sort(key=lambda x: x[0])

        # Write extracted data to file: first column is folder name, second column is energy value
        with open('extracted_energies.txt', 'w', encoding='utf-8') as f:
            for folder_name, energy in extracted_data:
                f.write(f"{folder_name}\t{energy:.8f}\n")
                
        print("Extraction completed! Data saved to extracted_energies.txt")
    else:
        print("No energy data found or unable to parse energy values.")
