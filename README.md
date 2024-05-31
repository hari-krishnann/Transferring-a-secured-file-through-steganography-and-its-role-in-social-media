# Transferring a secured file through steganography

## 1. About the Project
This project demonstrates a simple implementation of image steganography using Python. Steganography is the technique of hiding secret data within an ordinary, non-secret file or message to avoid detection. In this case, we hide text messages within images using the least significant bit (LSB) method. The project serves as an educational resource for learning about steganography and its practical applications.

## 2. How to Run the Code and Use the Project

### Requirements
- Python 3.x
- Pillow (Python Imaging Library)

### Steps

1. **Clone the repository:**

```bash
git clone <repository-url>
cd <repository-directory>
```

2. **Setup Virtual Environment (Optional but recommended):**

If you want to use a virtual environment (recommended):

```bash
python3 -m venv myenv
source myenv/bin/activate  # Use `myenv/bin/activate.fish` for Fish shell
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the script:**

```bash
python steganography.py
```

5. **Follow the prompts:**

The script will prompt you to choose whether you want to store text in an image or retrieve text from an encoded image. Follow the instructions and provide the necessary inputs (image path and text).

### Usage

**Storing Text in an Image:**

- Enter `store` when prompted.
- Provide the path to the image file you want to encode text into.
- Enter the text you want to hide in the image.

**Retrieving Text from an Encoded Image:**

- Enter `retrieve` when prompted.
- Provide the path to the encoded image file.
- The script will decode the hidden text and display it.

## 3. Explanation of How the Code Works

The code uses the LSB (Least Significant Bit) technique to embed a binary representation of the text message into the red, green, and blue channels of each pixel in the image.

**Encoding Text:**

1. The text message is converted into binary format.
2. The code checks if the binary representation of the text can fit within the image's pixels.
3. It iterates over each pixel in the image and modifies the least significant bit of the red, green, and blue channels to encode the binary text.
4. The modified image with the encoded text is saved as a new file (e.g., `encoded_image.png`).

**Decoding Text:**

1. The code iterates over each pixel in the encoded image.
2. It extracts the least significant bit from the red, green, and blue channels of each pixel, forming a binary string.
3. The binary string is converted back to text characters using the ASCII encoding.
4. The decoded text is returned.

## 4. Use Cases of the Project

- **Secure Communication:** Sending secret messages hidden in plain sight within images.
- **Digital Watermarking:** Embedding copyright information or author details within images.
- **Covert Data Transmission:** Transmitting sensitive data concealed within innocuous-looking images.

## 5. Limitations of the Project

- **Capacity:** The amount of text that can be hidden is limited by the size of the image and the number of available pixels.
- **Security:** LSB steganography is a basic technique and can be detected by sophisticated analysis tools designed to detect steganographic content.
- **Image Format:** Currently, the code supports only image formats supported by the Pillow library (e.g., JPEG, PNG, BMP).
- **Image Quality:** Modifying the least significant bits of pixel values may introduce visually perceptible artifacts in the encoded image, especially in areas with smooth color gradients.

## 6. Summary

This project demonstrates a basic implementation of image steganography using Python and the Pillow library. It allows users to hide text messages within images using the LSB technique. The project is suitable for educational purposes and as a starting point for further exploration into steganography techniques.

Feel free to experiment with different images and text messages to explore the capabilities of this implementation. However, it's important to note that this implementation is for educational purposes only and should not be used for transmitting sensitive or confidential information in real-world scenarios without additional security measures.
