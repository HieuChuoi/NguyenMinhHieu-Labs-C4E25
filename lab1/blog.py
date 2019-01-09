from pymongo import MongoClient
uri = "mongodb://admin:admin1@ds135384.mlab.com:35384/c4e25"

#1. Connect to database (mLab server)
client = MongoClient(uri)

#2. Get a database
db = client.get_database()

#3. Get a collection
post_collection = db["posts"]

#4. Creat a document
new_post = {
    "title": "hom nay troi nhieu may",  #field title
    "content": "toi ra duong, a ma thoi o nha code"   # field content
}


# Lazy loading
post_list = post_collection.find()  # Cursor
# first_post = post_list[0]
# print(first_post)
for p in post_list:
    print(p)


#5. Insert document
# post_collection.insert_one(new_post)


#6. Close conection
client.close()