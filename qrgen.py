import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H

def create_qr_code():
    print("QR CODE GENERATOR")
    print("Created by @NIKHIL")

    # Get the data to be stored in the QR code
    data = input("Enter the data you want to store in the QR code: ")

    # Get customization options from the user
    version = int(input("Enter the version (1-40, where 1 is the smallest size and 40 is the largest): "))
    box_size = int(input("Enter the box size (the size of each QR code unit, e.g., 10): "))
    border = int(input("Enter the border size (the thickness of the border, e.g., 4): "))

    print("Choose error correction level: ")
    print("1. Low (7% of codewords can be restored)")
    print("2. Medium (15% of codewords can be restored)")
    print("3. Quartile (25% of codewords can be restored)")
    print("4. High (30% of codewords can be restored)")
    error_correction = int(input("Enter the number corresponding to your choice: "))

    error_correction_levels = {
        1: ERROR_CORRECT_L,
        2: ERROR_CORRECT_M,
        3: ERROR_CORRECT_Q,
        4: ERROR_CORRECT_H
    }

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction_levels.get(error_correction, ERROR_CORRECT_L),
        box_size=box_size,
        border=border
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Customize the color of the QR code
    fill_color = input("Enter the fill color for the QR code (default is black): ")
    back_color = input("Enter the background color for the QR code (default is white): ")

    fill_color = fill_color if fill_color else "black"
    back_color = back_color if back_color else "white"

    # Create an image of the QR code
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Get the file path from the user
    file_path = input("Enter the file path to save the QR code (e.g., C:/Users/nii/python projects/qrnew.png): ")

    # Save the QR code image
    img.save(file_path)

    print("QR Code generated successfully and saved to", file_path)

if __name__ == "__main__":
    create_qr_code()
