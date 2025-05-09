from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
import logging
import os

app = Flask(__name__, static_folder='.', static_url_path='')

# Enable CORS for the Flask app with specific configurations
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Database setup
DB_NAME = "subscribers.db"

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("apiserver.log"),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)

def init_db():
    """Initialize the SQLite database and create the subscribers table if it doesn't exist."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                emailid TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()
        conn.close()
        logging.info("Database initialized successfully.")
    except Exception as e:
        logging.error(f"Error initializing database: {e}")

# Serve the index.html file
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# Serve other static files
@app.route('/<path:path>')
def serve_static_files(path):
    if os.path.exists(path):
        return send_from_directory('.', path)
    return jsonify({"error": "File not found"}), 404

# Endpoint to subscribe
@app.route('/api/v1/subscribe', methods=['POST'])
def subscribe():
    """API endpoint to add a subscriber."""
    data = request.get_json()
    logging.debug(f"Received data: {data}")

    # Validate input
    if not data or 'name' not in data or 'emailid' not in data:
        logging.warning("Invalid input received.")
        return jsonify({"error": "Invalid input. 'name' and 'emailid' are required."}), 400

    name = data['name']
    emailid = data['emailid']

    try:
        # Insert subscriber into the database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO subscribers (name, emailid) VALUES (?, ?)', (name, emailid))
        conn.commit()
        conn.close()

        logging.info(f"Subscriber added successfully: {name}, {emailid}")
        return jsonify({"message": "Subscriber added successfully!"}), 201
    except sqlite3.IntegrityError:
        logging.warning(f"Duplicate email ID: {emailid}")
        return jsonify({"error": "Email ID already exists."}), 409
    except Exception as e:
        logging.error(f"Error adding subscriber: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Initialize the database
    logging.info("Starting the application...")
    init_db()

    # Run the Flask app
    logging.info("Running the Flask app...")
    app.run(debug=True, host='0.0.0.0', port=5000)