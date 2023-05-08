
# table = """CREATE TABLE POST (
#             postid INTEGER PRIMARY KEY AUTOINCREMENT,
#             title VARCHAR(75) NOT NULL,
#             metaTitle VARCHAR(100),
#             slug VARCHAR(150) NOT NULL,
#             summary VARCHAR(200) NOT NULL,
#             published TINYINT(1) NOT NULL DEFAULT 0,
#             publishedAt DATETIME Not NULL,
#             content TEXT DEFAULT NULL,
#             featureImg VARCHAR(255) NOT NULL ); """

# tag_table = """ CREATE TABLE TAGS (
#                 value VARCHAR(255) NOT NULL,
#                 post_id INITEGER NOT NULL,
#                 FOREIGN KEY (post_id) REFERENCES POST(postid)
#             ); """


import pymongo

client = pymongo.MongoClient("mongodb+srv://debanjan:debanjan@cluster0.hokbp.mongodb.net/?retryWrites=true&w=majority")
db = client["BlogPost"]

post = db["post"]

# post.insert_one({"title":"Hello World","metaTitle":"Hello_World","slug":"HelloWorld"
#                 ,"summary":"Hello World summary","published":0,"publishedAt":"2021-01-01 00:00:00",
#                 "content":"Hello World Hello World Hello World Hello World","featureImg":"logo.png", "tags":["Hello","World"]})

# post.insert_one({"title":"Nice World","metaTitle":"Nice_World","slug":"NiceWorld"
#                 ,"summary":"Nice World summary","published":0,"publishedAt":"2021-01-01 00:00:00",
#                 "content":"Nice World Nice World Nice World Nice World","featureImg":"logo.png", "tags":["Nice","World"]})

# post.insert_one({"title":"Good World","metaTitle":"Good_World","slug":"GoodWorld"
#                 ,"summary":"Good World summary","published":0,"publishedAt":"2021-01-01 00:00:00",
#                 "content":"Good World Good World Good World Good World","featureImg":"logo.png", "tags":["Good","World"]})

# x = post.find()
x = post.find({},{ "_id": 0, "title": 1, "metaTitle": 1, "featureImg": 1, "summary": 1}).limit(3)
for i in x:
    print(i)

# @app.route('/post', methods=['GET', 'POST'])
# def post():
#     if request.method == 'POST':
#         title = request.form['title']
#         metaTitle = request.form['metaTitle']
#         slug = request.form['slug']
#         summary = request.form['summary']
#         published = request.form['published']
#         publishedAt = request.form['publishedAt']
#         content = request.form['content']
#         featureImg = request.form['featureImg']
#         post.insert_one({"title":title,"metaTitle":metaTitle,"slug":slug,"summary":summary,"published":published,"publishedAt":publishedAt,"content":content,"featureImg":featureImg})
#         return redirect(url_for('index'))
#     return render_template('post.html')
	# <!-- (id, title, metaTitle, slug, summary, published, publishedAt, content, featureImg) -->

	# <!-- {text:text, img:link, code:code, quote:quote} -->


#  TODO: IMPORTANT

# npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch