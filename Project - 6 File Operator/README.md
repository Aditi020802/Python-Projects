<div align="center">

# 📔 Personal Journal Manager

### A Python File Handling-Based Journal Application

**Create • Add • View • Search • Delete • Manage Journal Entries**

<p>
<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/File%20Handling-Implemented-6C5CE7?style=flat-square">
<img src="https://img.shields.io/badge/OOP-Implemented-0A7EA4?style=flat-square">
<img src="https://img.shields.io/badge/Exception%20Handling-Implemented-2E8B57?style=flat-square">
<img src="https://img.shields.io/badge/Console%20Application-Yes-444444?style=flat-square">
</p>

</div>

---

## 📌 Project Overview

**Personal Journal Manager** is a menu-driven Python console application that helps users create and manage journal entries in a text file. Each entry is saved with a timestamp. Users can add, view, search, and delete journal entries, create the journal file, and exit the application.

This project demonstrates file handling, object-oriented programming, exception handling, string processing, and menu-driven program design.

## ✨ Features

| Option | Feature | Description |
|:---:|---|---|
| 1 | Add a New Entry | Saves an entry with the current date and time |
| 2 | View All Entries | Displays all saved journal entries |
| 3 | Search for an Entry | Searches entries by keyword or date |
| 4 | Delete All Entries | Confirms before deleting the journal file |
| 5 | Create Journal File | Creates a new file if it does not already exist |
| 6 | Exit | Closes the application |

## 🖥️ Main Menu

```text
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Create Journal File
6. Exit

Enter your choice:
```

## 📝 Feature Details

### 1. Add a New Entry

The application asks for a journal entry, rejects empty input, creates a timestamp with `datetime.now()`, and appends the entry to the journal file.

Example:

```text
Enter your journal entry: Today I learned Python file handling.

Entry added successfully!
```

Saved format:

```text
[2026-10-13 10:30:00]
Today I learned Python file handling.
```

*The timestamp above is an example; the application uses the current date and time.*

### 2. View All Entries

Reads the journal file and displays all saved entries. It handles a missing file and an empty journal.

### 3. Search for an Entry

Searches entries by keyword or date. The search is case-insensitive and prints all matching entries.

### 4. Delete All Entries

The application asks for confirmation before deleting the journal file.

```text
Are you sure you want to delete all entries? (yes/no):
```

- Enter `yes` to delete the journal file.
- Enter `no` to cancel.
- Any other response displays a validation message.

**Warning:** Deleting the journal file removes all entries stored in it.

### 5. Create Journal File

Uses exclusive file creation mode (`x`). If the file already exists, the program informs the user rather than overwriting it.

### 6. Exit

Displays a goodbye message and ends the menu loop.

## 🛡️ Exception Handling

| Exception | Purpose |
|---|---|
| `FileNotFoundError` | Handles missing journal files |
| `FileExistsError` | Handles attempts to create a file that already exists |
| `PermissionError` | Handles file permission problems |
| `OSError` | Handles other file-system errors |

## 📚 Python Concepts Demonstrated

| Concept / Function | Usage |
|---|---|
| `class JournalManager` | Organizes journal functionality |
| `__init__()` | Initializes the journal filename |
| `main()` | Creates the object and starts the application |
| `if __name__ == "__main__"` | Runs the program when executed directly |
| `open()` | Opens the journal file |
| File mode `a` | Appends new entries |
| File mode `r` | Reads entries |
| File mode `x` | Creates a new file without overwriting an existing one |
| `datetime.now()` | Gets the current date and time |
| `strftime()` | Formats the timestamp |
| `os.remove()` | Deletes the journal file |
| `input()` | Receives user input |
| `strip()` | Removes surrounding whitespace |
| `splitlines()` | Processes file content line by line |
| `lower()` | Makes searching case-insensitive |
| List comprehension | Collects matching entries |
| `while True` | Keeps the menu running until exit |
| `try-except` | Handles file-related errors |

## 📂 Project Structure

```text
Personal-Journal-Manager/
│
├── main.py
├── README.md
├── journal.txt
│
└── assets/
    ├── Output1.png
    ├── Output2.png
    ├── Output3.png
    ├── Output4.png
    ├── Output5.png
    ├── Output6.png
    └── Project Demonstration.mp4
```

`journal.txt` is created when an entry is saved or when the user selects the create-file option. It may not exist before the program is run.

Put your six screenshots and demonstration video in the `assets` folder using the filenames above. If your actual filenames differ, update the paths in this README.

## 📸 Output Gallery

<div align="center">

<table>
<tr>
<td width="50%" align="center" valign="top">

