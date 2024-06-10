import sqlite3
# Create a database using the imported sqlite3 module
try:
    db = sqlite3.connect('my_db.db')
# Create a table called python_programming
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
                   ''')
    db.commit()
# Insert the following new rows into the python_programming table
    grades = [(55, 'Carl Davis', 61), (66, 'Dennis Fredrickson', 88), (77,
        'Jane Richards', 78), (12, 'Peyton Sawyer', 45), (2, 'Lucas Brooke', 9)]
    cursor.executemany('''
                   INSERT INTO python_programming(id,name,grade) VALUES(?,?,?)
                   ''', (grades))
    db.commit()
# Select all records with a grade between 60 and 80
    min_grade = 60
    max_grade = 80
    cursor.execute('''
                   SELECT * FROM python_programming where grade between ? and ?
                   ''', (min_grade, max_grade))
    for row in cursor:
        print('{0} , {1} , {2}'.format(row[0], row[1], row[2]))
# Change Carl Davis’s grade to 65
    name = 'Carl Davis'
    new_grade = 65
    cursor.execute('''
                   UPDATE python_programming set grade = ? WHERE name = ?     
                   ''', (new_grade, name))
    db.commit()
# Delete Dennis Fredrickson’s row
    name = 'Dennis Fredrickson'
    cursor.execute('''
                   DELETE FROM python_programming WHERE name = ?
                   ''', (name,))
    db.commit()
# Change the grade of all students with an id greater than 55 to a grade of 80.
    id = 55
    new_grade = 80
    cursor.execute('''
                   UPDATE python_programming set grade = ? WHERE id > ?     
                   ''', (new_grade, id))
    db.commit()
# ○ Include a screenshot in your submission showing the
# python_programming table contents in the DB Browser for SQLite.

except Exception as e:
    raise e
finally:
    # Close the db connection
    db.close()
