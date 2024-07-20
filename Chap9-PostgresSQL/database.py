import streamlit as st
import psycopg2-binary

def create_connection():
    return psycopg2.connect(
            dbname=st.secrets['PGDATABASE'],
            user=st.secrets['PGUSER'],
            password=st.secrets['PGPASSWORD'],
            host=st.secrets['PGHOST']
        )


def create_table():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id SERIAL PRIMARY KEY,
            task TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT FALSE
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def add_todo(task):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
    conn.commit()
    cur.close()
    conn.close()

def get_todos():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos ORDER BY id")
    todos = cur.fetchall()
    cur.close()
    conn.close()
    return todos

def update_todo(id, completed):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE todos SET completed = %s WHERE id = %s", (completed, id))
    conn.commit()
    cur.close()
    conn.close()

def delete_todo(id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM todos WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()