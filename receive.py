import serial
import time
import os  # Add this import

# Serial port settings
PORT = 'COM7'
BAUDRATE = 115200
TIMEOUT = 1

# Output file path
OUTPUT_FILE = 'output.png'

# Number of hex characters to skip and read
SKIP_BYTES = 19  # bytes
READ_BYTES = 66  # bytes
SKIP_CHARS = SKIP_BYTES * 2
READ_CHARS = READ_BYTES * 2

def main():
    reading = False

    # Delete output.png if it exists
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
        print(f"Deleted existing {OUTPUT_FILE}")

    try:
        with serial.Serial(PORT, BAUDRATE, timeout=TIMEOUT) as ser:
            print(f"Listening on {PORT}...")
            while True:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                if not line:
                    continue

                if "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" in line:
                    if not reading:
                        print("Start marker (FFFFFF) found. Beginning to read data...")
                        reading = True
                        continue
                    
                if "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" in line:
                    if reading:
                        hex_data = line.split("AAAAAAAA")[0]  # Keep only the part before the stop marker
                        print(f"Received hex stream (before marker): {hex_data}")

                        trimmed_data = hex_data[SKIP_CHARS:SKIP_CHARS + READ_CHARS]
                        binary_data = bytes.fromhex(trimmed_data)
                        with open(OUTPUT_FILE, 'ab') as f:
                            f.write(binary_data)
                        print(f"Written to {OUTPUT_FILE}: {binary_data}")
                        print("Stop marker (AAAAAAAA) found. Stopping and exiting.")
                        break

                if reading and "418C" in line:
                    hex_data = line
                    print(f"Received hex stream: {hex_data}")

                    if len(hex_data) >= (SKIP_CHARS + READ_CHARS):
                        trimmed_data = hex_data[SKIP_CHARS:SKIP_CHARS + READ_CHARS]
                        binary_data = bytes.fromhex(trimmed_data)
                        with open(OUTPUT_FILE, 'ab') as f:
                            f.write(binary_data)
                        print(f"Written to {OUTPUT_FILE}: {binary_data}")
                    else:
                        print("Received hex data is too short. Waiting for next response...")

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")

if __name__ == "__main__":
    main()
