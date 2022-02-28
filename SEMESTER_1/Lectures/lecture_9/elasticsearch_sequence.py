from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(
    "http://localhost:9200",
    basic_auth=("elastic", "changeme")
)

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

doc2 = {
    'author': 'Iliyan',
    'text': 'Elasticsearch: cool.',
    'timestamp': datetime.now(),
}

res = es.index(index="test-index", id=1, document=doc)
res = es.index(index="test-index", id=2, document=doc2)
print(res['result'])

res = es.get(index="test-index", id=1)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", query={"match_all": {}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print(hit["_source"])
    #print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])