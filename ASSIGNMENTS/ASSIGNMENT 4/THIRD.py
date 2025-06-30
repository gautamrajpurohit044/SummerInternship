import sqlite3

while True:
    choice = int(input('''Enter your choice:
    1. Create a new database
    2. Create a new table
    3. Insert data into the table
    4. Display data from the table
    5. Update data in the table
    6. Delete data from the table
    7. Exit
Your choice: '''))

    if choice == 1:
        db_name = input("Enter the name of the database: ")
        conn = sqlite3.connect(db_name + '.db')
        print(f"Database '{db_name}.db' created successfully.")
        conn.close()

    elif choice == 2:
        db_name = input("Enter the name of the database: ")
        conn = sqlite3.connect(db_name + '.db')
        cursor = conn.cursor()
        table_name = input("Enter the name of the table: ")
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            age INTEGER NOT NULL,
                            city TEXT NOT NULL)''')
        print(f"Table '{table_name}' created successfully in '{db_name}.db'.")
        conn.commit()
        conn.close()

    elif choice == 3:
        db_name = input("Enter the name of the database: ")
        conn = sqlite3.connect(db_name + '.db')
        cursor = conn.cursor()
        table_name = input("Enter the name of the table: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        city = input("Enter city: ")
        cursor.execute(f"INSERT INTO {table_name} (name, age, city) VALUES (?, ?, ?)", (name, age, city))
        print(f"Data inserted successfully into '{table_name}' in '{db_name}.db'.")
        conn.commit()
        conn.close()

    elif choice == 4:
        db_name = input("Enter the name of the database: ")
        conn = sqlite3.connect(db_name + '.db')
        cursor = conn.cursor()
        table_name = input("Enter the name of the table: ")
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        print(f"Data from '{table_name}' in '{db_name}.db':")
        for row in rows:
            print(row)
        conn.close()

    elif choice == 5:
        db_name = input("Enter the name of the database: ")
        conn = sqlite3.connect(db_name + '.db')
        cursor = conn.cursor()
        table_name = input("Enter the name of the table: ")
        id_to_update = int(input("Enter the ID of the record to update: "))
        new_name = input("Enter new name: ")
        new_age = int(input("Enter new age: "))
        new_city = input("Enter new city: ")
        cursor.execute(f"UPDATE {table_name} SET name=?, age=?, city=? WHERE id=?",
                       (new_name, new_age, new_city, id_to_update))
        print(f"Data updated successfully in '{table_name}' in '{db_name}.db'.")
        conn.commit()
        conn.close()

    elif choice == 6:
        db_name = input("Enter the name of the database: ")
        conn = sqlite3.connect(db_name + '.db')
        cursor = conn.cursor()
        table_name = input("Enter the name of the table: ")
        id_to_delete = int(input("Enter the ID of the record to delete: "))
        cursor.execute(f"DELETE FROM {table_name} WHERE id=?", (id_to_delete,))
        print(f"Data deleted successfully from '{table_name}' in '{db_name}.db'.")
        conn.commit()
        conn.close()

    elif choice == 7:
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
