import json #import json features 
import sqlite3 #import sqlite features 

roster_db = sqlite3.connect('rosterdb.sqlite')
cursor_for_db = roster_db.cursor()

# Do some setup
cursor_for_db.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER PRIMARY KEY,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER PRIMARY KEY,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

with open('roster_data.json') as file:
    str_data = file.read()

json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]


    cursor_for_db.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', (name,))
    cursor_for_db.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = cursor_for_db.fetchone()[0]

    cursor_for_db.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', (title,))
    cursor_for_db.execute('SELECT id FROM Course WHERE title = ? ', (title,))
    course_id = cursor_for_db.fetchone()[0]

    cursor_for_db.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ?)''',
        (user_id, course_id, role))
    

roster_db.commit()

cursor_for_db.execute('''SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name, Course.title, Member.role DESC LIMIT 2'''
)

rows = cursor_for_db.fetchall()

for row in rows:
    print(row)

cursor_for_db.execute('''
    SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;'''                   
)

result = cursor_for_db.fetchone()

print("Checksum:", result[0])

roster_db.close()