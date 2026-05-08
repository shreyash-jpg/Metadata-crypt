from PIL import Image
import piexif

def sanitize_metadata(file_path):
    try:
        if file_path.endswith(('.jpg', '.jpeg')):
            piexif.remove(file_path)
            print("Metadata stripped from image.")
        elif file_path.endswith('.png'):
            img = Image.open(file_path)
            img.save(file_path)
            print("PNG image saved without metadata.")
        else:
            print("Sanitization not implemented for this file type.")
    except Exception as e:
        print("Sanitization failed:", e)