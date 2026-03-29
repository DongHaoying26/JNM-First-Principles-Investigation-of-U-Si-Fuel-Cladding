All files in this folder contain the relevant data and scripts for the paper titled "First-Principles Investigation of U₃Si₂ Fuel/Cladding Interfacial Compatibility: Unveiling Thermodynamic Driving Forces and Kinetic Pathways."

Please cite the following link when using the data and scripts from this work:

The two sets of data are provided in .csv format.

•   # The "vasp_read_data.py" script can be used for batch data extraction from VASP calculations. Place the script outside the target folder to run. It will automatically generate the output containing the read numerical values.

1.  The "U-X-Si" spreadsheet contains all the formation energy data after our screening and correction process.
    ◦   (1) This data can be input into the "c_reaction.py" file to calculate the reaction formation enthalpy (ΔHr) for reaction screening.

        # The script includes functions for determining reaction elements, atomic counts, and calculating ΔHr. It uses manual input and is transferable to similar work.

    ◦   (2) The "convex_hull.py" script can be used to plot the convex hull for the reactions.

        # This script requires input of the ΔHr values calculated by the previous script to generate the convex hull plot for reaction screening.

        # This method can also be applied to other tasks, such as plotting convex hulls for material formation energies.

2.  The "C defect data" spreadsheet contains the total energy and defect formation energy data for all thermodynamic processes in this paper.
    ◦   The data can be processed using the "openxl_create_excel.py" file.

        # Data must be entered manually into this script. Note that the reaction Δμ must be pre-calculated.

        # Running the script generates a spreadsheet of reaction defect driving force data in .xlsx format.

        # If adapting for other work, modifications and definitions of the reaction equations are also necessary.
