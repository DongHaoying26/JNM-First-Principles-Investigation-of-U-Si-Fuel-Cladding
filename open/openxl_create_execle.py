# -*- coding: utf-8 -*-
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Alignment, Font

# Create a new workbook
new_workbook = Workbook()

# Create Sheet1 and fill in data
sheet1 = new_workbook.active
sheet1.title = "Sheet1"

# Create Sheet2 and fill in mu, msi, mc data
sheet2 = new_workbook.create_sheet(title="Sheet2")
sheet2_data = [
    ['mu', 0.18, 0.05, 0.77, 10.29],
    ['msi', 0.62, 0.82, -0.27, -14.54],
    ['mc', -0.18, -0.37, 0.71, 14.99]
]

# Fill Sheet2 data and apply steel blue fill
steel_blue_fill = PatternFill(start_color="4682B4", end_color="4682B4", fill_type="solid")
for row in sheet2_data:
    sheet2.append(row)

for row in sheet2.iter_rows(min_row=1, max_row=3, min_col=1, max_col=5):
    for cell in row:
        cell.fill = steel_blue_fill

# Manually defined original data
sheet1_data_part1 = [
    ['Three-Phase-Equilibria'],
    ['Species', 'U3Si2-SiC-U3Si5', 'U3Si2-SiC-USi', 'U3Si2-SiC-U3Si2C2', 'U3Si2-SiC-U20Si16C3'],
    ['U1vac', 2.01],
    ['U2vac', 3.11],
    ['Sivac', 2.75],
    ['SionU1', 0.83],
    ['SionU2', 1.75],
    ['UonSi', 1.77],
    ['UINT1', 2.31],
    ['UINT2', 4.21],
    ['UINT3', 4.33],
    ['UINT4', 3.63],
    ['ConU1', 5.12],
    ['ConU2', 3.88],
    ['ConSi', 2.32],
    ['CINT1', -0.79],
    ['CINT2', 2.55],
    ['CINT3', 1.34],
    ['CINT4', 1.00],
    ['SiINT1', 0.32],
    ['SiINT2', 0.52],
    ['SiINT3', 3.26],
    ['SiINT4', 2.07],

]

# Define fill color
dark_sea_green_fill = PatternFill(start_color="8FBC8F", end_color="8FBC8F", fill_type="solid")

# Fill in the first part of data
for row in sheet1_data_part1:
    sheet1.append(row)

# Copy the first part of data to columns C3 to E23
for row in range(3, 25):
    value = sheet1.cell(row=row, column=2).value
    sheet1.cell(row=row, column=3, value=value)
    sheet1.cell(row=row, column=4, value=value)
    sheet1.cell(row=row, column=5, value=value)

# Fill in the second part of data and reference values from Sheet2, apply steel blue fill
second_part_headers = ['mu', 'msi', 'mc']
for i, header in enumerate(second_part_headers):
    for j in range(5):
        sheet1.cell(row=i + 24, column=j + 1, value=header if j == 0 else f"=Sheet2!{chr(65+j)}{i+1}")
        sheet1.cell(row=i + 24, column=j + 1).fill = steel_blue_fill

# Initialize calculation results list
calculation_results = []

