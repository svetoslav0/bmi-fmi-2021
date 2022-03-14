from neo4j import GraphDatabase, basic_auth
import sys

class Neo4jDB:
    def __init__(self, url, userName, password) -> None:
        self.url = url
        self.userName = userName
        self.password = password

    def connect(self):
        driver = GraphDatabase.driver(self.url, auth=basic_auth(self.userName, self.password))
        self.session = driver.session()
    
    def main(self, url, name):
        with open(url, 'r') as csvfile:
            lines = csvfile.readlines()
            for line in lines[1:]:
                query = "CREATE (a:{}) ".format(name)
                keys = line.split(",")
                for key in keys:
                    key_value = key.split(":")
                    if len(key_value) == 2:
                        query += " SET a." + \
                            key_value[0].rstrip() + " = '" + \
                            key_value[1].rstrip() + "' "
                query += " RETURN a"
                yield query
        pass

    def run_query(self, query):
        return self.session.run(query)

    def integrate(self, type):
        index = 0
        if type == "sample":
            iterator = self.main('test_data/Sample.csv', "sample")
            for query in iterator:
                index = index + 1
                print("Add new entry in sample index = {}".format(index))
                res = self.session.run(query)
    
        index = 0
        if type == "hugosymbol":
            iterator = self.main('test_data/HugoSymbol.csv', "hugosymbol")
            for query in iterator:
                index = index + 1
                print("Add new entry in hugosymbol index = {}".format(index))
                res = self.session.run(query)

        index = 0
        if type == "mutations":
            itrator = self.create_relation()
            for query in itrator:
                index = index + 1
                print("Add new relations index = {}".format(index))
                res = self.session.run(query)

    def create_relation(self):
        with open('test_data/mutation.csv', 'r') as csvfile:
            lines = csvfile.readlines()
            for line in lines[1:]:
                query = "MATCH (a:sample),(b:hugosymbol) "
                keys = line.split(",")
                query += "WHERE a.name = '{}' AND b.name = '{}' CREATE (a)-[r:mutation]->(b) ".format(
                    keys[0].rstrip(), keys[len(keys) - 1].rstrip())
                for key in keys[1:len(keys)-1]:
                    key_value = key.split(":")
                    if len(key_value) >= 2:
                        query += " SET r.{} = '{}' ".format(
                            key_value[0].rstrip(), key_value[1].rstrip())
                query += " RETURN a"
                yield query
        return

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Enter valid url, user name and password")
        exit()

    url = str(sys.argv[1])
    userName = str(sys.argv[2])
    password = str(sys.argv[3])
    type = sys.argv[4]

    neo4jdb = Neo4jDB(url, userName, password)
    neo4jdb.connect()
    neo4jdb.integrate(type)

   
