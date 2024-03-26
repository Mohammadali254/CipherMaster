import tkinter as tk
from tkinter import messagebox

# Define the table of numerical values for each letter
table = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
         'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
         'Z': 25}

encipher_flag = True


def affine_cipher(x):
    """Define the affine cipher equation"""
    return (3 * x + 14) % 26


def inverse_affine_cipher(y):
    """Define the inverse affine cipher equation"""
    return (9 * (y - 14)) % 26


def encipher(word):
    """Encipher a word using the affine cipher"""
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


def decipher(enciphered_word):
    """Decipher text using the inverse affine cipher"""
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
    """Center the window on the screen based on the dimensions of the window"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


# Function to handle enciphering and deciphering
def process_text():
    entry_content = entry.get().strip()

    if len(entry_content) >= 7:

        output_content = encipher(entry_content) if encipher_flag else decipher(entry_content)

        output.config(state='normal')
        output.delete('1.0', tk.END)
        output.insert('1.0', output_content)
        output.config(state='disabled')

        entry.delete(0, tk.END)

    else:
        messagebox.showerror("Error", "Please enter a word with 7 or more alphabetic characters.")


def handle_toggle_task():
    global encipher_flag

    if encipher_flag:
        encipher_flag = False
        toggle_task_button_text.set("Decipher")
        label_text.set("Enter cipher text to decipher:")
    else:
        encipher_flag = True
        toggle_task_button_text.set("Encipher")
        label_text.set("Enter a word with at least 7 alphabets to encipher:")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Affine Cipher")
    root["padx"] = 32
    root["pady"] = 20

    toggle_task_button_text = tk.StringVar()
    toggle_task_button_text.set("Encipher" if encipher_flag else "Decipher")
    toggle_task_button = tk.Button(root, textvariable=toggle_task_button_text, command=handle_toggle_task,
                                   justify=tk.LEFT)
    toggle_task_button.grid(row=0, column=0, sticky=tk.W, pady=8)

    # Create a label and an entry widget for user input
    label_text = tk.StringVar()
    label_text.set("Enter a word with at least 7 alphabets to encipher:")
    label = tk.Label(root, textvariable=label_text, justify=tk.LEFT)
    label.grid(row=1, column=0, sticky=tk.W)

    entry = tk.Entry(root, justify=tk.LEFT, width=48)
    entry.grid(row=2, column=0, sticky=tk.W)

    # Create a button to process the text
    process_button = tk.Button(root, text="Process", command=process_text, justify=tk.LEFT)
    process_button.grid(row=3, column=0, sticky=tk.W, pady=8)

    output_label_text = tk.StringVar()
    output_label_text.set("")

    output = tk.Text(root, wrap='word', height=1, borderwidth=0, highlightthickness=0, fg="green", width=48)
    output.grid(row=4, column=0, sticky=tk.W)

    # Set window dimensions
    window_width = 600
    window_height = 400

    # Center the window
    center_window(root, window_width, window_height)

    # Run the main event loop
    root.mainloop()
