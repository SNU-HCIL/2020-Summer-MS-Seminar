from flask import Flask, jsonify, request
import os
import bcrypt
import jwt
import json
from flask_cors import CORS, cross_origin
from playAI import play


app = Flask(__name__)
CORS(app)


@app.route("/sign-in", methods=['POST', 'OPTIONS'])
def auth():
    with open('records.json') as json_file:
        records = json.load(json_file)

    print(records)
    
    req = handleRequest(request)
    print(req)

    if req['id'] not in records:
        new_record = {req['id']:{'win':0, 'draw':0, 'lose':0}}
        records.update(new_record)
        print(records)

        with open('records.json', 'w', encoding='utf-8') as make_file:
            json.dump(records, make_file, indent="\t")

    return records[req['id']]


@app.route("/next", methods=['POST', 'OPTIONS'])
def next():
    OXs = list(request.form.to_dict().keys())[0]
    conv = lambda i : i or None
    squares = [conv(i) for i in OXs.split(',')]
    # print( play(squares))
    return str(play(squares))
    # with open('records.json') as json_file:
    #     records = json.load(json_file)

    # print(records)
    
    # req = handleRequest(request)
    # print(req)

    # if req['id'] not in records:
    #     new_record = {req['id']:{'win':0, 'draw':0, 'lose':0}}
    #     records.update(new_record)
    #     print(records)

    #     with open('records.json', 'w', encoding='utf-8') as make_file:
    #         json.dump(records, make_file, indent="\t")

    # return records[req['id']]


    # return 'results'
    # req['password'] = bcrypt.hashpw(req['password'].encode('UTF-8'), bcrypt.gensalt())

    # # row = app.database.execute(text("""
    # #     SELECT
    # #         id,
    # #         hashed_password
    # #     FROM users
    # #     WHERE email = :email
    # # """), {'email': email}).fetchone()

    # new_id = app.database.execute(text("""
    #     INSERT INTO users (
    #         name,
    #         hashed_password
    #     ) VALUES (
    #         :name,
    #         :password
    #     )
    # """), req).lastrowid

    # row = app.database.execute(text("""
    #     SELECT
    #         id,
    #         name
    #     FROM users
    #     WHERE id = :user_id
    # """), {'user_id': new_id}).fetchone

    # create_user = {'id': row['id'],
    # 'name': row['name']} if row else None
    
    # return jsonify(create_user)
    # return 'result'

@app.route("/update", methods=['POST', 'OPTIONS'])
def update():
    with open('records.json') as json_file:
        records = json.load(json_file)

    # print(records)    
    req = handleRequest(request)
    if req['winner'] == 'O':
        records[req['username']]['lose'] += 1
    elif req['winner'] == 'X':
        records[req['username']]['win'] += 1
    else:
        records[req['username']]['draw'] += 1
    

    # if req['id'] not in records:
    #     new_record = {req['id']:{'win':0, 'draw':0, 'lose':0}}
    #     records.update(new_record)
    print(records)

    with open('records.json', 'w', encoding='utf-8') as make_file:
        json.dump(records, make_file, indent="\t")

    return records[req['username']]

@app.route("/")
def root():
    print('access to the root')
    return 'root'

def handleRequest(request):
    data = json.loads(list(request.form.to_dict().keys())[0])
    print(data)
    return data

if __name__=='__main__':
    # app.run() # production
    # app.run(debug=True) # for debugging purpose
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)) ,debug = False, threaded = False)