# Student Records Management System

The **Student Records Management System** is a Python-based program designed to manage student records in a simple, user-friendly interface. Users can add, update, remove, search, and sort student records, ensuring that all the details are correctly validated before being processed.

The system stores student data such as ID, name, address, city, state, zip code, and phone number in a list of lists. The program provides a series of menu options that allow users to interact with and manage the student records.

## Features

- **Add Student**: Add new student records with validation checks for all input fields.
- **Update Student**: Update student records by ID or by first and last name.
- **Remove Student**: Remove a student record using their ID.
- **Search Student**: Search for students by first name or last name.
- **Sort Records**: Sort student records by ID, first name, last name, or city.
- **Print Report**: Generate a sorted report of student records based on user preference.
- **Exit**: Exit the program.

## Validations

The program ensures that all user inputs are correctly validated:
- **Student ID**: 5 digits only.
- **Name**: First and last name must not exceed 15 characters each and must be entered with a space between them.
- **Street Address**: Must be a valid street number.
- **City**: Maximum of 15 characters.
- **State**: Must be a 2-letter abbreviation.
- **Zip Code**: Must be exactly 5 digits.
- **Phone Number**: Must be exactly 10 digits.
