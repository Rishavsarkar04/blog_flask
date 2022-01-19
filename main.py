from flask import Flask, render_template , request , session , redirect , flash
from flask.helpers import url_for
from flask_mail import Mail
from sqlalchemy.sql.elements import BooleanClauseList, RollbackToSavepointClause
from werkzeug.utils  import secure_filename
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError
import json
import pymysql
import math
pymysql.install_as_MySQLdb()
import os



with open('config.json', 'r') as c:
    params = json.load(c)['parameters']

local_server = True

app = Flask(__name__)


app.secret_key = os.urandom(12).hex()

app.config['UPLOAD_FOLDER'] = params['upload_location']

app.config.update(
    
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT  = '465',
    MAIL_USE_SSL  = True,
    MAIL_USE_TLS = False,
    MAIL_USERNAME  = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_password']
)

mail = Mail(app)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['production_uri']

db = SQLAlchemy(app)

class Contacts(db.Model):

    serial_no  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Posts(db.Model):

    serial_no  = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(20), nullable=False)
    tagline = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=True)
    img_file = db.Column(db.String(20), nullable= True)
    like = db.Column(db.Integer, default = 0)
    dislike = db.Column(db.Integer, default = 0)


class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(80), nullable=False)
    post_slug = db.Column(db.String(20), nullable=False)
    replies = db.relationship('Reply' , backref = 'comment' , lazy = 'dynamic' , cascade="all, delete" )

class Reply(db.Model):

    id  = db.Column(db.Integer, primary_key=True)
    reply = db.Column(db.String(80), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id') , nullable=False)
    

 
@app.route('/')
def home():
    posts = Posts.query.order_by(Posts.date.desc()).all()
    last = math.ceil(len(posts)/int(params['num_of_pages']))
    #[0:params['num_of_pages']]

    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1) * int(params['num_of_pages']) : (page-1) * int(params['num_of_pages']) + int(params['num_of_pages'])]
    

    if page == 1:
        pev = '#'
        next ='/?page=' + str(page + 1)

    elif (page == last):
            pev = '/?page=' + str(page - 1)  
            next ='#'

    else:
        pev = '/?page=' + str(page - 1)  
        next ='/?page=' + str(page + 1)

    
    return render_template('index.html' , params = params , posts = posts , pev = pev, next=next , last = last , page = page)

@app.route('/search')
def search():
    
    q = request.args.get('qeury')
    if q == '':
        sposts = Posts.query.order_by(Posts.date.desc()).all()
        last = math.ceil(len(sposts)/int(params['num_of_pages']))
        #[0:params['num_of_pages']]

        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        sposts = sposts[(page-1) * int(params['num_of_pages']) : (page-1) * int(params['num_of_pages']) + int(params['num_of_pages'])]
   
    else:   
        sposts = Posts.query.filter(Posts.tittle.contains(q) | Posts.content.contains(q)).all()       
        last = math.ceil(len(sposts)/int(params['num_of_pages']))
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        sposts = sposts[(page-1) * int(params['num_of_pages']) : (page-1) * int(params['num_of_pages']) + int(params['num_of_pages'])]

    if page == 1:
        pev = '#'
        next =f'/search?qeury={q}&page=' + str(page + 1)

    elif (page == last):
            pev = f'/search?qeury={q}&page=' + str(page - 1)  
            next ='#'

    else:
        pev = f'/search?qeury={q}&page=' + str(page - 1)  
        next =f'/search?qeury={q}&page=' + str(page + 1)

    
    return render_template('search.html' , params = params , sposts = sposts , pev = pev, next=next , last = last , page = page , q=q)


@app.route('/about')
def about():
    return render_template('about.html' , params = params)


@app.route('/post/<string:post_slug>', methods = ['GET' ,'POST'])
def post(post_slug):
    if request.method == 'POST':
        post_query = Posts.query.filter(Posts.slug == post_slug).first()    
        ld = request.form.get('like')
        dl = request.form.get('dislike')

        if ld == 'like':
            total_like = int(post_query.like) + 1
            post_query.like = total_like
            db.session.commit()           
            return redirect(url_for('post' , post_slug = post_slug))

        elif dl == 'dislike':
            total_dislike = int(post_query.dislike) + 1
            post_query.dislike = total_dislike
            db.session.commit()
            return redirect(url_for('post' , post_slug = post_slug))

        comments = request.form.get('comment')

        if comments:
            cm = Comment(comment = comments , post_slug = post_slug)
            db.session.add(cm)
            db.session.commit()
            return redirect(url_for('post' , post_slug = post_slug))
        
        replys = request.form.get('reply')

        if replys:
            commentid = request.form.get('commentId')
            comment_reply = Comment.query.filter_by(id = commentid).first()
            rp = Reply( reply = replys , comment = comment_reply )
            try:
                db.session.add(rp)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
            return redirect(url_for('post' , post_slug = post_slug))

    commentid = request.form.get('commentId')
      
    comments = Comment.query.filter_by(post_slug = post_slug).all()

    replies = Reply.query.all()

    post = Posts.query.filter_by(slug = post_slug).first()

    return render_template('post.html' , params = params , post = post , comments = comments, replies= replies)


