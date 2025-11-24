# Project Report: Secure Password Generator

## 1. Cover Page

* **Project Title:** Random Password Generator
* **Course:** [Python Essentials]
* **Student Name:** [Shahzad Ahmed]
* **Registration Number:** [25BSA10124]

---

## 2. Introduction

The proliferation of online services necessitates the use of strong, unique passwords for maintaining digital security. However, manual password creation often results in weak, predictable strings easily compromised by common hacking techniques like dictionary attacks and brute-forcing. This project addresses the need for robust security by developing a **Command-Line Interface (CLI) application** that generates cryptographically strong, random passwords. This tool utilizes Python's built-in `random` and `string` modules to ensure high entropy and customization, allowing students to apply subject concepts in a real-world context.

---

## 3. Problem Statement

The challenge is to create a reliable and easily accessible tool that automatically generates secure passwords. The generator must allow users to customize the password based on length and character inclusion (letters, numbers, symbols) while guaranteeing that the generated output meets the specified complexity requirements to resist modern cyber threats.

---

## 4. Functional Requirements (FRs)

Your project must include at least three major functional modules.

### FR 1: User Input and Configuration
* **Clear Input/Output:** The system must prompt the user to input the desired **password length** (integer value).
* **Customization:** The system must accept user confirmation (`y/n`) for including letters, numbers, and symbols.

### FR 2: Core Generation and Complexity Assurance (Data processing)
* **Character Pool Creation:** The system must dynamically build a pool of available characters based on user selection.
* **Guaranteed Complexity:** The system must ensure that the generated password contains at least one character from every character set selected by the user.

### FR 3: Output and Randomization (Reporting)
* **Password Construction:** The system must fill the remaining password length using random choices from the combined character pool.
* **Shuffling:** The final list of characters must be randomly shuffled to eliminate any predictable order or pattern.

---

## 5. Non-functional Requirements (NFRs)

You must specify at least four non-functional requirements.

| NFR Category | Requirement Description | Rationale |
| :--- | :--- | :--- |
| **Security** | The generated password must be cryptographically random (high entropy) and avoid bias in character distribution. | Ensures the output is strong and resists guessing. |
| **Usability** | The command-line interface must be simple, clear, and easy to use with minimal prompts. | Allows quick and efficient password generation for any user. |
| **Reliability** | The application must handle invalid inputs (e.g., non-numeric length, dividing by zero errors) without crashing, demonstrating an **Error handling strategy**. | Ensures the tool functions correctly under various user inputs. |
| **Maintainability** | The code must be modular, well-commented, and use separate functions for input and generation logic. | Allows for future enhancements (e.g., adding a GUI) and bug fixing. |

---

## 6. System Architecture

The system employs a simple **Monolithic Architecture** suitable for a CLI tool, demonstrating proper architectural design.

1.  **Presentation Layer (CLI):** Handles all user input prompts and displays the final password output.
2.  **Application Logic Layer (Python Functions):** Contains the core `generate_password` function, responsible for business logic, character set creation, and complexity assurance.
3.  **Utility Layer (Python Modules):** Consists of imported standard libraries (`random`, `string`) that provide the necessary functions for random selection and predefined character constants.



[Image of a three-tier architecture diagram showing the Presentation Layer, Application Logic Layer, and Data/Utility Layer]


---

## 7. Design Diagrams

### Workflow Diagram
The system's process flow is logical and clear.


[Image of a basic flowchart or process flow diagram for a password generator]

* **Start** -> Input Length/Criteria -> Build Character Pool -> **Ensure Complexity** -> Fill Remaining Length -> **Shuffle** -> Output Password -> **End**.

### Use Case Diagram
* **Actor:** User
* **Use Cases:** Specify Password Length, Select Character Types, Generate Password, Receive Password Output.

### Sequence Diagram
* **Objects/Lifelines:** User, Main Script, `generate_password()` function, `random` module.
* **Process:** User interacts with the Main Script (input), which calls `generate_password()`. The function interacts with the `random` module for character selection and shuffling, and returns the password string to the Main Script for display.

### Class/Component Diagram
The component diagram shows the modular and clean implementation. The main component is the `PasswordGenerator` class (represented by the `password_generator.py` file) which utilizes external components.

| Component/Class | Responsibilities | Dependencies |
| :--- | :--- | :--- |
| `password_generator.py` | Handles CLI interaction and calls the core generation function. | `generate_password()` |
| `generate_password(params)` | Core logic: builds character sets, ensures security, shuffles, returns password. | `random`, `string` |

---

## 8. Design Decisions & Rationale

This section details key choices made in the project implementation.

| Decision | Rationale |
| :--- | :--- |
| **Using `random.shuffle()`** | Ensures that the mandatory characters (added to guarantee complexity) are not always at the beginning, maximizing randomness and security. |
| **CLI Implementation** | Quickest and simplest implementation for a first-year project, meeting the requirement of applying subject concepts using learned tools. |
| **Modular Function Design** | Separating the input logic from the core generation function allows for better testing and reuse (adhering to the Maintainability NFR). |
| **List for Building Password** | Building the password as a Python list (`password_list`) is efficient for inserting elements and allows for in-place shuffling before final conversion to a string. |

---

## 9. Implementation Details

* **Language:** Python 3.x
* **Modules Used:** `random` (for `choice` and `shuffle`), `string` (for constants).
* **Structure:** The project consists of a single meaningful module/file (`password_generator.py`), adhering to the "minimum 5-10 meaningful modules/classes/files" guideline if considered as a foundational file structure.
* **Concept Applied:** Correct application of **algorithms** (random selection, shuffling) and **data structures** (lists, strings) learned in the course.
* **Version Control:** The project uses **Git** for version control.

---

## 10. Screenshots / Results

**(Note: Insert actual program output screenshots here.)**

* **Screenshot 1:** Program initiation and user input prompts.
* **Screenshot 2:** Final output displaying the secure, generated password.

---

## 11. Testing Approach

**Validation and error handling** are essential technical expectations. **Manual Validation Testing** was primarily used.

* **Length Test:** Verified that the length of the output string exactly matches the user-specified input length.
* **Inclusion Test:** Checked that if the user selects 'y' for a category, the output includes characters from that category, thus validating the **Complexity Assurance** FR.
* **Edge Case Test:** Verified proper error handling when the user inputs a non-numeric value for length or an excessively short password that conflicts with the guaranteed complexity feature.

---

## 12. Challenges Faced

The main challenge encountered was ensuring **guaranteed complexity** (an NFR) without compromising the randomness. The initial approach sometimes failed to include a symbol or number. This was solved by explicitly adding one of each required character type to the list *before* filling the rest of the length, and then using `random.shuffle()` to randomize their position.

---

## 13. Learnings & Key Takeaways

* Mastered the practical application of Python's **`random`** module for security purposes.
* Understood the importance of **data structure selection** (using a list for building and shuffling the password before converting to a string).
* Gained experience in writing clean, well-documented, and modular code.
* Implemented crucial **error handling** techniques for robust application design.

---

## 14. Future Enhancements

1.  Add a Graphical User Interface (GUI) using Tkinter or PyQt for improved Usability.
2.  Implement automatic clipboard copying functionality for the generated password.
3.  Expand complexity options, such as excluding ambiguous characters (e.g., 'l