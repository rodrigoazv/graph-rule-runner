
from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "bolt://0.0.0.0:7687", 
  auth=basic_auth("<USERNAME>", "<PASSWORD>"))

cypher_query = '''
MATCH (p:Product)-[:PART_OF]->(:Category)-[:PARENT*0..]->
(:Category {categoryName:$category})
RETURN p.productName as product
'''

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
      category="Dairy Products").data())

  for record in results:
    print(record['product'])

driver.close()