# Password Security Analyzer 🔐

A Python command-line project that examines basic password characteristics and gives practical security feedback. Built as a learning project focused on input validation, conditional logic, pattern detection, testing, and defensive security awareness.

## Features

- Checks password length and character variety
- Flags a small built-in set of commonly used passwords
- Detects obvious character sequences and repeated characters
- Provides a simple heuristic assessment and recommendations
- Hides password entry in the terminal using Python's `getpass`
- Includes automated unit tests

> **Security note:** This is an educational tool, **not** a production password-strength meter. Its score is heuristic, does not model real-world cracking resistance, and cannot verify whether a password has been breached. Do not enter real account passwords into unfamiliar tools. The program does not intentionally log or transmit input.

## Requirements

- Python 3.9 or newer
- No third-party packages required

## Run the program

```bash
python password_analyzer.py
```

On some Windows systems, use `py password_analyzer.py` instead.

Use a **made-up test password** when prompted. Input is hidden in a normal terminal.

## Run the tests

```bash
python -m unittest discover -s tests -v
```

## Example

```text
=== Password Security Analyzer ===
Educational feedback only. Never enter a real password into an untrusted tool.
Enter a MADE-UP test password (hidden input):

Assessment: Very weak (0/4)
- This is a widely used password. Choose something unique.
```

The example uses the test input `password123` (which is hidden during actual entry).

## How it works

The `analyze_password` function checks the length and character categories of the supplied string, then applies penalties for common passwords, predictable sequences, and repeated characters. It returns a structured `Assessment` with a score, rating, and feedback. The CLI displays the results without printing the entered password.

## Project structure

```text
password-security-analyzer/
├── password_analyzer.py
├── tests/
│   └── test_password_analyzer.py
├── README.md
└── .gitignore
```

## Skills demonstrated

Python functions, data classes, regex, control flow, input validation, unit testing, CLI development, documentation, and basic password security concepts.

## Future improvements

- Evaluate passphrases and predictable substitutions more thoroughly
- Explore vetted password-estimation libraries such as `zxcvbn`
- Add more test cases and accessibility improvements

## Author

X'Zevious Broadus — Cybersecurity student at the University at Albany

[GitHub profile](https://github.com/Xayexe) · [Cybersecurity notes](https://github.com/Xayexe/cyber-notes)
