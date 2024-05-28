import pytesseract
from PIL import Image
import openpyxl
import string

# Path to the image file
image_path = '/home/rajashekar/Downloads/WhatsApp Image 2024-04-18 at 12.21.47 PM.jpeg'

# Path to the output Excel file
excel_file = 'output.xlsx'

# Perform OCR on the image
text = pytesseract.image_to_string(Image.open(image_path))

# Filter out non-printable characters
printable = set(string.printable)
text = ''.join(filter(lambda x: x in printable, text))
print(text)


# # Create a new Excel workbook
# wb = openpyxl.Workbook()
# ws = wb.active
#
# # Split the text into lines and write it to Excel
# lines = text.split('\n')
# for row_idx, line in enumerate(lines, start=1):
#     ws.cell(row=row_idx, column=1).value = line
#
# # Save the Excel workbook
# wb.save(excel_file)
#
# print("Excel file saved successfully!")
