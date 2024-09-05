function addTodo() {
    const todoInput = document.getElementById('todo-input');
    const todoList = document.getElementById('todo-list');

    if (todoInput.value.trim() !== '') {
        const listItem = document.createElement('li');
        listItem.className = 'todo-item';
        
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.onclick = () => listItem.classList.toggle('completed');
        
        const text = document.createElement('span');
        text.textContent = todoInput.value;
        
        const removeButton = document.createElement('button');
        removeButton.textContent = '제거하기';
        removeButton.onclick = () => todoList.removeChild(listItem);
        
        listItem.appendChild(checkbox);
        listItem.appendChild(text);
        listItem.appendChild(removeButton);
        
        todoList.appendChild(listItem);
        todoInput.value = '';
    }
}
