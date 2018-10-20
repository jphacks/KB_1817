from flask import request, redirect, url_for, render_template, flash, abort, session, jsonify
from charin import app, db
from charin.models import User
import math
import json

default_give = 10
#index
@app.route('/')
def index():
    return render_template('index.html')

#位置情報を定期的にDBヘ
@app.route('/locate_user', methods=['POST'])
def locate():
    location = request.form
    latitude = location["latitude"]
    longitude = location["longitude"]
    user_id = session.get('user_id')

    user_locate = db.session.query(User).filter(User.id==user_id).first()
    user_locate.latitude = latitude
    user_locate.longitude = longitude
    db.session.commit()
    db.session.close()

    return ""

@app.route('/get_users_location', methods=['GET'])
def get_users_location():
    user_id = session.get('user_id')
    user = db.session.query(User).filter(User.id==user_id).first()
    latitude = user.latitude
    longitude = user.longitude

    near_radius = math.sqrt((0.009**2)+(0.009**2))
    min_latitude = latitude - near_radius
    max_latitude = latitude + near_radius
    min_longitude = longitude - near_radius
    max_longitude = longitude + near_radius

    near_users = db.session.query(User).filter((User.latitude >= min_latitude) | (User.latitude <= max_latitude) | (User.longitude >= min_longitude) | (User.longitude <= max_longitude)).all()
    response = []
    for near_user in near_users:
        user_dict = {}
        if near_user == user:
            near_users.remove(near_user)
        else:
            user_dict[near_user.id] = (near_user.latitude,near_user.longitude)
            response.append(user_dict)
    db.session.close()
    return jsonify(near_users=response)

# 投げ銭する
@app.route('/give', methods=['POST'])
def give():
    user_id = session.get('user_id')
    requests = request.form["near_users"]
    dec = json.loads(requests)
    near_users = dec["near_users"]
    if len(near_users) > 0:
        #投げ銭したユーザーから残高を引く
        give_user = db.session.query(User).filter(User.id==user_id).first()
        now_credit = give_user.credit
        after_credit = now_credit - default_give
        give_user.credit = after_credit

        #近くにいたユーザーで投げ銭を山分け
        each_take = default_give // len(near_users)
        for near_user in near_users:
            user_id = near_user.id
            user = db.session.query(User).filter(User.id==user_id).first()
            now_credit = user.credit
            after_credit = now_credit + each_take
            user.credit = after_credit

        db.session.commit()
        db.session.close()
    else:
        print('近くに誰もいません')
        flash('近くに誰もいません...')
    return ""

#user周り
#新規user作成
@app.route('/user/create/', methods=['GET', 'POST'])
def user_create():
    if request.method == 'POST':
        user = User(name=request.form['name'],
                    email=request.form['email'],
                    password=request.form['password'])
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
    db.session.close()
    return render_template('user/create.html')

#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user, authenticated = User.authenticate(db.session.query,
                request.form['email'], request.form['password'])
        if authenticated:
            session['user_id'] = user.id
            flash('You were logged in')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password')
    db.session.close()
    return render_template('login.html')

#logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You were logged out')
    return redirect(url_for('index'))

#iframe
@app.route('/maps')
def maps():
    return render_template('maps.html')