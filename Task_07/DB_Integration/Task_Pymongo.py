import datetime
import pprint

import pymongo as pyM
'''
usuario, senha e nome do cluster foram censurados por motivos de segurança, na parte de conexão ao banco de dados do AtlasDB
'''
client = pyM.MongoClient("mongodb+srv://(usuario):(senha)@(Nome_do_cluster).sxallkd.mongodb.net/?retryWrites=true&w=majority")
db = client.bank
collections = db.bank
print(collections.name)

posts_inseridos = [{
    "cliente": "victor",
    "cpf": "12345678954",
    "endereco": "Rua dos bobos numero 0",
    "tipo_conta": "Conta corrente",
    "agencia_conta": "0001",
    "numero_conta": "14589-8",
    "saldo": 8500.00,
    "tags": ["conta_banco", "criando_usuario"],
    "date": datetime.datetime.utcnow()},
    {
        "cliente": "sabrina",
        "cpf": "45898745895",
        "endereco": "Rua paraguai 180",
        "tipo_conta": "Conta poupança",
        "agencia_conta": "0001",
        "numero_conta": "85478-9",
        "saldo": 10000.00,
        "tags": ["conta_banco", "criando_usuario"],
        "date": datetime.datetime.utcnow()
    }]

posts = db.posts
result = posts.insert_many(posts_inseridos)
result.inserted_ids
pprint.pprint(db.posts.find_one({"cliente": "victor"}))
pprint.pprint(db.posts.find_one({"cliente": "sabrina"}))

for post in posts.find():
    pprint.pprint(post)

print(db.list_collection_names)

def function_to_be_used_as_example(arg1):
    print(arg1)

#coding...