from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import pymongo


client = pymongo.MongoClient("mongodb+srv://debanjan:debanjan@cluster0.hokbp.mongodb.net/?retryWrites=true&w=majority")
db = client["BlogPost"]

post = db["post"]


app = Flask(__name__)


@app.route('/')
def index():
    data = post.find()
    #output format (title, metaTitle, slug, summary, published, publishedAt, content, featureImg)
    return render_template('index.html',posts=data)


@app.route('/admin_create_post', methods=['GET', 'POST'])
def post_create():
    if request.method == 'GET':
        return render_template('add_post.html')
    elif request.method == 'POST':
        title = request.form['title']
        slug = title
        summary = request.form['summary']
        content = request.form['content']
        featureImg = request.form['image']
        print(title, slug, summary, content, featureImg)
        post.insert_one({"title":title,"metaTitle":title,"slug":slug,"summary":summary,"published":1,"publishedAt":1,"content":content,"featureImg":featureImg})
        return render_template('add_post.html', message="1")
    return render_template('add_post.html', message="0")


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/getpost/<metaTitle>')
def posts(metaTitle):
    common_posts = []
    data = post.find_one({"metaTitle":metaTitle})
    cp = post.find({},{ "_id": 0, "title": 1, "metaTitle": 1, "featureImg": 1, "summary": 1}).limit(4)
    print(type(cp))
    for i in cp:
        if i['metaTitle'] != metaTitle:
            common_posts.append(i)
    return render_template('single_page.html',post=data,common_posts=common_posts)



if __name__ == '__main__':
    app.run(debug=True)



# npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch