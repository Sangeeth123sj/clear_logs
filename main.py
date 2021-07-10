from website import create_app
from flask_login import login_user, logout_user,current_user, login_required
from website.models import Supple
from website import db
from flask import flash
import json

app = create_app()
if __name__ == '__main__':
   app.run(debug=True)


from flask import Flask, render_template, redirect, request, jsonify
from flask_socketio import SocketIO
#async_mode = None
#app = Flask(__name__)
#socket_ = SocketIO(app, async_mode=async_mode )



@app.route('/check', methods=['POST','GET'])
def login_check():
    if request.method == 'POST':
        result = request.form
        #if result['email'] == 'sang@gmail.com' and result['password'] == '123':
        return render_template('home.html', result=result['email'])


@app.route('/home', methods=['POST','GET'])
@login_required
def home():
    if  request.method == 'GET':
        return render_template('home.html',user = current_user)
    if request.method == 'POST':
        subject = request.form.get('subject')
        semester = request.form.get('semester')
        modules_covered = request.form.get('modules_covered')
        modules_left = request.form.get('modules_left')
        new_supple = Supple(user_id = current_user.id, subject = subject, semester = semester, modules_covered = modules_covered )
        db.session.add(new_supple)
        db.session.commit()
        flash("Subject saved!", category='success')
        return render_template('home.html', user = current_user) 

@app.route('/delete_supple', methods=['POST'])
def delete():
    supple = json.loads(request.data)
    supple_id = supple['supple_id']
    supple = Supple.query.get(supple_id)
    if supple:
        if supple.user_id == current_user.id:
            db.session.delete(supple)
            db.session.commit()
    return jsonify({})
