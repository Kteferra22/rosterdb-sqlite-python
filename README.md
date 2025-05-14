📋 Roster Database Manager

This Python script reads a JSON file containing course roster data and stores it in a normalized SQLite database. It creates a many-to-many relationship between users and courses, with a Member table tracking each user's role in the course.

🔧 Features
1. Parses a JSON file with course roster data.

2. Creates and populates three related tables in SQLite:
-  User: stores unique user names.
-  Course: stores unique course titles.
-  Member: creates relationships between users and courses, with role information.

3. Outputs a selection of joined data.

4. Generates a checksum using the joined data.

📁 File Structure

rosterdb.sqlite         #Generated SQLite database

roster_data.json        #Input data file (must be present)

roster_script.py        #Main script file

🧪 Example JSON Input (roster_data.json)
[
    
    ["Alice", "Python", 1],
    ["Bob", "Python", 0],
    ["Alice", "SQL", 0]
]


🚀 Getting Started
Prerequisites
1. Python 3.x installed
2. JSON data file named roster_data.json in the same directory

Running the Script
python roster_script.py

🗃️ Database Schema

User(id INTEGER PRIMARY KEY, name TEXT UNIQUE)

Course(id INTEGER PRIMARY KEY, title TEXT UNIQUE)

Member(user_id INTEGER, course_id INTEGER, role INTEGER, PRIMARY KEY (user_id, course_id))

🧩 Sample Output
[

['Alice', 'Python', 1],

['Alice', 'SQL', 0],

[Checksum: XYZZY<...>]

]
📌 Notes
1. The script will overwrite rosterdb.sqlite if it exists.

2. Only the first two entries (ordered by user name and course title) are printed.

3. The Checksum is a string generated from concatenated and hex-encoded data.
