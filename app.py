from flask import Flask, request, jsonify

app = Flask(__name__)

users = []
messages = []

# Create user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    users.append({"name": data["name"]})
    return jsonify({"message": "User created"}), 201

# Send message
@app.route('/messages', methods=['POST'])
def send_message():
    data = request.json
    messages.append({
        "from": data["from"],
        "to": data["to"],
        "message": data["message"]
    })
    return jsonify({"message": "Message deliveredf successfully"}), 201

# Get messages
@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages), 200

# Update status
@app.route('/status', methods=['POST'])
def update_status():
    data = request.json
    return jsonify({"status": data["status"], "updated": True}), 200

if __name__ == '__main__':
    app.run(debug=True)