# Fill in calculation formulas and compute results
for i, row in enumerate(sheet1_data_part1[2:]):
    input_name = row[0]  # Get input data name
    input_value = row[1]

    # Initialize result variables
    results = []

    # Adjust calculation formulas as needed
    for j in range(4):  # Adjust to 4 to cover all Sheet2 data
        mu_value_col = chr(66 + j)
        msi_value_col = chr(66 + j)
        mc_value_col = chr(66 + j)
        mu_value = f"Sheet2!{mu_value_col}1"
        msi_value = f"Sheet2!{msi_value_col}2"
        mc_value = f"Sheet2!{mc_value_col}3"

        formula = None

        if input_name ==   'U1vac':
            formula = f"={input_value} - {mu_value}"
        elif input_name == 'U2vac':
            formula = f"={input_value} - {mu_value}"
        elif input_name == 'Sivac':
            formula = f"={input_value} - {msi_value}"
        elif input_name == 'SionU1':
            formula = f"={input_value} + {msi_value} - {mu_value}"
        elif input_name == 'SionU2':
            formula = f"={input_value} + {msi_value} - {mu_value}"
        elif input_name == 'UonSi':
            formula = f"={input_value} - {msi_value} + {mu_value}"
        elif input_name == 'UINT1':
            formula = f"={input_value} + {mu_value}"
        elif input_name == 'UINT2':
            formula = f"={input_value} + {mu_value}"
        elif input_name == 'UINT3':
            formula = f"={input_value} + {mu_value}"
        elif input_name == 'UINT4':
            formula = f"={input_value} + {mu_value}"
        elif input_name == 'ConU1':
            formula = f"={input_value} + {mc_value} - {mu_value}"
        elif input_name == 'ConU2':
            formula = f"={input_value} + {mc_value} - {mu_value}"
        elif input_name == 'ConSi':
            formula = f"={input_value} - {msi_value} + {mc_value}"
        elif input_name == 'CINT1':
            formula = f"={input_value} + {mc_value}"
        elif input_name == 'CINT2':
            formula = f"={input_value} + {mc_value}"
        elif input_name == 'CINT3':
            formula = f"={input_value} + {mc_value}"
        elif input_name == 'CINT4':
            formula = f"={input_value} + {mc_value}"
        elif input_name == 'SiINT1':
            formula = f"={input_value} + {msi_value}"
        elif input_name == 'SiINT2':
            formula = f"={input_value} + {msi_value}"
        elif input_name == 'SiINT3':
            formula = f"={input_value} + {msi_value}"
        elif input_name == 'SiINT4':
            formula = f"={input_value} + {msi_value}"


        results.append(formula)

    # Create calculation result row
    formula_row = [input_name] + results

    # Add to calculation results list
    calculation_results.append(formula_row)

# Write calculation results to the third part of the table in the same column, apply dark sea green fill
start_row = 27  # Calculation results start row
for i, row in enumerate(calculation_results):
    for j in range(5):
        cell = sheet1.cell(row=start_row + i, column=j + 1, value=row[j])
        cell.fill = dark_sea_green_fill
        cell.alignment = Alignment(horizontal='center', vertical='center')

# Center align all cell contents
for row in sheet1.iter_rows():
    for cell in row:
        cell.alignment = Alignment(horizontal='center', vertical='center')

# Create Sheet3 and fill in data
sheet3 = new_workbook.create_sheet(title="Sheet3")

# First part of data
sheet3_data_part1 = [
    ['Data Statistics'],
    ['E0', -661.408],
    ['U1vac', -650.060],
    ['U2vac', -648.953],
    ['Sivac', -653.234],
    ['SionU1', -656.660],
    ['SionU2', -655.744],
    ['UonSi', -663.656],
    ['UINT1', -668.438],
    ['UINT2', -666.543],
    ['UINT3', -666.419],
    ['UINT4', -667.119],
    ['ConU1', -656.180],
    ['ConU2', -657.418],
    ['ConSi', -662.888],
    ['CINT1', -671.430],
    ['CINT2', -668.087],
    ['CINT3', -669.298],
    ['CINT4', -669.641],
    ['SiINT1', -666.511],
    ['SiINT2', -666.314],
    ['SiINT3', -663.569],
    ['SiINT4', -664.764],
]

# Fill in the first part of data
for row in sheet3_data_part1:
    sheet3.append(row)

# Second part of data
sheet3_data_part2 = [
    ['Mu', 9.3408],
    ['Msi', 5.424],
    ['Mc', 9.228]
]

# Fill in the second part of data and apply cornflower blue fill
cornflower_blue_fill = PatternFill(start_color="6495ED", end_color="6495ED", fill_type="solid")
for row in sheet3_data_part2:
    sheet3.append(row)

for row in sheet3.iter_rows(min_row=24, max_row=26, min_col=1, max_col=2):
    for cell in row:
        cell.fill = cornflower_blue_fill

# Initialize calculation results list
calculation_results_sheet3 = []

