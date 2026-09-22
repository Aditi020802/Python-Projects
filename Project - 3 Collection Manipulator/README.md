<div align="center">

# 🎓 ✨ Student Data Organizer ✨

### **P-2 Data Structure & Control Flow Project**

<p>
  <strong>A Python console application for managing student information using lists, dictionaries, sets, loops, pattern matching, and user-defined data operations.</strong>
</p>

<br>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Level-Beginner-2EA44F?style=for-the-badge" alt="Beginner">
  <img src="https://img.shields.io/badge/Type-Console%20Application-6F42C1?style=for-the-badge" alt="Console Application">
  <img src="https://img.shields.io/badge/Data%20Structure-List%20%7C%20Dictionary%20%7C%20Set-FF9800?style=for-the-badge" alt="Data Structures">
</p>

<br>

🚀 <a href="#-quick-start">Quick Start</a>
&nbsp; • &nbsp;
✨ <a href="#-features">Features</a>
&nbsp; • &nbsp;
🧠 <a href="#-python-concepts">Python Concepts</a>
&nbsp; • &nbsp;
🏗️ <a href="#-architecture">Architecture</a>
&nbsp; • &nbsp;
📸 <a href="#-project-preview">Preview</a>

</div>

---

# 🌟 About The Project

> [!NOTE]
> ### 💡 The Core Concept
>
> **Student Data Organizer** is an interactive Python console application designed to manage student information.
>
> The application allows users to **add, display, update, delete, and organize student records** through a simple menu-driven interface.
>
> Student information is stored using a **list of dictionaries**, while subjects are stored using a **set** to demonstrate unique-value handling.

The project combines several important Python fundamentals:

```text
👤 User Input
      ↓
📦 List
      ↓
📖 Dictionary
      ↓
🔢 Set
      ↓
🔄 Loops
      ↓
🎯 match-case
      ↓
🛠️ CRUD Operations
      ↓
🖥️ Console Output
```

---

# ✨ Features

<table width="100%">
<tr>
<th align="center">Option</th>
<th align="left">Feature</th>
<th align="left">Description</th>
</tr>

<tr>
<td align="center">1️⃣</td>
<td><b>Add Student</b></td>
<td>Adds a new student with complete personal and academic information.</td>
</tr>

<tr>
<td align="center">2️⃣</td>
<td><b>Display All Students</b></td>
<td>Displays all students currently stored in the application.</td>
</tr>

<tr>
<td align="center">3️⃣</td>
<td><b>Update Student</b></td>
<td>Updates name, age, email, phone, grade, and city using Student ID.</td>
</tr>

<tr>
<td align="center">4️⃣</td>
<td><b>Delete Student</b></td>
<td>Deletes a student record using Student ID.</td>
</tr>

<tr>
<td align="center">5️⃣</td>
<td><b>Display Subjects</b></td>
<td>Collects and displays all unique subjects offered by students.</td>
</tr>

<tr>
<td align="center">6️⃣</td>
<td><b>Exit</b></td>
<td>Terminates the Student Data Organizer.</td>
</tr>
</table>

---

# 📋 Student Information

Each student record contains:

| Field | Python Type | Example |
| :--- | :---: | :--- |
| 🆔 Student ID | `int` | `101` |
| 👤 Name | `str` | `"Sujal"` |
| 🎂 Age | `int` | `21` |
| 🎓 Grade | `str` | `"A"` |
| 📅 Date of Birth | `str` | `"2005-08-15"` |
| 📧 Email | `str` | `"student@gmail.com"` |
| 📱 Phone | `str` | `"9876543210"` |
| 🏙️ City | `str` | `"Ahmedabad"` |
| 📚 Subjects | `set` | `{"Python", "Math"}` |

---

# 🧠 Python Concepts

## 01 — List

The main student collection is created using a list:

```python id="5s5b7g"
students = []
```

Every student dictionary is added to this list:

```python id="2y8a3k"
students.append(student)
```

The list allows multiple student records to be stored together.

---

## 02 — Dictionary

Each student is represented using a dictionary:

```python id="ycbm9e"
student = {
    "id": student_id,
    "name": name,
    "age": age,
    "dob": dob,
    "email": email,
    "phone": phone,
    "grade": grade,
    "city": city,
    "subjects": subjects
}
```

This makes each student's information easy to organize using key-value pairs.

---

## 03 — Set

Subjects are stored as a set:

