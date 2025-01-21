# Image Steganography using Python

This project implements image steganography by embedding a secret message into the least significant bits (LSB) of an image's pixel values and later extracting it.

## Features
- **Encoding:** Embeds a text message into an image.
- **Decoding:** Extracts the hidden message from the encoded image.
- **Delimiter:** Ensures message extraction stops at the correct point.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Pillow (PIL fork) for image processing

Install dependencies using:
```bash
pip install Pillow
```

## Usage

### Encoding a message into an image
1. Place your input image in the project directory.
2. Modify the message in the code if needed.
3. Run the encoding script:
    ```bash
    python encodenew.py
    ```
4. The output image with the embedded message will be saved as `output_image.png`.

### Decoding a message from an image
1. Ensure `output_image.png` is available in the project directory.
2. Run the decoding script:
    ```bash
    python decodenew.py
    ```
3. The extracted message will be displayed in the terminal.

## Code Explanation

### Encoding Process
1. Convert the message to binary and append a delimiter.
2. Embed each bit into the least significant bit (LSB) of the red channel of each pixel.
3. Save the modified image.

### Decoding Process
1. Extract LSB values from the red channel of pixels.
2. Stop when the delimiter (`00000000`) is detected.
3. Convert binary data back to readable text.

## Example
Example message encoded: `Hello good morning!`

Output:
```
Decoded message is: Hello good morning!
```
## Author
[Aashna Suman](https://github.com/yourgithubprofile)
