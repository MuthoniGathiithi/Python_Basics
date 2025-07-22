import barcode
from barcode.writer import ImageWriter

def generate_barcode():
    data = input("Enter the number or text for the barcode: ")
    
    # Use Code128 format for alphanumeric data
    barcode_class = barcode.get_barcode_class('code128')
    
    my_barcode = barcode_class(data, writer=ImageWriter())
    filename = my_barcode.save("generated_barcode")

    print(f"Barcode generated and saved as '{filename}.png'")

if __name__ == "__main__":
    generate_barcode()
