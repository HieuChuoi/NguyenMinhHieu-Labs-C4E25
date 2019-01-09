from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_database()

post_collection = db["Hieu"]

new_post = {
    "title": "C4E25",
    "author": "Nguyen Minh Hieu",
    "content": "Lớp C4E25 là một lớp có rất nhiều thành viên giỏi và đáng ngưỡng mộ. Em rất thích cách dạy của anh Huy và thích anh Quân vì anh ý rất nhiệt tình giúp đỡ em"
}

post_collection.insert_one(new_post)
client.close()