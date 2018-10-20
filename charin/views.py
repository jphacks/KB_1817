from flask import request, redirect, url_for, render_template, flash, abort, session
from charin import app, db
from charin.models import User

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

    return ""
# @app.route('/get_users_location', methods=['GET'])
# def get_users_location():
#     user_id = session.get('user_id')
#     user = db.session.query(User).filter(User.id==user_id).first()
#     latitude = user.latitude
#     longitude = user.longitude
#     near_users = db.session.query(User).f

#投げ銭する
# @app.route('/give', methods=['GET','POST'])
# def give():
#     if request.method == 'POST':

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
    return render_template('login.html')

#logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You were logged out')
    return redirect(url_for('index'))