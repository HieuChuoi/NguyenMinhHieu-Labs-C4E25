from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_database()
customers = db["customers"]

events = db.customers.count_documents(({"ref": "events"}))
print("Events:", events)

ads = db.customers.count_documents(({"ref": "ads"}))
print("Ads:", ads)

wom = db.customers.count_documents(({"ref": "wom"}))
print("WOM:", wom)


from matplotlib import pyplot
ref_count =[events, ads, wom]
ref_name =["Events", "Ads", "Wom"]

pyplot.pie(ref_count, labels=ref_name, autopct="%.1f%%", shadow=True)
pyplot.axis("equal")
pyplot.show()