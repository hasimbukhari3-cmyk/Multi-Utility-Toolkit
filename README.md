# Multi-Utility-Toolkit

# Multi-Utility Toolkit

## Description
A Python-based console application that demonstrates Python's modular structure by integrating multiple standard modules, custom modules, and packages. It provides utility functions for date-time operations, mathematical computations, random data generation, unique identifier creation, and file operations.

## Features
- **Datetime & Time**: Current date/time, date difference, custom formatting, stopwatch, countdown timer.
- **Math**: Factorial, compound interest, trigonometry, area calculations, unit conversions.
- **Random**: Random numbers, lists, passwords, OTPs, sampling.
- **UUID**: Generate UUID4 identifiers for files, records, and sessions.
- **File Operations**: Create, write, read, append, delete files via custom module.
- **Dynamic Exploration**: Explore module attributes using `dir()`.
- **Menu-Driven Interface**: Easy navigation with sub-menus.

## Project Structure
Multi-Utility-Toolkit/
│
├── main.py
├── toolkit_package/
│   ├── init.py
│   ├── file_operations.py
│   └── math_utilities.py
├── README.md
└── sample_output.txt

## Assumptions
- The toolkit is a console-based application.
- Users have Python 3.x installed.
- File operations work on text files (`.txt`).
- The stopwatch and countdown timer use the `time` module for delays.
- Random passwords include uppercase, lowercase, digits, and special characters.
- UUIDs are generated using `uuid.uuid4()`.
- Data persists between program runs.

## Modules Used
| Module | Type | Purpose |
|--------|------|---------|
| `datetime` | Built-in | Date and time operations |
| `time` | Built-in | Stopwatch and countdown |
| `math` | Built-in | Mathematical computations |
| `random` | Built-in | Random data generation |
| `uuid` | Built-in | Unique identifier generation |
| `string` | Built-in | String constants |
| `file_operations` | Custom | File handling |
| `math_utilities` | Custom | Unit conversions and advanced math |

## How to Run
1. Ensure Python 3.x is installed.
2. Clone the repository.
3. Run: `python main.py`

## The `__name__ == "__main__"` Paradigm
- `main.py` runs the menu only when executed directly.
- `file_operations.py` and `math_utilities.py` have test blocks that run only when executed directly, not when imported.

## Author
[hasim bukhari]