### 🖥️ Output 1 — Main Menu

<img src="https://github.com/Aditi020802/Python-Projects/blob/main/Project%20-%206%20File%20Operator/Output/output-1.png" alt="Personal Journal Manager Output 1" width="100%">

</td>
<td width="50%" align="center" valign="top">

### 🖥️ Output 2 — Add Entry

<img src="https://github.com/Aditi020802/Python-Projects/blob/main/Project%20-%206%20File%20Operator/Output/output-2.png" alt="Personal Journal Manager Output 2" width="100%">

</td>
</tr>
<tr>
<td width="50%" align="center" valign="top">

### 🖥️ Output 3 — View Entries

<img src="https://github.com/Aditi020802/Python-Projects/blob/main/Project%20-%206%20File%20Operator/Output/output-3.png" alt="Personal Journal Manager Output 3" width="100%">

</td>
<td width="50%" align="center" valign="top">

### 🖥️ Output 4 — Search Entry

<img src="https://github.com/Aditi020802/Python-Projects/blob/main/Project%20-%206%20File%20Operator/Output/output-4.png" alt="Personal Journal Manager Output 4" width="100%">

</td>
</tr>
<tr>
<td width="50%" align="center" valign="top">

### 🖥️ Output 5 — Delete Entries

<img src="https://github.com/Aditi020802/Python-Projects/blob/main/Project%20-%206%20File%20Operator/Output/output-5.png" alt="Personal Journal Manager Output 5" width="100%">

</td>
<td width="50%" align="center" valign="top">

### 🖥️ Output 6 — Create File / Exit

<img src="https://github.com/Aditi020802/Python-Projects/blob/main/Project%20-%206%20File%20Operator/Output/output-6.png" alt="Personal Journal Manager Output 6" width="100%">

</td>
</tr>
</table>

</div>

---

## 🎥 Project Demonstration

<div align="center">

### ▶️ See the Complete Project in Action

The demonstration video shows the Personal Journal Manager workflow, including adding, viewing, searching, and deleting entries, creating the journal file, and exiting the application.

**[▶️ Open Project Demonstration Video](https://github.com/Aditi020802/Python-Projects/blob/main/Project%20-%206%20File%20Operator/Project%20Demonstration.mp4)**

</div>

> **Tip:** If GitHub does not preview the MP4 directly, click the link above to open the demonstration video.

Video location:

```text
assets/Project Demonstration.mp4
```

## 🚀 How to Run

### 1. Install Python

Install Python 3.x and check the installation:

```bash
python --version
```

On systems using `python3`, run:

```bash
python3 --version
```

### 2. Open the Project

Open the project folder in VS Code or another Python IDE.

### 3. Open the Terminal

Navigate to your project folder. Replace the example folder name if yours is different:

```bash
cd Personal-Journal-Manager
```

### 4. Run the Program

```bash
python main.py
```

Or:

```bash
python3 main.py
```

### 5. Use the Menu

Enter a number from `1` to `6` and follow the prompts.

## 📦 Requirements

- Python 3.x
- Standard-library modules: `os` and `datetime`
- No external packages required
- No database or API required

## 🎯 Learning Outcomes

- Create and use Python classes and objects
- Write timestamped data to text files
- Read and search file content
- Create files safely using exclusive creation mode
- Delete files with confirmation
- Handle file-related exceptions
- Use the `datetime` and `os` modules
- Validate user input
- Build a menu-driven console application

## 🚧 Possible Future Improvements

- Edit an individual journal entry
- Delete a single entry
- Add categories or tags
- Add password protection
- Export entries to PDF or CSV
- Add backup and restore functionality
- Create a graphical user interface

## 📊 Project Snapshot

| Category | Details |
|---|---|
| Project | Personal Journal Manager |
| Language | Python 3.x |
| Application Type | Console Application |
| Main Class | `JournalManager` |
| Default File | `journal.txt` |
| Storage | Text file |
| Main Concepts | File handling, OOP, exception handling |
| Output Screenshots | 6 |
| Demonstration Video | `assets/Project Demonstration.mp4` |
| External Packages | None |

## 🧑‍💻 Author

<div align="center">

### **Sujal Patel**

Python Developer / Learner

**Python • File Handling • OOP • Exception Handling • Problem Solving**

</div>

---

## 📄 License

This project was created for educational and learning purposes.

<div align="center">

### 📔 Personal Journal Manager

**Create • Store • View • Search • Manage Journal Entries**

⭐ Explore • Learn • Code • Improve

[⬆ Back to Top](#-personal-journal-manager)

</div>
