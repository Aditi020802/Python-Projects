import os

def create_file(filename):
    try:
        with open(filename, "x", encoding="utf-8"):
            pass
        return "File created successfully."
    except FileExistsError:
        return "File already exists."
    except OSError as error:
        return f"Error: {error}"

def write_file(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(data)
        return "Data written successfully."
    except OSError as error:
        return f"Error: {error}"

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        return content if content else "File is empty."
    except FileNotFoundError:
        return "Error: File not found."
    except OSError as error:
        return f"Error: {error}"

def append_file(filename, data):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(data)
        return "Data appended successfully."
    except OSError as error:
        return f"Error: {error}"