```python id="9v7c0q"
subjects = set(subject_input.split(","))
```

A set is useful because it stores **unique values**.

The program also creates a set containing all subjects:

```python id="h1c5q9"
all_subjects = set()
```

Then subjects are combined using:

```python id="m9i1xw"
all_subjects.update(student["subjects"])
```

---

## 04 — `while` Loop

The main menu continuously runs using:

```python id="2t0j4b"
while True:
```

The application continues until the user selects option `6`.

---

## 05 — `match-case`

The menu choices are handled using Python's `match-case` statement:

```python id="7o8j2k"
match chioce:
    case 1:
        # Add Student

    case 2:
        # Display Students

    case 3:
        # Update Student

    case 4:
        # Delete Student

    case 5:
        # Display Subjects

    case 6:
        # Exit

    case _:
        # Invalid Choice
```

---

## 06 — `for` Loop

The program uses loops to search and display student records.

Example:

```python id="5e8b7k"
for student in students:
    print(student["name"])
```

---

## 07 — `len()`

The program checks whether students exist:

```python id="w7y2j9"
if len(students) == 0:
    print("No student found.")
```

It is also used while deleting a student:

```python id="1l8g6q"
for i in range(len(students)):
```

---

## 08 — `append()`

Adds a new student to the list:

```python id="9o0x7k"
students.append(student)
```

---

## 09 — `pop()`

Deletes a student from the list:

```python id="q2t4v8"
students.pop(i)
```

---

## 10 — `set.update()`

Combines subjects from multiple students:

```python id="m3q6s8"
all_subjects.update(student["subjects"])
```

This allows the program to display a combined collection of subjects.

---

# 🏗️ Architecture

The application follows a simple menu-driven architecture.

<table width="100%">
<tr>
<td width="30%"><b>📦 Data Storage</b></td>
<td>Student records are stored inside a list.</td>
</tr>

<tr>
<td><b>📖 Student Record</b></td>
<td>Each student is represented by a dictionary.</td>
</tr>

<tr>
<td><b>📚 Subjects</b></td>
<td>Subjects are stored using a set to maintain unique values.</td>
</tr>

<tr>
<td><b>🎛️ Menu System</b></td>
<td>A continuous while loop provides the main application menu.</td>
</tr>

<tr>
<td><b>🎯 Control Flow</b></td>
<td>Python match-case handles each menu selection.</td>
</tr>

<tr>
<td><b>🛠️ CRUD</b></td>
<td>Add, display, update, and delete operations manage student records.</td>
</tr>
</table>

---

# 🔄 Program Flow

<div align="center">

```text
                    🚀 START
                       │
                       ▼
             ┌──────────────────┐
             │  Welcome Message │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │   Display Menu   │
             └────────┬─────────┘
                      │
                      ▼
                👤 User Choice
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
       OPTION 1    OPTION 2    OPTION 3
       Add         Display      Update
          │           │           │
          └───────────┼───────────┘
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
       OPTION 4    OPTION 5    OPTION 6
       Delete      Subjects      Exit
          │           │           │
          └───────────┼───────────┘
                      │
                      ▼
               🔄 Show Menu Again
```

</div>

---

# 💻 Project Preview

## 🖥️ Main Menu

```text
-------------------------------------------
Welcome to the Student Data Organizer!
-------------------------------------------

Selact an option:
1. Add Student
2. Disply All Student
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice::
```

---

# ➕ Add Student

Select option `1`:

```text
---------------------------
student ID:101
Name : Sujal
Age : 21
Grade : A
Date of Birth (YYYY-MM-DD) :2005-01-15
Email : sujal@gmail.com
Phone number : 9876543210
City name : Ahmedabad
Subjects (Comma-separated) : Python,Math,English

Student added successfully!
------------------------------
```

The information is stored as:

```python id="9m4w8v"
{
    "id": 101,
    "name": "Sujal",
    "age": 21,
    "grade": "A",
    "dob": "2005-01-15",
    "email": "sujal@gmail.com",
    "phone": "9876543210",
    "city": "Ahmedabad",
    "subjects": {
        "Python",
        "Math",
        "English"
    }
}
```

---

# 👀 Display All Students

Select option `2`:

```text
----- All Students -----

------*------*------*------
Student ID:: 101
Name :: Sujal
Age :: 21
Grade :: A
Date of Birth :: 2005-01-15
Subject :: {'Python', 'Math', 'English'}
Email :: sujal@gmail.com
Phone :: 9876543210
City :: Ahmedabad
------*------*------*------
```

