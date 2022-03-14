from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "bolt://35.174.139.5:7687",
  auth=basic_auth("neo4j", "coating-compromises-trusts"))

cypher_query = '''
MATCH (c:Person{name:$name})
  RETURN c as person
'''

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
                      name="Jaime Lannister").data())
  for record in results:
    print(record['person'])

driver.close()