@app.route('/dashboard' , methods =['GET','POST'])
def dashboard():
    if 'user' in session and session['user'] == params['admin_name']:
        posts = Posts.query.all()
        return render_template('dashboard.html' , params=params , posts = posts)

    elif request.method=='POST':
        username = request.form.get('uname')
        password = request.form.get('upass')
        if (username == params['admin_name'] and password == params['admin_password']):
            flash('you are logged in' , 'success')
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html' , params=params , posts = posts)
        else:
            flash('wrong username or password' , 'danger')
            return render_template('login.html' , params = params )
    else:     
        return render_template('login.html' , params = params )


@app.route('/edit/<string:serialno>' ,  methods=["GET","POST"])
def edit(serialno):
    if 'user' in session and session['user'] == params['admin_name']:
        if request.method == 'POST':
            box_title = request.form.get('title')        
            box_tagline = request.form.get('tline')
            box_slug = request.form.get('slug')
            box_content = request.form.get('content')
            box_image = request.form.get('image')

            
            if serialno == '0':
                slugquery = Posts.query.filter_by(slug = box_slug).first()
                titlequery = Posts.query.filter_by(tittle = box_title).first()
                

                if (slugquery and titlequery):
                    flash('this tittle and slug is already exsits' , 'info')
                    post = Posts.query.filter_by(serial_no=serialno).first()
                    return render_template('edit.html' , params = params , post = post , serialno = serialno)

                elif titlequery:
                    flash('this tittle is already exsits' , 'info')
                    post = Posts.query.filter_by(serial_no=serialno).first()
                    return render_template('edit.html' , params = params , post = post , serialno = serialno)

                elif slugquery:
                    flash('this slug is already exsits' , 'info')                    
                    post = Posts.query.filter_by(serial_no=serialno).first()
                    return render_template('edit.html' , params = params , post = post , serialno = serialno)            
                else:          
                    post =  Posts(tittle = box_title , tagline = box_tagline , slug = box_slug , content = box_content , img_file = box_image , date = datetime.now())
                    db.session.add(post)
                    db.session.commit()
                   

            else:
                post = Posts.query.filter_by(serial_no = serialno).first()
                post.tittle = box_title
                post.tagline = box_tagline
                post.slug = box_slug
                post.content = box_content
                post.img_file = box_image
                post.date = datetime.now()
                            
                db.session.commit()
                     
    post = Posts.query.filter_by(serial_no=serialno).first()
    return render_template('edit.html' , params = params , post = post , serialno = serialno)   


@app.route('/upload' ,  methods=["GET","POST"]) 
def uploader():
    if "user" in session and session['user']==params['admin_name']:
        if request.method=='POST':
            flash("Uploaded successfully!" , 'success')
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    flash('logged out successfully' , 'success')
    session.pop('user')
    return redirect(url_for('dashboard'))


@app.route('/delete/<string:serialno>' ,  methods=["GET","POST"])
def delete(serialno):
    if 'user' in session and session['user'] == params['admin_name']:
        post = Posts.query.filter_by(serial_no = serialno).first()
        comdel = Comment.query.filter(Comment.post_slug == post.slug).all()

        for i in comdel:
            db.session.delete(i)
        db.session.delete(post)
        db.session.commit()
              
    return redirect(url_for('dashboard'))

    
@app.route('/contact' ,  methods=["GET","POST"])
def contact():
    if (request.method=='POST'):
        # add entry to the database
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contacts(name = name , phone_num = phone , msg = message , email = email , date = datetime.now())

        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender= email,
                          recipients = [params['gmail_user']],
                          body = message + "\n" + phone
                          )
        flash('thanks for submitting your details we will get back to you soon' , 'success')
    return render_template('contact.html' , params = params)


if __name__ == '__main__':
    app.run(debug=True)