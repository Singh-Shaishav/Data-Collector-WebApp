from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from send_email import send_email



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:sks24894@localhost/Height Data Collector'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["Email_name"]
        height=request.form["Height_name"] 
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data=Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height)
            send_email(email, height, average_height)
            return render_template("success.html")
    return render_template("Fail.html")


if __name__=='__main__':
    app.debug=True
    app.run(port=5000)




