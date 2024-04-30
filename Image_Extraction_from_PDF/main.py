from spire.pdf import *
from spire.pdf.common import *
import math

# Create an object of PdfDocument class
pdf = PdfDocument()

# Load a PDF document
pdf.LoadFromFile("C:/Users/tejas/OneDrive/Desktop/Paper391.pdf")

# Create an object of PdfTrueTypeFont class
font = PdfTrueTypeFont("HarmonyOS Sans SC", 48.0, 0, True)

# Specify the watermark text
text = "TEJAS LAMKHADE"

# Calculate two offsets that are used to determine the position of the watermark text
offset1 = float(font.MeasureString(text).Width * math.sqrt(2) / 4)
offset2 = float(font.MeasureString(text).Height * math.sqrt(2) / 4)

# Loop through the pages in the document
for i in range(pdf.Pages.Count):
    # Get a page
    page = pdf.Pages.get_Item(i)

    # Set the transparency of the watermark
    page.Canvas.SetTransparency(0.8)

    # Translate the page coordinate system to the specified position
    page.Canvas.TranslateTransform(page.Canvas.Size.Width / 2 - offset1 - offset2,
                                   page.Canvas.Size.Height / 2 + offset1 - offset2)

    # Rotate the coordinate system 45 degrees counterclockwise
    page.Canvas.RotateTransform(-45.0)

    # Draw the watermark on the page
    page.Canvas.DrawString(text, font, PdfBrushes.get_Gray(), 0.0, 0.0)

# Specify the path to the output folder
output_folder = "C:/Users/tejas/OneDrive/Desktop/OutputFolder/"

# Specify the output file name
output_filename = "output.pdf"

# Save the document to the specified folder
pdf.SaveToFile(output_folder + output_filename)
pdf.Close()
