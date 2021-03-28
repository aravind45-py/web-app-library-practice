from flask import Flask, render_template, request, redirect, url_for
import pymongo
import pprint
client = pymongo.MongoClient("mongodb+srv://aravind:aravind@cluster1.lkblz.mongodb.net/new?retryWrites=true&w=majority")
db = client.get_database('beta')
col = db.get_collection('test')
app = Flask(__name__)


@app.route('/')
def home():
    all_books= []
    for i in col.find():
        all_books.append(i)
    return render_template('index.html',books = all_books)


@app.route("/add",methods=['GET','POST'])
def add():
    if request.method=="POST":
        data_title = request.form.get('title')
        data_author = request.form.get('author')
        data_rating = request.form.get('rating')
        col.insert_one({"title":data_title,"author":data_author,"rating":data_rating})
        return redirect(url_for('home'))
    return render_template('add.html')
@app.route('/dele/<string:title>',methods=['GET','POST'])
def dele(title):
    col.delete_one({'title':title})
    return redirect(url_for('home'))
@app.route('/edit',methods=['GET','POST'])
def edit():
    col.update_one({'title'})

if __name__ == "__main__":
    app.run(debug=True)

