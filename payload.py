import itertools
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def generate_payload():
    try:
        num_words = int(entry_num_words.get())
        letters = entry_letters.get() if var_letters.get() else "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = entry_digits.get() if var_digits.get() else "0123456789"
        symbols = entry_symbols.get() if var_symbols.get() else "!@#$%^&*()-_=+[]{}|;:,.<>?/"
        
        charset = "".join(filter(None, [letters, digits, symbols]))
        
        if not charset:
            messagebox.showerror("Error", "At least one character set must be selected.")
            return
        
        payload = ["".join(p) for p in itertools.product(charset, repeat=num_words)]
        
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write("\n".join(payload))
            messagebox.showinfo("Success", f"Payload saved at: {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Bruteforce Payload Generator")
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="#2c3e50")  

ascii_art = '''
                        ____________
                      .~      ,   . ~.
                     /                \\
                    /      /~\/~\   ,  \\
                   |   .   \    /   '   |
                   |         \/         |
          XX       |  /~~\        /~~\  |       XX
        XX  X      | |  o  \    /  o  | |      X  XX
      XX     X     |  \____/    \____/  |     X     XX
 XXXXX     XX      \         /\        ,/      XX     XXXXX
X        XX%;;@      \      /  \     ,/      @%%;XX        X
X       X  @%%;;@     |           '  |     @%%;;@  X       X
X      X     @%%;;@   |. ` ; ; ; ;  ,|   @%%;;@     X      X
 X    X        @%%;;@                  @%%;;@        X    X
  X   X          @%%;;@              @%%;;@          X   X
   X  X            @%%;;@          @%%;;@            X  X
    XX X             @%%;;@      @%%;;@             X XX
      XXX              @%%;;@  @%%;;@              XXX
                         @%%;;%%;;@
                           @%%;;@
                         @%%;;@..@@
                          @@@  @@@
'''

ascii_label = tk.Label(root, text=ascii_art, font=("Courier", 8), bg="#2c3e50", fg="white", justify="left")
ascii_label.pack()

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TCheckbutton", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

label_num_words = ttk.Label(frame, text="Number of characters per word:")
label_num_words.grid(row=0, column=0, sticky="w")
entry_num_words = ttk.Entry(frame, width=10)
entry_num_words.grid(row=0, column=1, pady=5)

var_letters = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

chk_letters = ttk.Checkbutton(frame, text="Include Letters", variable=var_letters)
chk_letters.grid(row=1, column=0, sticky="w")
entry_letters = ttk.Entry(frame, width=30)
entry_letters.grid(row=1, column=1, pady=5)

chk_digits = ttk.Checkbutton(frame, text="Include Digits", variable=var_digits)
chk_digits.grid(row=2, column=0, sticky="w")
entry_digits = ttk.Entry(frame, width=30)
entry_digits.grid(row=2, column=1, pady=5)

chk_symbols = ttk.Checkbutton(frame, text="Include Symbols", variable=var_symbols)
chk_symbols.grid(row=3, column=0, sticky="w")
entry_symbols = ttk.Entry(frame, width=30)
entry_symbols.grid(row=3, column=1, pady=5)

generate_button = ttk.Button(frame, text="Generate", command=generate_payload)
generate_button.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
