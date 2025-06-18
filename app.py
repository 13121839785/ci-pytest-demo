from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟用户数据库
users = {
    "alice": "123456",
    "bob": "password"
}

# 模拟 token 存储
tokens = {}

# 登录接口（POST）
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # 校验用户名密码
    if username in users and users[username] == password:
        token = f"token-{username}"
        tokens[token] = username
        return jsonify({"token": token})

    return jsonify({"message": "Invalid credentials"}), 401


# 受保护接口（必须带 token）
@app.route("/user/profile", methods=["GET"])
def user_profile():
    auth_header = request.headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        user = tokens.get(token)
        if user:
            return jsonify({
                "username": user,
                "email": f"{user}@example.com",
                "role": "tester"
            })
    return jsonify({"message": "Unauthorized"}), 401



@app.route("/user/list")
def user_list():
    page = request.args.get("page", default=1, type=int)
    size = request.args.get("size", default=10, type=int)

    # 模拟返回列表
    data = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
        {"id": 4, "name": "David"},
        {"id": 5, "name": "Emma"},
        {"id": 6, "name": "Frank"},
        {"id": 7, "name": "Grace"},
        {"id": 8, "name": "Helen"},
        {"id": 9, "name": "Ivan"},
        {"id": 10, "name": "Jane"}
    ]

    # 简单分页逻辑
    start = (page - 1) * size
    end = start + size
    result = data[start:end]

    return jsonify({
        "page": page,
        "size": size,
        "total": len(data),
        "data": result
    })

# 添加用户（POST，需要带 token）
# 自动增长 ID
user_id_counter = 4  # 初始已有 3 个用户

@app.route("/user/add", methods=["POST"])
def add_user():
    global user_id_counter
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer ") or auth_header.split(" ")[1] not in tokens:
        return jsonify({"message": "Unauthorized"}), 401

    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"message": "Missing name or email"}), 400

    new_user = {
        "id": user_id_counter,
        "name": name,
        "email": email
    }
    users_db.append(new_user)
    user_id_counter += 1

    return jsonify({
        "message": "User added successfully",
        "id": new_user["id"],  # ✅ 返回 ID，供自动化用例使用
        "user": new_user
    }), 201


# 模拟用户数据库（用 id 来存用户）
user_list = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

# 查询单个用户接口（GET /user/<id>）
@app.route("/user/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer ") or auth_header.split(" ")[1] not in tokens:
        return jsonify({"message": "Unauthorized"}), 401

    for user in users_db:  # ✅ 改成用 users_db
        if user["id"] == user_id:
            return jsonify(user)

    return jsonify({"message": "User not found"}), 404

# 修改用户信息接口（PUT /user/<id>）
@app.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer ") or auth_header.split(" ")[1] not in tokens:
        return jsonify({"message": "Unauthorized"}), 401

    data = request.get_json()
    for user in user_list:
        if user["id"] == user_id:
            user.update({
                "name": data.get("name", user["name"]),
                "email": data.get("email", user["email"])
            })
            return jsonify({"message": "User updated", "user": user})

    return jsonify({"message": "User not found"}), 404
users_db = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]

# DELETE 删除用户接口（需要 token）
@app.route("/user/delete/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer ") or auth_header.split(" ")[1] not in tokens:
        return jsonify({"message": "Unauthorized"}), 401

    for user in users_db:
        if user["id"] == user_id:
            users_db.remove(user)
            return jsonify({"message": "User deleted"})

    return jsonify({"message": "User not found"}), 404



if __name__ == "__main__":
    app.run(port=5000)
