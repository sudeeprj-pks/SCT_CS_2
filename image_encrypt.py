from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            # Apply a simple pixel manipulation (XOR encryption)
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[i, j] = (r, g, b)

    img.save(output_path)
    print(f" Image encrypted successfully as {output_path}")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[i, j] = (r, g, b)

    img.save(output_path)
    print(f" Image decrypted successfully as {output_path}")

# Example usage
if __name__ == "__main__":
    print("=== Simple Image Encryption Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").lower()
    input_path = input("Enter image path: ")
    output_path = input("Enter output path: ")
    key = int(input("Enter encryption key (number): "))

    if choice == 'e':
        encrypt_image(input_path, output_path, key)
    elif choice == 'd':
        decrypt_image(input_path, output_path, key)
    else:
        print(" Invalid choice!")
