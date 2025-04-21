#CourseTracker
# Define the three tracks
track_1 = "Computer Science"
track_2 = "Information Technology"
track_3 = "Cyber Security"

# Create dictionaries to store student data for each track
CompScience_students = {}
InfoTech_students = {}
CyberSecur_students = {}

# Example variables for tracking courses and students
courses_CompScience = ["Physics", "Chemistry", "Biology"]
courses_InfoTech = ["History", "Literature", "Philosophy"]
courses_CyberSecur = ["Accounting", "Economics", "Business Studies"]

# Example student data structure
# Each student will have a name, ID, and a list of enrolled courses
student_template = {
    "name": "",
    "id": "",
    "enrolled_courses": []
}

# Example usage
# Adding a student to the Science track
CompScience_students["S001"] = {
    "name": "Alice",
    "id": "S001",
    "enrolled_courses": ["Physics", "Biology"]
}

# Adding a student to the Arts track
InfoTech_students["A001"] = {
    "name": "Bob",
    "id": "A001",
    "enrolled_courses": ["History", "Philosophy"]
}

# Adding a student to the Commerce track
CyberSecur_students["C001"] = {
    "name": "Charlie",
    "id": "C001",
    "enrolled_courses": ["Accounting", "Economics"]
}