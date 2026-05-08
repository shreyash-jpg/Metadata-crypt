import piexif, PyPDF2, docx
from PIL import Image

def extract_metadata(file_path):
    try:
        if file_path.endswith(('.jpg', '.jpeg', '.png')):
            img = Image.open(file_path)
            exif_data = img._getexif()
            print("\nImage Metadata:", exif_data)

        elif file_path.endswith('.pdf'):
            reader = PyPDF2.PdfReader(file_path)
            print("\nPDF Metadata:", reader.metadata)

        elif file_path.endswith('.docx'):
            doc = docx.Document(file_path)
            props = doc.core_properties
            print("\nDOCX Metadata:", vars(props))
        else:
            print("\nUnsupported file format.")
    except Exception as e:
        print("Error extracting metadata:", e)