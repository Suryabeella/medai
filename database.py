import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "database")
DB_NAME = os.path.join(DB_DIR, "mediaai.db")


def get_connection():
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS medicines(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medicine_name TEXT,
        price TEXT,
        availability TEXT,
        manufacturer TEXT,
        pharmacy TEXT,
        product_url TEXT
    )
    """)

    conn.commit()
    conn.close()


def register_user(name, email, password):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users(name,email,password) VALUES(?,?,?)",
            (name, email, password)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def login_user(email, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )
    user = cur.fetchone()
    conn.close()
    return user


def save_medicine(data):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO medicines(
        medicine_name, price, availability, manufacturer, pharmacy, product_url
    ) VALUES(?,?,?,?,?,?)
    """, (
        data.get("medicine_name", "Unknown"),
        data.get("price", "Not Found"),
        data.get("availability", "Unavailable"),
        data.get("manufacturer", "-"),
        data.get("pharmacy", "-"),
        data.get("product_url", "")
    ))
    conn.commit()
    conn.close()


def get_all_medicines():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM medicines ORDER BY id DESC")
    medicines = cur.fetchall()
    conn.close()
    return medicines
