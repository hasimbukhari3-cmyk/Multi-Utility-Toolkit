"""
file_operations.py - Custom module for file handling operations.

This module demonstrates file handling using Python's built-in open() function
with different modes ('w', 'r', 'a') and proper exception handling.

Author: [Your Name]
Date: [Current Date]
"""

import os


def create_file(filename):
    """
    Create a new empty file.

    Args:
        filename (str): Name of the file to create.

    Returns:
        str: Success or error message.
    """
    try:
        if os.path.exists(filename):
            return f"File '{filename}' already exists."
        with open(filename, 'w', encoding='utf-8') as file:
            pass  # Create empty file
        return f"File '{filename}' created successfully!"
    except PermissionError:
        return "Error: Permission denied. Cannot create the file."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def write_to_file(filename, data):
    """
    Write data to a file (overwrites existing content).

    Args:
        filename (str): Name of the file.
        data (str): Data to write.

    Returns:
        str: Success or error message.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(data)
        return "Data written successfully!"
    except PermissionError:
        return "Error: Permission denied. Cannot write to the file."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def read_from_file(filename):
    """
    Read and return the contents of a file.

    Args:
        filename (str): Name of the file to read.

    Returns:
        str: File contents or error message.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        return content if content else "(File is empty)"
    except FileNotFoundError:
        return f"Error: File '{filename}' does not exist."
    except PermissionError:
        return "Error: Permission denied. Cannot read the file."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def append_to_file(filename, data):
    """
    Append data to an existing file.

    Args:
        filename (str): Name of the file.
        data (str): Data to append.

    Returns:
        str: Success or error message.
    """
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(data + "\n")
        return "Data appended successfully!"
    except PermissionError:
        return "Error: Permission denied. Cannot append to the file."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def delete_file(filename):
    """
    Delete a file.

    Args:
        filename (str): Name of the file to delete.

    Returns:
        str: Success or error message.
    """
    try:
        if not os.path.exists(filename):
            return f"File '{filename}' does not exist."
        os.remove(filename)
        return f"File '{filename}' deleted successfully!"
    except PermissionError:
        return "Error: Permission denied. Cannot delete the file."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# The __name__ == "__main__" paradigm: this block runs only when the
# module is executed directly, not when imported.
if __name__ == "__main__":
    print("Testing file_operations module directly...")
    print(create_file("test_file.txt"))
    print(write_to_file("test_file.txt", "Hello, World!"))
    print(read_from_file("test_file.txt"))
    print(append_to_file("test_file.txt", "Appended line."))
    print(read_from_file("test_file.txt"))
    print(delete_file("test_file.txt"))
