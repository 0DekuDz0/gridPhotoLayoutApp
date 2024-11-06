from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
import sys
import os


padding = 1
CM_TO_POINTS = 72 / 2.54  # Convert cm to points

layoutList = [
    {"name": "Layout 1", "image": {"width": 27, "height": 18.5 }},
    {"name": "Layout 2", "image": {"width": 11.85, "height": 17}},
    {"name": "Layout 3", "image": {"width": 5.5, "height": 5.5}},
    {"name": "Layout 4", "image": {"width": 12.85, "height": 8.47}},
    {"name": "Layout 6", "image": {"width": 8.54, "height": 8}},
    {"name": "Layout 8", "image": {"width": 6.4, "height": 8.5}},
    {"name": "Layout 9", "image": {"width": 8.6, "height": 5.6}}
]

def draw_image(layout_name,titles,file_paths):
    layout = next((layout for layout in layoutList if layout["name"] == layout_name), None)
    
    # If layout is None, print an error message and exit the function
    if layout is None:
        print(f"Error: Layout '{layout_name}' not found in layoutList.")
        return    
    pdf_file_path = f"{titles[0]}.pdf"
    pdf_canvas = canvas.Canvas(pdf_file_path, pagesize=landscape(A4))
    pdf_canvas.setFont("Helvetica", 24)

    page_width, page_height = landscape(A4)  # Get dimensions of landscape A4 page
    y = padding * CM_TO_POINTS  # Initial y position (top margin)
    i=0
    while y + layout["image"]["height"] * CM_TO_POINTS < page_height:
        x = padding * CM_TO_POINTS  # Initial x position (left margin)
        while x + layout["image"]["width"] * CM_TO_POINTS < page_width:
            # Draw the image
            pdf_canvas.drawImage(file_paths[i], x, y, 
                                 layout["image"]["width"] * CM_TO_POINTS, 
                                 layout["image"]["height"] * CM_TO_POINTS)
            i+=1
            # Move to the next position in the row
            x += layout["image"]["width"] * CM_TO_POINTS + padding * CM_TO_POINTS
            
            # Print the coordinates for debugging
            print("x:", x / CM_TO_POINTS, "y:", y / CM_TO_POINTS)

        # Move down to the next row
        y += layout["image"]["height"] * CM_TO_POINTS + padding * CM_TO_POINTS
    
    # Patient and doctor names
    patient_name = titles[0]
    doctor_name = titles[1]

    # Font size for the names
    font_size = 12
    pdf_canvas.setFont("Helvetica", font_size)

    # Calculate positions for left and right alignment
    left_margin = padding * CM_TO_POINTS  # Left margin for patient name
    right_margin = page_width - pdf_canvas.stringWidth(doctor_name, "Helvetica", font_size) - padding * CM_TO_POINTS

    # Y position for names
    name_y_position = page_height - 1 * CM_TO_POINTS

    # Draw the patient name (left-aligned)
    pdf_canvas.drawString(left_margin, name_y_position, patient_name)

    # Draw the doctor name (right-aligned)
    pdf_canvas.drawString(right_margin, name_y_position, doctor_name)

    # Save the PDF

    pdf_canvas.save()
    open_powerpoint(pdf_file_path)

def open_powerpoint(pdf_file):
    # Define the command to open the PDF file in PowerPoint
    if sys.platform.startswith('win'):
        # Windows
        os.startfile(pdf_file)  # This will open the PDF file with the default PDF viewer
    elif sys.platform.startswith('darwin'):
        # macOS
        os.system(f'open "{pdf_file}"')  # This will open the PDF file with the default PDF viewer
    else:
        # Linux (this is an example, may need adjustment based on your environment)
        os.system(f'xdg-open "{pdf_file}"')  # This will open the PDF file with the default PDF viewer
    sys.exit()



