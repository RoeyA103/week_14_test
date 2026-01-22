from mysql.connector import pooling , Error ,connect
from dotenv import load_dotenv
import os

load_dotenv()

SQL_HOST = os.getenv("SQL_HOST","mysql-0.mysql-svc")
SQL_USER = os.getenv("SQL_USER","root")
SQL_PASS = os.getenv("SQL_PASS","123")


# pool = pooling.MySQLConnectionPool(
#     pool_name="mypool",      
#     pool_size=3,             
#     pool_reset_session=True, 
#     host=SQL_HOST,
#     user=SQL_USER,
#     password=SQL_PASS,
#     # database="weapons_db"
# 
def get_conn():

    try:
        conn = connect(
        host=SQL_HOST,
        user=SQL_USER,
        password=SQL_PASS
        )

       

        return conn
    except Error as e:
        raise e


def create_db():
    try:
        conn = get_conn()
        cursor = conn.cursor()

        create_db_query = """
        CREATE DATABASE IF NOT EXISTS weapons_db;
        """
        cursor.execute(create_db_query)
        conn.commit()

        print("db 'weapons_db' created successfully.")

    except Error as e:
        raise e

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def init_db():
    try:
        conn = get_conn()
        cursor = conn.cursor()

        cursor.execute("USE weapons_db;")


        create_table_query = """
        CREATE TABLE IF NOT EXISTS weapons (
            id INT AUTO_INCREMENT PRIMARY KEY,
            weapon_id VARCHAR(100),
            weapon_name VARCHAR(100),
            weapon_type VARCHAR(100),
            range_km,
            weight_kg FLOAT,
            manufacturer VARCHAR(100),
            origin_country VARCHAR(100),
            storage_location VARCHAR(100),
            year_estimated INT,
            risk_level VARCHAR(100)
        );
        """
        cursor.execute(create_table_query)
        conn.commit()

        print("Table 'weapons' created successfully.")

    except Error as e:
        raise e

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def save_records(data:list[dict]):
    try:
        conn = get_conn()
        cursor = conn.cursor()

        cursor.execute("USE weapons_db;")

        query = """
            insert into weapons (
            weapon_id ,
            weapon_name ,
            weapon_type ,
            range_km ,
            weight_kg ,
            manufacturer,
            origin_country,
            storage_location,
            year_estimated,
            risk_level)
            values (
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
            );
        """
        for row in data:
            values = list(row)
            cursor.execute(query, values)
        conn.commit()
        return True
    except Error as e:
        raise e

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()        
