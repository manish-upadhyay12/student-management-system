# Student Management System

A Python-based Student Management System that uses CSV files to store and manage student records. This project demonstrates file handling, CSV operations, CRUD functionality, exception handling, and basic data management concepts.

## Features

* Create a new student data file
* Add student records
* Search student by roll number
* Search student by name
* Display all student records
* Update existing student information
* Delete a specific student record
* Delete an entire file
* Input validation using exception handling

## Technologies Used

* Python
* CSV Module
* Pathlib Module

## Student Data Fields

Each student record contains:

* Name
* Father Name
* Age
* Roll Number
* College
* Phone Number
* Village

## Project Structure

```text
student-management-system/
│
├── student_managment_system.py
└── README.md
```

## How to Run

1. Clone the repository

```bash
git clone https://github.com/manish-upadhyay12/student-managment-system.git
```

2. Move into the project directory

```bash
cd student-managment-system
```

3. Run the program

```bash
python student_managment_system.py
```

## Concepts Practiced

* Functions
* Loops
* Conditional Statements
* Exception Handling
* File Handling
* CSV Reading and Writing
* CRUD Operations
* Path Management using Pathlib

## Future Improvements

* OOP Version
* Duplicate Roll Number Validation
* Better User Interface
* Export Data to Excel
* Data Sorting and Filtering
* Pandas Integration

## Author

Manish Upadhyay

B.Tech CSE (Data Science & Artificial Intelligence)

Learning Python, Data Analytics, and Artificial Intelligence.


# knowledgeable information
# 👉 csv.writer(file) ek writer object (tool / pen) banata hai
# 👉 Ye object directly file me kuch nahi likhta
# 👉 Ye sirf writing capability deta hai
# csv.writer()= file me structured data likhne ke liye hota hai
# writerow() =ek single row likhta hai
# newline="" =extra blank lines stop karta hai
# "w" mode= file ko overwrite karta hai
# csv module =import karna mandatory hai
# with open("student.csv","w",newline ="") as file:
#     data = csv.writer(file)
#     data.writerow(["a",10])
