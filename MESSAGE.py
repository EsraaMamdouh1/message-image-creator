import os
import shutil
import sys

def create_message_images(input_text):
    allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ. "
    char_to_num = {
        'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '10',
        'K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18', 'S': '19',
        'T': '20', 'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25', 'Z': '26', '.': '27', ' ': '28'
    }
    input_text = input_text.upper()  # Convert the input text to uppercase

    # Checking for disallowed characters
    for char in input_text:
        if char not in allowed_chars:
            raise ValueError(f"Character '{char}' is not allowed. Use only A-Z, '.', and space.")

    # Create the MESSAGE folder if it doesn't exist
    if not os.path.exists("MESSAGE"):
        os.makedirs("MESSAGE")
    else:
        # Clear the MESSAGE folder if it already exists
        shutil.rmtree("MESSAGE")
        os.makedirs("MESSAGE")

    # Copy the corresponding images to the MESSAGE folder
    for i, char in enumerate(input_text):
        num = char_to_num[char]
        src = os.path.join("Alphabet", f"{num}.jpg")
        
        # Check if the source file exists
        if not os.path.isfile(src):
            raise FileNotFoundError(f"Image file for character '{char}' not found in the Alphabet folder as '{num}.jpg'.")
        
        dst = os.path.join("MESSAGE", f"{i+1}_{char}.jpg")
        shutil.copy(src, dst)

if __name__ == "__main__":
    print("Please enter a message using only A-Z, '.', and spaces.")

    # Get the input message from the user
    input_text = input("Enter your message: ")

    try:
        create_message_images(input_text)
        print("Message created successfully! Check the 'MESSAGE' folder for the output images.")
    except ValueError as e:
        print(e)