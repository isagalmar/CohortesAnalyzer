import duckdb as dd
import os

# Create an in-memory DuckDB connection
#con.execute('CREATE TABLE mytable(field1 VARCHAR, field2 VARCHAR[])')
#con.execute("INSERT INTO mytable VALUES ('1', LIST_VALUE('1', '2', '3'))")
#con.execute("COPY mytable FROM './data/cohorte_alegias.csv' (HEADER, DELIMITER ',')")


class DuckConnectionMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DuckConnection(metaclass=DuckConnectionMeta):
    
    def __init__(self):
        self.open_connection = dd.connect("mi_base_de_datos.duckdb", read_only=False)
        self.open_connection.read_csv("./data/cohorte_alegias.csv")
    
    def load_csv(self):
        pass
        
    def read(self):
        result = self.open_connection.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'main';
""").fetchall()
        print(result)