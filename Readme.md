## 📚 University Course Registration Management System

Welcome to the University Course Registration Management System, a mini-project designed to simplify the process of course registration and management at universities, similar to the system used at the University of Tripoli! 🎓 This system is built using Python and provides a range of functionalities for students, faculty members, and registrars to manage courses, grades, and schedules. 🚀

# 🗂️ Table of Contents

Project Overview
Setup and Running the Project
Functionalities
Registrar Functionalities
Student Functionalities
Faculty Member Functionalities
Data Management
Code Structure and Functions
Future Enhancements
🔍 Project Overview
The system includes three main types of users:

**Registrar 🧑‍💼**: Manages students, faculty members, and course schedules.
**Student 👨‍🎓**: Registers for courses, views their academic records, and checks schedules.
**Faculty Member 👩‍🏫**: Views assigned courses, manages student grades, and checks schedules.
Each user has their own set of functionalities managed through a simple and easy-to-use menu-based system. 🗒️

⚙️ Setup and Running the Project
To set up and run the project:

Ensure you have Python installed on your system. 🐍
Download or clone the project files.
Make sure the JSON files (students.json, faculty_members.json, schedules.json, courses.json) are in the same directory as the Python script. If these files do not exist, the program will create them automatically.
Run the Python script:
bash
Copy code
python university_management.py
📌 The program will start with a login screen where you can choose the type of user (Registrar, Student, or Faculty Member) and perform the respective actions.

**🛠️ Functionalities**

# **Registrar Functionalities 🧑‍💼**

After logging in as a registrar, the following options are available:

**Manage Students**: Add new students, search for existing students, and manage their courses.

**Manage Faculty Members**: Add new faculty members, assign courses, change passwords, and remove courses from faculty members.
View Registered Students for a Course: Display a list of students registered in a specific course.

**Assign Grades for Courses**: Set grades for students in registered courses.

**Display Lecture and Exam Schedules**: View schedules for all lectures and exams.

**Logout**: Return to the main menu.

# **Student Functionalities 👨‍🎓**

After logging in as a student, the following options are available:

**View Completed Semesters with GPA**: Display all completed semesters with courses, grades, and GPA.

**Manage Registered Courses**: Add or remove courses for the current semester, ensuring all prerequisites and co-requisites are met.

**View Lecture and Exam Schedules**: View the schedule of lectures and exams for registered courses.

**Logout**: Return to the main menu.

# **Faculty Member Functionalities 👩‍🏫**

After logging in as a faculty member, the following options are available:

**View List of Students in a Course**: Display a list of students registered in a specific course taught by the faculty member.

**Add Grades for Students in a Course**: Assign grades to students in courses they teach.

**View Lecture and Exam Schedules**: View the schedule for lectures and exams for assigned courses.

**Logout**: Return to the main menu.

# 📂 Data Management

Data is managed through JSON files:

students.json: Stores student information including courses, grades, and academic records.
faculty_members.json: Stores faculty member information including assigned courses and login credentials.
schedules.json: Stores lecture and exam schedules.
courses.json: Stores course information including prerequisites, corequisites, and credits.
📝 The system reads from these files at startup and writes back any changes when saving data.

# 🧩 Code Structure and Functions

# 1. Data Loading and Saving

load_data(): Loads data from JSON files for students, faculty members, schedules, and courses.
save_data(): Saves the current data state to the JSON files.

# 2. User Authentication and Menus

login(): Main login function that allows users to choose their role (Registrar, Student, Faculty Member) and logs them in.
registrar_login(): Authenticates the registrar using a predefined username and password.
student_menu(): Displays the menu options for students.
faculty_menu(): Displays the menu options for faculty members.

# 3. Registrar Functions

registrar_menu(): Displays the registrar's menu and handles input choices.
manage_student(), add_new_student(), search_student(): Functions to manage student data.
manage_faculty(), add_new_faculty_member(), search_faculty_member(): Functions to manage faculty data.
assign_grades(): Allows the registrar to assign grades to students.
create_schedule(), create_lecture_schedule(), create_exam_schedule(): Functions to manage lecture and exam schedules.

# 4. Student Functions

manage_student_courses(), open_new_semester_for_student(), delete_and_add_courses_for_student(): Functions for managing student courses.
display_completed_semesters_with_gpa(): Displays the completed semesters with grades and GPA calculation.
display_schedule(): Displays the schedule for lectures and exams.

# 5. Faculty Member Functions

faculty_options(), display_students_in_course(), add_grades_for_course(): Functions for managing courses and grades for faculty members.

# 6. Utility Functions

calculate_grade_label(grade): Converts a numerical grade to a grade label (e.g., "Excellent", "Very Good").
check_prerequisites(student_id, course_code), check_corequisites(student_id, course_code): Checks if a student meets the prerequisites and corequisites for a course.

# **🌟 Future Enhancements**

🖥️ Implement a User Interface (UI) to make the system more user-friendly.

📊 Add more functionalities like notifications, detailed reports, and data analytics.

🛡️ Improve error handling and input validation throughout the system.

🔐 Implement role-based access controls for more secure data management.
This README provides a clear overview of the project, its structure, functionalities, and future enhancement ideas. The project is designed to be simple yet powerful, catering to the needs of a university's course registration system. 🎉