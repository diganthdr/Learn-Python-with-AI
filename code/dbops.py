import sqlite3

# Function to connect to the database
def connect_to_db(db_name):
    connection = sqlite3.connect(db_name)
    return connection

# Function to create a table
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    connection.commit()

# Function to insert a record
def insert_user(connection, name, age, email):
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO users (name, age, email)
        VALUES (?, ?, ?)
    ''', (name, age, email))
    connection.commit()

# Function to fetch all records
def fetch_all_users(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

# Function to update a record
def update_user(connection, user_id, name=None, age=None, email=None):
    cursor = connection.cursor()
    query = 'UPDATE users SET '
    params = []
    if name:
        query += 'name = ?, '
        params.append(name)
    if age:
        query += 'age = ?, '
        params.append(age)
    if email:
        query += 'email = ?, '
        params.append(email)
    query = query.rstrip(', ') + ' WHERE id = ?'
    params.append(user_id)
    print("Executing query:", query)
    cursor.execute(query, tuple(params))
    connection.commit()

# Function to delete a record
def delete_user(connection, user_id):
    cursor = connection.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    connection.commit()

# Example usage
if __name__ == "__main__":
    db_name = "example.db"
    conn = connect_to_db(db_name)
    create_table(conn)

    # Insert a user
    insert_user(conn, "Alice", 30, "alice@example.com")

    # Fetch all users
    users = fetch_all_users(conn)
    print("Users:", users)

    # Update a user
    update_user(conn, 1, name="Alice Smith")

    # Delete a user
    delete_user(conn, 1)

    conn.close()