from flask import Flask, jsonify
import pandas as pd
from src.config import db_engine


# Initialize the Flask app
app = Flask(__name__)

# Define the route for the API
@app.route('/read/first-chunck', methods=['GET'])
def read_first_chunck():
    if not db_engine:
        return jsonify({"error": "Failed to connect to database"}), 500

    try:
        df = pd.read_sql_query('SELECT * FROM fashion LIMIT 10', db_engine)
        data = df.to_dict(orient='records')
        return jsonify(data), 200
    except Exception as e:
        print(f"Error reading data: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
