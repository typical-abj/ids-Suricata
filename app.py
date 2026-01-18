from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)

# Set the paths for your Suricata log files
log_file_path = "/var/log/suricata/fast.log"  # Modify with your actual log file path
error_log_file_path = "/var/log/suricata/error.log"  # Modify with your actual error log file path

# Function to read the log file
def read_logs(file_path):
    logs = []
    try:
        with open(file_path, "r") as file:
            # Read the logs line by line
            logs = file.readlines()
    except FileNotFoundError:
        print(f"Log file not found: {file_path}")
    return logs

# Home page route
@app.route('/')
def home():
    return render_template("index.html")

# Error log page route
@app.route('/error_logs')
def error_logs():
    return render_template("errorlog.html")

# API route to get Suricata logs
@app.route('/logs')
def logs():
    logs = read_logs(log_file_path)
    # Filter logs as necessary (optional), here we just send all logs
    return jsonify({"suricata": logs})

# API route to get error logs
@app.route('/error_logs_data')
def error_logs_data():
    error_logs = read_logs(error_log_file_path)
    # Filter or process error logs as needed
    return jsonify({"error": error_logs})

if __name__ == '__main__':
    app.run(debug=True)
