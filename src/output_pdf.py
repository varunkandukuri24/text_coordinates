import fitz

# Load the PDF

input_pdf_path = "./assets/b2form.pdf"
output_pdf_path = "./assets/output.pdf"

pdf_document = fitz.open(input_pdf_path)

# Fill the form fields with the provided data
first_name = "Varun"
last_name = "Kandukuri"

# Assuming the first page contains the form
page = pdf_document[0]

# Coordinates for "Family Name (Last Name)" and "Given Name (First Name)"
last_name_rect = fitz.Rect(134, 392, 304, 404)  # Example coordinates
first_name_rect = fitz.Rect(134, 368, 304, 381)  # Example coordinates

# Insert text into the specified rectangles
page.insert_textbox(last_name_rect, last_name, fontsize=12, color=(0, 0, 0))
page.insert_textbox(first_name_rect, first_name, fontsize=12, color=(0, 0, 0))

# Save the modified PDF to a new file
pdf_document.save(output_pdf_path)
pdf_document.close()

output_pdf_path