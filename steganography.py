from PIL import Image

def hide_metadata(file_path, secret):
    img = Image.open(file_path)
    binary_secret = ''.join(format(ord(c), '08b') for c in secret)
    pixels = img.getdata()
    new_pixels = []
    i = 0

    for pixel in pixels:
        new_pixel = list(pixel)
        for n in range(len(pixel)):
            if i < len(binary_secret):
                new_pixel[n] = pixel[n] & ~1 | int(binary_secret[i])
                i += 1
        new_pixels.append(tuple(new_pixel))

    img.putdata(new_pixels)
    img.save(file_path.replace('.', '_steg.'))
    print("Metadata hidden in image.")


def reveal_metadata(file_path, key=None):
    img = Image.open(file_path)
    pixels = img.getdata()
    binary_data = ""

    for pixel in pixels:
        for n in pixel:
            binary_data += str(n & 1)
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded = ''.join(chr(int(b, 2)) for b in chars if int(b, 2) != 0)
    print("Hidden Metadata Revealed:", decoded)