# Fill in calculation formulas and compute results
for i, row in enumerate(sheet3_data_part1[2:]):
    input_name = row[0]  # Get input data name
    input_value = row[1]

    # Initialize result variables
    results = []

    # Adjust calculation formulas as needed
    for j in range(2):  # Adjust to 2 to cover all Sheet3 second part data
        mu_value_col = chr(66 + j)
        msi_value_col = chr(66 + j)
        mc_value_col = chr(66 + j)
        m0_value_col = chr(66 + j)
        mu_value = f"Sheet3!{mu_value_col}24"
        msi_value = f"Sheet3!{msi_value_col}25"
        mc_value = f"Sheet3!{mc_value_col}26"
        m0_value = f"Sheet3!{mc_value_col}2"

        formula = None

        if input_name == 'U1vac':
            formula = f"={input_value} - {mu_value} - {m0_value}"
        elif input_name == 'U2vac':
            formula = f"={input_value} - {mu_value} - {m0_value}"
        elif input_name == 'Sivac':
            formula = f"={input_value} - {msi_value} - {m0_value}"
        elif input_name == 'SionU1':
            formula = f"={input_value} + {msi_value} - {mu_value} - {m0_value}"
        elif input_name == 'SionU2':
            formula = f"={input_value} + {msi_value} - {mu_value} - {m0_value}"
        elif input_name == 'UonSi':
            formula = f"={input_value} - {msi_value} + {mu_value} - {m0_value}"
        elif input_name == 'UINT1':
            formula = f"={input_value} + {mu_value} - {m0_value}"
        elif input_name == 'UINT2':
            formula = f"={input_value} + {mu_value} - {m0_value}"
        elif input_name == 'UINT3':
            formula = f"={input_value} + {mu_value} - {m0_value}"
        elif input_name == 'UINT4':
            formula = f"={input_value} + {mu_value} - {m0_value}"
        elif input_name == 'ConU1':
            formula = f"={input_value} + {mc_value} - {mu_value} - {m0_value}"
        elif input_name == 'ConU2':
            formula = f"={input_value} + {mc_value} - {mu_value} - {m0_value}"
        elif input_name == 'ConSi':
            formula = f"={input_value} - {msi_value} + {mc_value} - {m0_value}"
        elif input_name == 'CINT1':
            formula = f"={input_value} + {mc_value} - {m0_value}"
        elif input_name == 'CINT2':
            formula = f"={input_value} + {mc_value} - {m0_value}"
        elif input_name == 'CINT3':
            formula = f"={input_value} + {mc_value} - {m0_value}"
        elif input_name == 'CINT4':
            formula = f"={input_value} + {mc_value} - {m0_value}"
        elif input_name == 'SiINT1':
            formula = f"={input_value} + {msi_value} - {m0_value}"
        elif input_name == 'SiINT2':
            formula = f"={input_value} + {msi_value} - {m0_value}"
        elif input_name == 'SiINT3':
            formula = f"={input_value} + {msi_value} - {m0_value}"
        elif input_name == 'SiINT4':
            formula = f"={input_value} + {msi_value} - {m0_value}"


        results.append(formula)

    # Create calculation result row
    formula_row = [input_name] + results

    # Add to calculation results list
    calculation_results_sheet3.append(formula_row)

# Write calculation results to the third part of the table in the same column, apply dark sea green fill
start_row = 27  # Calculation results start row
for i, row in enumerate(calculation_results_sheet3):
    for j in range(2):
        cell = sheet3.cell(row=start_row + i, column=j + 1, value=row[j])
        cell.fill = dark_sea_green_fill
        cell.alignment = Alignment(horizontal='center', vertical='center')

# Center align all cell contents
for row in sheet3.iter_rows():
    for cell in row:
        cell.alignment = Alignment(horizontal='center', vertical='center')

# Adjust column width to fit content
for col in sheet1.columns:
    max_length = 0
    column = col[0].column_letter  # Get column letter
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
    adjusted_width = (max_length + 2) * 1.2
    sheet1.column_dimensions[column].width = adjusted_width

for col in sheet3.columns:
    max_length = 0
    column = col[0].column_letter  # Get column letter
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
    adjusted_width = (max_length + 2) * 1.2
    sheet3.column_dimensions[column].width = adjusted_width

# Merge the first 5 columns of the first row in Sheet1
sheet1.merge_cells('A1:E1')
# Merge the first 2 columns of the first row in Sheet3
sheet3.merge_cells('A1:B1')

# Set format for merged cells
sheet1['A1'].font = Font(bold=True, size=sheet1['A1'].font.size + 5)
sheet3['A1'].font = Font(bold=True, size=sheet3['A1'].font.size + 5)

# Save the new workbook
new_file_path = '1finalu3si2c2_sic.xlsx'
new_workbook.save(new_file_path)

print(f"New workbook created and saved as {new_file_path}")
