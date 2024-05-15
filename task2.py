from PIL import Image

def perform_xor_operation(data, key):
    result = bytearray()
    for byte in data:
        result.append(byte ^ key)
    return bytes(result)

def encrypt_image():
    path = input('Enter path of Image: ')
    key = int(input('Enter Key for encryption: '))
    
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    
    encrypted_data = perform_xor_operation(image, key)
    encrypted_path = path.replace('.jpg', '_encrypted.jpg')
    
    with open(encrypted_path, 'wb') as fout:
        fout.write(encrypted_data)
    
    print('Encryption Done. Encrypted file saved as:', encrypted_path)

def decrypt_image():
    path = input('Enter path of Image: ')
    key = int(input('Enter Key for decryption: '))
    
    fin = open(path, 'rb')
    encrypted_data = fin.read()
    fin.close()
    
    decrypted_data = perform_xor_operation(encrypted_data, key)
    decrypted_path = path.replace('_encrypted.jpg', '_decrypted.jpg')
    
    with open(decrypted_path, 'wb') as fout:
        fout.write(decrypted_data)
    
    print('Decryption Done. Decrypted file saved as:', decrypted_path)

try:
    choice = input('Enter "E" to encrypt or "D" to decrypt: ')
    
    if choice.upper() == 'E':
        encrypt_image()
    elif choice.upper() == 'D':
        decrypt_image()
    else:
        print('Invalid choice. Please enter "E" for encryption or "D" for decryption.')

except Exception as e:
    print('Error caught:', type(e).__name__, '-', str(e))