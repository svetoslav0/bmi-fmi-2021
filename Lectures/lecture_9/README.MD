# Elasticsearch official docker repository

https://hub.docker.com/_/elasticsearch

## Run Elasticsearch docker image

``` bash
docker network create elastic
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.16.2
docker run -d --name es01-test --net elastic -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.16.2
```

## Python driver for elasticsearch

https://elasticsearch-py.readthedocs.io/en/v7.16.2/

### Example

``` Python
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", id=1, document=doc)
print(res['result'])

res = es.get(index="test-index", id=1)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", query={"match_all": {}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
```

## Run Kibana Docker image

``` bash
docker pull docker.elastic.co/kibana/kibana:7.16.2
docker run --name kib01 -p 127.0.0.1:5601:5601 -e "ELASTICSEARCH_HOSTS=http://localhost:9200" docker.elastic.co/kibana/kibana:7.16.2

```
