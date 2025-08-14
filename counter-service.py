from flask import Flask, request, jsonify
import os

# Ensure /app/data exists in the container
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Counter file path
COUNTER_FILE = os.path.join(DATA_DIR, "counter.txt")

app = Flask(__name__)

def read_counter():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            return int(f.read().strip())
    return 0

def update_counter(counter):
    print(f"Writing counter to: {COUNTER_FILE}")
    os.makedirs(os.path.dirname(COUNTER_FILE), exist_ok=True)
    with open(COUNTER_FILE, "w") as f:
        f.write(str(counter))

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    counter = read_counter()
    if request.method == 'POST':
        counter += 1
        update_counter(counter)
        return f"POST requests counter updated. Current count: {counter}"
    return f"Current POST requests count: {counter}"

@app.route('/health', methods=['GET'])
def health_check():
    try:
        read_counter()
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "reason": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=False)
