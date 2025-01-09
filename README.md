#Student Records Management System
This project is a simple student records management system that allows users to manage student records by performing operations such as adding, updating, removing, searching, and sorting student information. The system provides a menu-driven interface where each student's details are stored as a list, and a series of validations ensure that all input is correct.

Features
Add Student: Add a new student record with required information.
Update Student: Update a student's record either by their ID or name.
Remove Student: Remove a student's record by their ID.
Search Student: Search for a student by first or last name.
Sort Student Records: Sort records by ID, first name, last name, or city.
Print Report: Generate a report of sorted student records.
Exit: Exit the program.
Installation
Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/yourusername/student-records-management.git
Navigate to the project directory:

bash
Copy code
cd student-records-management
Run the program:

bash
Copy code
python student_records.py
Make sure you have Python installed on your system.

Usage
Upon running the program, the following menu will appear:

mathematica
Copy code
1. Student_Record
2. Add
3. Update
4. Remove
5. Search
6. Print Report
7. Exit
Add Student
Enter the student's 5-digit ID, name, address, city, state, zip code, and phone number.
Update Student
Update a student's record by entering their ID or name.
Remove Student
Remove a student's record by entering their 5-digit ID.
Search Student
Search for a student by typing their first or last name.
Sort Records
Sort student records by ID, first name, last name, or city.
Print Report
Generate a sorted report based on your choice.
Example
Menu Example:
mathematica
Copy code
1. Student_Record
2. Add
3. Update
4. Remove
5. Search
6. Print Report
7. Exit
Selecting Option 2 will prompt you to enter details for a new student.
Selecting Option 6 will allow you to generate a report sorted by ID, First Name, Last Name, or City.
Validations
The system validates the following:

Student ID must be a 5-digit number.
Names (first and last) must be 15 characters or less.
Street number must be valid.
City name should be no more than 15 characters.
State should be a 2-letter abbreviation.
Zip code should be a 5-digit number.
Phone number must be a 10-digit number.
Future Enhancements
Implement database support for better data storage.
Add user authentication to restrict access to the system.
Improve the user interface for better usability.