If no students exist:

```text
----- All Students -----

No student found.
```

---

# ✏️ Update Student

Select option `3`:

```text
*-----*-----*-----*-----*

---- Update Student ----

Enter Student ID to update :101

Student Found!

Enter New Name : Sujal Patel
Enter New Age : 22
Enter New Email : sujalpatel@gmail.com
Enter New Phone : 9876543210
Enter New Grade : A+
Enter New City : Gandhinagar

student updated successfully!
```

The program searches for the matching Student ID and updates:

```text
👤 Name
🎂 Age
📧 Email
📱 Phone
🎓 Grade
🏙️ City
```

---

# 🗑️ Delete Student

Select option `4`:

```text
===========================

--- Delete Student ---

Enter Student ID to delete: 101

Student deleted successfully!

============================
```

If the ID does not exist:

```text
Student not found.
```

---

# 📚 Display Subjects Offered

Select option `5`:

```text
--- All Subjects Offered ---

Python
Math
English
Science
```

The application collects subjects from all students and combines them into one unique set.

---

# 🚪 Exit

Select option `6`:

```text
**---**---**---**---**---**---**---**
Thank you for using the Student Data Organizer!
**---**---**---**---**---**---**---**
```

---

# 📊 Data Structure Design

<div align="center">

```text
students
   │
   ├── Student 1
   │     ├── id
   │     ├── name
   │     ├── age
   │     ├── dob
   │     ├── email
   │     ├── phone
   │     ├── grade
   │     ├── city
   │     └── subjects → SET
   │
   ├── Student 2
   │     ├── id
   │     ├── name
   │     ├── age
   │     └── ...
   │
   └── Student 3
         ├── id
         ├── name
         ├── age
         └── ...

```

</div>

### Structure

```text
List
 └── Dictionary
       ├── String
       ├── Integer
       ├── String
       ├── String
       ├── String
       ├── String
       ├── String
       └── Set
            ├── Subject 1
            ├── Subject 2
            └── Subject 3
```

---

# 🔁 CRUD Operations

The project demonstrates the basic CRUD pattern:

| Operation | Menu | Python Method |
| :--- | :---: | :--- |
| ➕ Create | `1` | `append()` |
| 👀 Read | `2` | `for` loop |
| ✏️ Update | `3` | Dictionary assignment |
| 🗑️ Delete | `4` | `pop()` |

Option `5` provides additional subject aggregation functionality.

---

# 📁 Project Structure

```text
📦 Student-Data-Organizer
│
├── 🐍 main.py
├── 📘 README.md
│
└── 📂 assets
    ├── 🖼️ Output.png
    └── 🎥 Project Demonstration.mp4
```

### 📄 File Description

| File | Purpose |
| :--- | :--- |
| `main.py` | Main Student Data Organizer program |
| `README.md` | Project documentation |
| `assets/Output.png` | Console output screenshot |
| `assets/Project Demonstration.mp4` | Project demonstration video |

---

# 📸 Project Preview

<div align="center">

### 🖥️ Console Output

<br>

<img src="https://github.com/Aditi020802/Python-Projects/blob/main/Project%20-%203%20Collection%20Manipulator/Output/output1.jpeg" alt="Student Data Organizer Output" width="95%">
<img src="https://github.com/Aditi020802/Python-Projects/blob/main/Project%20-%203%20Collection%20Manipulator/Output/output2.jpeg" alt="Student Data Organizer Output" width="95%">
<img src="https://github.com/Aditi020802/Python-Projects/blob/main/Project%20-%203%20Collection%20Manipulator/Output/output3.jpeg" alt="Student Data Organizer Output" width="95%">
<img src="https://github.com/Aditi020802/Python-Projects/blob/main/Project%20-%203%20Collection%20Manipulator/Output/output4.jpeg" alt="Student Data Organizer Output" width="95%">
<img src="https://github.com/Aditi020802/Python-Projects/blob/main/Project%20-%203%20Collection%20Manipulator/Output/output5.jpeg" alt="Student Data Organizer Output" width="95%">
<img src="https://github.com/Aditi020802/Python-Projects/blob/main/Project%20-%203%20Collection%20Manipulator/Output/output6.jpeg" alt="Student Data Organizer Output" width="95%">

