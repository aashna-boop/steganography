from PIL import Image

# Convert message to binary
msg = "Hello good morning!"
binary_msg = "".join(format(ord(char), '08b') for char in msg) + '00000000'  # Add delimiter
print("Binary message:", binary_msg)

# Image pixel data
path = "hummingbird.jpg"
img = Image.open(path)
pix = img.load()
print("Image loaded")

# Initialize bit generator
def msg_bits(binary_msg):
    for bit in binary_msg:
        yield int(bit)

bit_gen = msg_bits(binary_msg)

# Embedding binary message to LSB of pixels in the image
break_outer = False
for i in range(img.height):
    for j in range(img.width):
        try:
            r, g, b = pix[j, i]
            r = (r & 0xFE) | next(bit_gen)
            pix[j, i] = (r, g, b)
        except StopIteration:
            break_outer = True
            break
    if break_outer:
        break

# Save the modified image
output_path = "output_image.png"
img.save(output_path)
print(f"Message embedded successfully into {output_path}!")

# Open encoded image
img = Image.open(output_path)
pix = img.load()

# Get image dimensions
width, height = img.size
print(f"Image dimensions: {width}x{height} pixels")

# Decoding
binary_msg = ""
for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        binary_msg += str(r & 1)
        if binary_msg[-8:] == '00000000':
            binary_msg = binary_msg[:-8]
            break
    else:
        continue
    break

print("Hidden message extracted in bits:", binary_msg[:64])

# Convert binary to ASCII
msg_bits = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
msg = [chr(int(bit, 2)) for bit in msg_bits]

# Convert to string
decoded_msg = "".join(msg)
print("Decoded message is:", decoded_msg)
