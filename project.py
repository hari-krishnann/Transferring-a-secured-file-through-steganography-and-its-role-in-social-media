from PIL import Image

def encode_text(image_path, text):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    max_text_length = (width * height * 3) // 8

    binary_text = ''.join(format(ord(char), '08b') for char in text)

    if len(binary_text) > max_text_length:
        raise ValueError("Text too long to encode in the given image")

    index = 0
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            if index < len(binary_text):
                r = (r // 2) * 2 + int(binary_text[index])
                index += 1
            if index < len(binary_text):
                g = (g // 2) * 2 + int(binary_text[index])
                index += 1
            if index < len(binary_text):
                b = (b // 2) * 2 + int(binary_text[index])
                index += 1

            pixels[i, j] = (r, g, b)

    img.save("/encoded_image.png")

def decode_text(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    binary_text = ''
    index = 0

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            binary_text += str(r % 2)
            binary_text += str(g % 2)
            binary_text += str(b % 2)
            index += 3

            if len(binary_text) >= 8 and binary_text[-8:] == '00000000':
                binary_text = binary_text[:-8]
                text = ''.join([chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8)])
                return text

    return "No hidden text found in the image"


choice = input("Do you want to store text or retrieve text? (store/retrieve): ")

if choice == 'store':
    image_path = input("Enter the path of the image: ")
    text_to_store = input("Enter the text to be stored: ")
    encode_text(image_path, text_to_store)
    print("Text stored in the image!")

elif choice == 'retrieve':
    image_path = input("Enter the path of the encoded image: ")
    extracted_text = decode_text(image_path)
    print("Extracted text from the image:", extracted_text)

else:
    print("Invalid choice.")