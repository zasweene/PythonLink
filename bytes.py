def byte_to_hex_string(file_path, output_path):
    with open(file_path, 'rb') as file:
        byte_data = file.read()

    with open(output_path, 'w') as output_file:
        formatted_bytes = []
        for i, byte in enumerate(byte_data):
            formatted_bytes.append(f"0x{byte:02x}")
            if (i + 1) % 16 == 0:
                output_file.write(", ".join(formatted_bytes) + ",\n")
                formatted_bytes = []

        if formatted_bytes:
            output_file.write(", ".join(formatted_bytes) + "\n")

# Example usage
file_path = 'pngcomp.png'         # Replace with your binary file path
output_path = 'bytes.txt'        # Output file path
byte_to_hex_string(file_path, output_path)
