# PythonLink

This program receives files from the board via USB.

## Running the program

- The program can be run from the terminal using python.
- Once running, it will wait until it receives a frame of 0xFF, indicating the start of file transmission.
- The program will continue to pipe the incoming byte stream into a .png file.
- The program will continue to run until a frame of 0xAA is received, indicating the end of file transmission.

## Note

- This program assumes that the 'Receiver.c' program is running on the board.
- The COM port is hardcoded in this program and may need to be modified to accomodate the specific COM port that the board is connected to.

# Bytes

This program converts a .png file into a byte stream. These bytes can be copied into, and hard coded, onto the boards.

