import streamlit as st
from database import (
    create_connection,
    create_table,
    add_todo,
    get_todos,
    update_todo,
    delete_todo,
)

st.title("Todo App")
st.subheader("Create, Read, Update, and Delete todos")
st.write("---")

# Ensure table exists
create_table()

# Add new todo
new_todo = st.text_input("Enter task:")
add_todo_button = st.button("Add")
if add_todo_button:
    if new_todo:
        add_todo(new_todo)
        st.success(f"{new_todo} added successfully!")
    else:
        st.error("Please enter a task.")

todos = get_todos()
# print todos to the screen
col1, col2, col3, col4 = st.columns([1, 3, 2, 1])

col1.subheader("ID")
col2.subheader("Task")
col3.subheader("Done")
col4.subheader("Delete")

for todo in todos:
    col1, col2, col3, col4 = st.columns([1, 3, 2, 1])
    col1.write(todo[0])
    col2.write(todo[1])
    if col3.button("✅" if todo[2] else "🟩",key=f"update_{todo[0]}"):
        update_todo(todo[0], not todo[2])
        st.success("Todo updated successfully!")
        st.rerun()
    if col4.button("🗑️", key=f"delete_{todo[0]}"):
        delete_todo(todo[0])
        st.success("Todo deleted successfully!")
        st.rerun()
