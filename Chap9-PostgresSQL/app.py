import streamlit as st
from database import create_table, add_todo, get_todos, update_todo, delete_todo

# Streamlit app

st.title("Todo App")

# Ensure table exists
create_table()

# Add new todo
new_todo = st.text_input("Add a new todo:")
if st.button("Add"):
    if new_todo:
        add_todo(new_todo)
        st.success(f"{new_todo} added successfully!")
    else:
        st.error("Please enter a todo.")

# Display todos
todos = get_todos()
for todo in todos:
    col1, col2, col3 = st.columns([3, 1, 1])
    
    # Display task with strike-through if completed
    task_text = todo[1]
    if todo[2]:
        task_text = f"~~{task_text}~~"
    col1.markdown(task_text)
    
    # Complete/Uncomplete button
    if col2.button("✓" if not todo[2] else "✗", key=f"complete_{todo[0]}"):
        update_todo(todo[0], not todo[2])
        st.rerun()
    
    # Delete button
    if col3.button("🗑️", key=f"delete_{todo[0]}"):
        delete_todo(todo[0])
        st.rerun()

# Instructions
st.markdown("---")
st.markdown("**Instructions:**")
st.markdown("- To add a new todo, type it in the text box and click 'Add'")
st.markdown("- To mark a todo as complete/incomplete, click the ✓/✗ button")
st.markdown("- To delete a todo, click the 🗑️ button")
