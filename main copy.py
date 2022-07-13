from pymongo import MongoClient

# cluster = 'mongodb+srv://alex:tertul@cluster0.fvanwtt.mongodb.net/eleclib?retryWrites=true&w=majority'
cluster = 'mongodb+srv://alex:tertul@cluster0.dbxggby.mongodb.net/eleclib?retryWrites=true&w=majority'
# cluster = 'mongodb://localhost:27017/eleclib'
client = MongoClient(cluster)

print('databases:', client.list_database_names())
db = client.eleclib
# print(db.books)
print('collections:', db.list_collection_names()) #! [] local collection name not showing

# book1 = {'title': 'East of Eden', 'Synopsis': 'Classic American novel', 'author': 'Steinbeck'}
# books = db.books

# result = books.insert_one(book1)
# result = books.find_one()
# print(result)
# {'_id': ObjectId('62cede112919f323e95e968a'), 'title': 'East of Eden', 'Synopsis': 'Classic American novel', 'author': 'Steinbeck'}