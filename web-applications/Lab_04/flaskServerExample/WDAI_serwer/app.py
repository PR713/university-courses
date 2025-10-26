from flask import Flask, jsonify, make_response, request, abort
import requests
import threading
import json
import jwt
import sqlite3
from functools import wraps

app = Flask(__name__)

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        headers = request.headers
        bearer = headers.get('Authorization')
        if not bearer:
            return make_response(jsonify({"message": "Brak tokena!"}), 401)

        token = bearer.split()[1] 

        try:
            data = jwt.decode(token, 'SECRET_KEY', algorithms=['HS256'])
            if data['public_id'] != 'admin':
                return make_response(jsonify({"message": "Niepoprawny token!"}), 401)
            current_user = 'admin'
        except:
            return make_response(jsonify({"message": "Token niepoprawny!"}), 401)
        return f(*args, **kwargs)
    return decorator

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route("/posts")
def getPosts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    result = []
    for item in posts:
      result.append({k: item[k] for k in item.keys()})
    return json.dumps(result)

@app.route("/posts/<int:id>",  methods=['GET'])
def getPostById(id):
    post = get_post(id)
    result =  {k: post[k] for k in post.keys()}
    return json.dumps(result)

@app.route("/posts",  methods=['POST'])
@token_required
def createPost():
    title = request.get_json().get('title')
    content = request.get_json().get('content')
    if not title:
        return 'Title is required!', 400

    elif not content:
        return 'Content is required!', 400

    else:
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                     (title, content))
        conn.commit()
        conn.close()
        return 'Post was successfully added', 200

@app.route("/posts/<int:id>", methods=['PUT'])
@token_required
def editPost(id):
    post = get_post(id)
    title = request.get_json().get('title')
    content = request.get_json().get('content')
    if not title:
        return 'Title is required!', 400

    elif not content:
        return 'Content is required!', 400
    else:
        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ?'
                     ' WHERE id = ?',
                     (title, content, id))
        conn.commit()
        conn.close()
        return 'Post was successfully changed', 200
     

@app.route("/posts/<int:id>", methods=['DELETE'])
@token_required
def deletePost(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return 'deleted', 200

@app.route("/login",  methods = ['POST'])
def login():
    auth = request.get_json()
    if not auth or not auth.get('username') or not auth.get('password'):
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic-realm= "Login required!"'})

    if auth.get('username') == 'admin' and auth.get('password') == 'Test1234!':
        token = jwt.encode({'public_id': 'admin'}, 'SECRET_KEY', 'HS256')
        return make_response(jsonify({'token': token}), 201)

    return make_response('Could not verify password!', 403, {'WWW-Authenticate': 'Basic-realm= "Wrong Password!"'})


if __name__ == '__main__':
    app.run()

#http://127.0.0.1:5000/posts