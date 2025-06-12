from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial data in the to-do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return "Welcome to the sample to-do list app"

# GET: Retrieve all items
@app.route('/items', methods=['GET'])  # Fixed typo
def get_items():
    return jsonify(items)

# GET: Retrieve a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])  # Added item_id in route
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"Error": "Item not found"}), 404
    return jsonify(item)

# POST: Create a new item
@app.route('/items', methods=['POST'])  # Fixed typo in methods
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"Error": "Invalid input"}), 400
    
    new_id = items[-1]["id"] + 1 if items else 1  # Fixed item[-1] to items[-1]
    new_item = {
        "id": new_id,
        "name": request.json['name'],
        "description": request.json.get("description", "")
    }
    items.append(new_item)
    return jsonify(new_item), 201

# PUT: Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"Error": "Item not found"}), 404
    
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# DELETE: Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
