# QR Code Generator

This project is a QR code generator application built with Python.
It allows users to input data and generate custom QR codes with various options for customization such as size, border, error correction level, and colors. 
The generated QR codes can be saved as image files in different formats.

## Features
- Generate QR codes for text, URLs, and more.
- Customize QR code version (size), box size, and border size.
- Choose error correction levels (Low, Medium, Quartile, High).
- Customize the colors of the QR code and its background.
- Save QR codes in different image formats (e.g., PNG, JPEG).

## Requirements
- Python 3.x
- `qrcode` library
- `Pillow` library

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/qrcode-generator.git
    ```
2. Navigate to the project directory:
    ```sh
    cd qrcode-generator
    ```
3. Install the required dependencies:
    ```sh
    pip install qrcode[pil]
    ```

## Usage
1. Run the QR code generator script:
    ```sh
    python qrgen.py
    ```
2. Follow the prompts to enter the data and customization options:
    - Enter the data you want to store in the QR code (e.g., a URL).
    - Choose the QR code version (1-40, where 1 is the smallest size and 40 is the largest).
    - Enter the box size (the size of each QR code unit).
    - Enter the border size (the thickness of the border).
    - Choose the error correction level:
        1. Low (7% of codewords can be restored)
        2. Medium (15% of codewords can be restored)
        3. Quartile (25% of codewords can be restored)
        4. High (30% of codewords can be restored)
    - Enter the fill color for the QR code (default is black).
    - Enter the background color for the QR code (default is white).
    - Enter the file path to save the QR code (e.g., `C:/Users/nii/python projects/qrnew.png`).

3. **The generated QR code will be saved to the specified file path.**

## Example
Here's an example of how to use the QR code generator:
```plaintext
QR CODE GENERATOR
Created by @NIKHIL
Enter the data you want to store in the QR code: https://www.example.com
Enter the version (1-40, where 1 is the smallest size and 40 is the largest): 10
Enter the box size (the size of each QR code unit, e.g., 10): 10
Enter the border size (the thickness of the border, e.g., 4): 4
Choose error correction level:
1. Low (7% of codewords can be restored)
2. Medium (15% of codewords can be restored)
3. Quartile (25% of codewords can be restored)
4. High (30% of codewords can be restored)
Enter the number corresponding to your choice: 3
Enter the fill color for the QR code (default is black): blue
Enter the background color for the QR code (default is white): yellow
Enter the file path to save the QR code (e.g., C:/Users/nii/python projects/qrnew.png): C:/Users/nii/python projects/qrnew.png
QR Code generated successfully and saved to C:/Users/nii/python projects/qrnew.png
