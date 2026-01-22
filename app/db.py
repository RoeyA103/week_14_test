from mysql.connector import pooling , Error
from dotenv import load_dotenv
import os

load_dotenv()

SQL_HOST = os.getenv("SQL_HOST")
SQL_USER = os.getenv("SQL_USER","root")
SQL_PASS = os.getenv("SQL_PASS","123")


pool = pooling.MySQLConnectionPool(
    pool_name="mypool",      
    pool_size=3,             
    pool_reset_session=True, 
    host=SQL_HOST,
    user=SQL_USER,
    password=SQL_PASS,
    # database="weapons_db"
)


def init_db():
    try:
        conn = pool.get_connection()
        cursor = conn.cursor()

        create_table_query = """
        CREATE DATABASE IF NOT EXISTS weapons_db;

        USE weapons_db;

        CREATE TABLE IF NOT EXISTS weapons (
            id INT AUTO_INCREMENT PRIMARY KEY,
            weapon_id VARCHAR(100),
            weapon_name VARCHAR(100),
            weapon_type VARCHAR(100),
            range_km INT,
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
        conn = pool.get_connection()
        cursor = conn.cursor()
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
            values = row.values()
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