<br><br>

📷 **Student Data Organizer console output**

</div>

---

# 🎥 Project Demonstration

<div align="center">

### ▶️ Watch The Project In Action

**[🎬 Open Project Demonstration](https://github.com/Aditi020802/Python-Projects/blob/main/Project%20-%203%20Collection%20Manipulator/Project%20Demonstration.mp4)**

<br>

</div>

> [!TIP]
> If GitHub does not preview the MP4 directly, click the demonstration link to open the video file.

---

# 🚀 How To Run

## Step 1 — Install Python

Install **Python 3.x** on your computer.

Check installation:

```bash
python --version
```

---

## Step 2 — Open The Project

Open the project using:

```text
VS Code
PyCharm
IDLE
Any Python-supported IDE
```

---

## Step 3 — Open Terminal

Navigate to the project directory:

```bash
cd Student-Data-Organizer
```

---

## Step 4 — Run The Program

```bash
python main.py
```

---

# 📦 Dependencies

This project does not require any external packages.

```text
🐍 Python 3.x
📦 External Packages → None
🗄️ Database → None
🌐 API → None
```

The project uses Python's built-in functionality.

---

# ⚠️ Current Implementation Notes

The current version is intentionally focused on Python fundamentals.

### 🔹 In-memory Storage

Student records are stored in:

```python id="zj2g8d"
students = []
```

Therefore, all student data is lost when the program exits.

### 🔹 Subject Input

Subjects are entered as comma-separated values:

```text
Python,Math,English
```

The program converts them into a set:

```python id="1yq3kj"
subjects = set(subject_input.split(","))
```

### 🔹 Update Age

The original program accepts the new age using:

```python id="2q3p7n"
new_age = input("Enter New Age :")
```

Therefore, the updated age is stored as a **string**, unlike the original age which is stored as an integer.

---

# 🔮 Future Improvements

Possible improvements for the next version:

- [ ] Prevent duplicate Student IDs
- [ ] Add input validation
- [ ] Add `try-except` error handling
- [ ] Validate email addresses
- [ ] Validate phone numbers
- [ ] Validate date of birth
- [ ] Keep updated age as an integer
- [ ] Add search student option
- [ ] Add sorting students
- [ ] Save data to a file
- [ ] Add JSON storage
- [ ] Add CSV support
- [ ] Add SQLite database
- [ ] Add GUI using Tkinter
- [ ] Add login/authentication
- [ ] Add student statistics

---

# 📊 Project Snapshot

<div align="center">

<table width="100%">

<tr>

<td align="center" width="33%">

### 🏷️ PROJECT

**P-2 Data Structure & Control Flow**

</td>

<td align="center" width="33%">

### 🐍 LANGUAGE

**Python 3.x**

</td>

<td align="center" width="33%">

### 📊 LEVEL

**Beginner**

</td>

</tr>

<tr>

<td align="center">

### 💻 TYPE

**Console Application**

</td>

<td align="center">

### 📦 DEPENDENCIES

**None**

</td>

<td align="center">

### 🗂️ STORAGE

**In-Memory**

</td>

</tr>

</table>

</div>

---

# 🎯 Key Takeaway

<div align="center">

### 👤 Input
⬇️  
### 📦 Dictionary
⬇️  
### 📋 List
⬇️  
### 🔢 Set
⬇️  
### 🔄 Control Flow
⬇️  
### 🛠️ CRUD Operations
⬇️  
### 🖥️ Output

</div>

The project provides practical experience with **Python lists, dictionaries, sets, loops, `match-case`, conditional statements, user input, CRUD operations, and basic data organization**.

---

# 🤝 Contributing

This project is created for learning and practicing Python programming.

To contribute:

```bash
# Create a new branch
git checkout -b feature/new-feature

# Make your changes

# Commit changes
git commit -m "feat: improve student organizer"

# Push your branch
git push origin feature/new-feature
```

Then create a Pull Request.

---

# 📄 License

This project is distributed under the **MIT License**.

---

<div align="center">

# 🎓 Student Data Organizer

### **Python • Lists • Dictionaries • Sets • Loops • Match-Case • CRUD**

<br>

## 👩‍💻 Completed By

# **Aditi Modhvadia**

<br>

⭐ **Explore • Learn • Code • Improve**

<br>

### Thanks For Visiting! ❤️

<br>

[🔼 Back to Top](#-student-data-organizer)

</div>
