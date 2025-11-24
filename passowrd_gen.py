import random
import string

    # 1. Define the possible characters based on user input
    characters = ""
    
    if include_letters:
        characters += string.ascii_letters # Uppercase and lowercase letters
    
    if include_numbers:
        characters += string.digits # 0123456789
    
    if include_symbols:
        # Punctuation set is a good, safe set of symbols
        characters += string.punctuation
    
    # Check if any character set was selected
    if not characters:
        return "Error: You must select at least one character type (letters, numbers, or symbols)."

    password_list = []
    
    # Add at least one of each selected type to guarantee complexity
    if include_letters:
        # Prioritize different cases for better distribution
        password_list.append(random.choice(string.ascii_lowercase))
        password_list.append(random.choice(string.ascii_uppercase))
    
    if include_numbers:
        password_list.append(random.choice(string.digits))
        
    if include_symbols:
        password_list.append(random.choice(string.punctuation))
    
    # Recalculate remaining length after adding guaranteed characters
    # If the user asks for a very short password (e.g., length=4), this handles the scenario gracefully
    remaining_length = max(0, length - len(password_list))

    # 3. Fill the rest of the password length randomly
    # Use the combined `characters` string for the remaining slots
    for _ in range(remaining_length):
        password_list.append(random.choice(characters))
    
    # 4. Shuffle the list to randomize the order of the guaranteed characters
    random.shuffle(password_list)

    # 5. Convert the list back into a single string
    password = "".join(password_list)
    
    # Ensure the password matches the desired length (important if the guaranteed list was too long)
    return password[:length]

# --- User Interface/Example Usage ---
if __name__ == "__main__":
    print("✨ **Welcome to the Python Password Generator!** ✨")
    
    # Get user input for password length
    while True:
        try:
            p_length = int(input("Enter the desired password length (e.g., 12): "))
            if p_length <= 0:
                print("Length must be a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    # Get user input for complexity
    use_letters = input("Include letters (y/n)? ").lower() == 'y'
    use_numbers = input("Include numbers (y/n)? ").lower() == 'y'
    use_symbols = input("Include symbols (y/n)? ").lower() == 'y'
    
    if not (use_letters or use_numbers or use_symbols):
        print("\n❌ You must choose at least one character type. Please try again.")
    else:
        # Generate and display the password
        final_password = generate_password(
            length=p_length,
            include_letters=use_letters,
            include_numbers=use_numbers,
            include_symbols=use_symbols
        )
        print("\n🔑 **Generated Password:**")
        print(f"**{final_password}**")