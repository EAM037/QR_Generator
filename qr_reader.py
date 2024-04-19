import qrcode
import os

def generate_qr_code(data, filename):
    # Create a QRCode object with specified parameters
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Add the data to be encoded
    qr.add_data(data)
    # Generate the QR code
    qr.make(fit=True)

    # Make an image representation of the QR code with specified colors
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)

def main():
    # Prompt the user to input data and filename
    data = input("Enter the data you want to encode: ")
    filename = input("Enter the filename for the QR code (without extension): ")

    # Get the directory of the current script
    directory = os.path.dirname(os.path.realpath(__file__))

    # Create the full path to the file
    full_path = os.path.join(directory, filename + '.png')

    # Call the generate_qr_code function with user inputs
    generate_qr_code(data, full_path)

    # Print a confirmation message
    print(f"QR code saved as {full_path}")

if __name__ == "__main__":
    main()
