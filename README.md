# 🔒 Random Password Generator

A simple and secure command-line tool built in **Python** to generate strong, customizable passwords based on user-defined length and character sets. This project uses the built-in `random` and `string` modules.

## ✨ Features

* **Customizable Length:** Users can specify the exact length of the password.
* **Character Selection:** Allows selection of character types: **Letters** (A-Z, a-z), **Numbers** (0-9), and **Symbols** ($\#, \!, \$, \dots$).
* **Guaranteed Complexity:** The generator ensures that at least one character of each selected type is included, maximizing security.
* **Shuffled Output:** Uses the `random.shuffle` function to prevent predictable patterns in the generated password.

---

## ⚙️ Prerequisites

To run this project, you only need **Python 3.x** installed on your system. No external libraries are required.

## 🚀 Getting Started

Follow these steps to run the password generator locally.

### 1. Save the file

Save the provided Python code as a file named `password_generator.py`.

### 2. Run the script

Execute the script from your terminal or command prompt:

```bash
python password_generator.py
