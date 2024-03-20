import tkinter as tk
from tkinter import messagebox

# Define the table of numerical values for each letter
table = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

# Define the affine cipher equation
def affine_cipher(x):
    return (3 * x + 14) % 26

# Define the inverse affine cipher equation
def inverse_affine_cipher(y):
    return (9 * (y - 14)) % 26

# Define a function to encipher a word using the affine cipher
def encipher(word):
    enciphered_word = ''
    for letter in word.upper():  # Convert input word to uppercase
        if letter in table:
            numerical_value = table[letter]
            enciphered_value = affine_cipher(numerical_value)
            enciphered_letter = list(table.keys())[list(table.values()).index(enciphered_value)]
            enciphered_word += enciphered_letter
        else:
            enciphered_word += letter  # Preserve non-alphabetic characters
    return enciphered_word

# Define a function to decipher an enciphered word using the inverse affine cipher
def decipher(enciphered_word):
    deciphered_word = ''
    for letter in enciphered_word:
        if letter in table:
            enciphered_value = table[letter]
            deciphered_value = inverse_affine_cipher(enciphered_value)
            deciphered_letter = list(table.keys())[list(table.values()).index(deciphered_value)]
            deciphered_word += deciphered_letter
        else:
            deciphered_word += letter  # Preserve non-alphabetic characters
    return deciphered_word


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

# Function to handle enciphering and deciphering
def process_text():
    word = entry.get().strip()
    if len(word) >= 7 and word.isalpha():
        enciphered_word = encipher(word)
        messagebox.showinfo("Enciphered Word", enciphered_word)
        deciphered_word = decipher(enciphered_word)
        messagebox.showinfo("Deciphered Word", deciphered_word)
        response = messagebox.askyesno("Continue?", "Do you want to continue?")
        if response:
            entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a word with 7 or more alphabetic characters.")

# Create the main window
root = tk.Tk()
root.title("Affine Cipher")

# Create a label and an entry widget for user input
label = tk.Label(root, text="Enter a word with 7 or more alphabetic characters:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create a button to process the text
process_button = tk.Button(root, text="Process", command=process_text)
process_button.pack()

# Set window dimensions
window_width = 600
window_height = 400

# Center the window
center_window(root, window_width, window_height)

# Run the main event loop
root.mainloop()
