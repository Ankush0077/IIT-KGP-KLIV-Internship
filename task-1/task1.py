import random
from rsa.key import newkeys
from rsa.pkcs1 import encrypt, decrypt
import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode

random.seed(42)

# Generate a random 2x2 matrix with values between 0 and 1.
matrix = [[random.random(), random.random()],
           [random.random(), random.random()]]
print(f'\nThe original matrix is: \n\n{matrix}\n\n')

# Convert the floating-point values to integers.
matrix = [[int(value * (10**18)) for value in row] for row in matrix]
print(f'After converting the floating value into integers, the matrix becomes: \n\n{matrix}\n\n')


# Generate RSA keys
(public_key, private_key) = newkeys(1024)
print(f'For implementing RSA algorithm, the keys are: \n\nPublic Key: {public_key}\n\nPrivate Key: {private_key}\n\n')

# Convert the matrix to a string representation
matrix = str(matrix).encode('latin-1')
print(f'After converting the matrix into bytes for encryption, the bytes is: \n\n{matrix}\n\n')

# Encrypt the matrix using RSA public key
matrix = encrypt(matrix, public_key)
print(f'The encrypted message is: \n\n{matrix}\n\n')

# print(f'{matrix.decode("latin-")}\n\n')

# Generate the QR code from the encrypted matrix
qr_code = pyqrcode.create(matrix.decode('latin-1'))
print(f'The generated QR Code from the encrypted matrix is: \n\n{qr_code}\n\n')

# Save the QR code as an image file
qr_code.png('encrypted_qr_code.png', scale=6)

# Step 6: Read the QR code image and decode the encrypted matrix
qr_code_image = Image.open('encrypted_qr_code.png')
qr_code_data = decode(qr_code_image)
matrix = qr_code_data[0].data.decode().encode('latin-1')
print(f'The decrypted QR Code is: \n\n{(matrix)}\n\n')

# Step 7: Decrypt the encrypted matrix using the private key
matrix = decrypt(matrix, private_key)
print(f'The decrypted bytes of matrix is: \n\n{matrix}\n\n')
matrix = eval(matrix.decode('latin-1'))
print(f'The decrypted integer value matrix is: \n\n{matrix}\n\n')

# Step 8: Convert the integers back to floating-point values
matrix_float = [[value / (10 ** 18) for value in row] for row in matrix]
print(f'The decrypted matrix is: \n\n{matrix_float}\n\n')