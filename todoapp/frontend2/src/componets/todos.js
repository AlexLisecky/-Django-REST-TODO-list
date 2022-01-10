import React from 'react'


const TodoItem = ({ todo }) => {
    return (
        <tr>
            <td>
                {todo.id}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.is_active}
            </td>
            <td>
                {todo.project_name}
            </td>
            <td>
                {todo.user}
            </td>
        </tr>
    )
}

const TodoList = ({ todos }) => {
    return (
        <table className='user__table'>
            <th>
                Id
            </th>
            <th>
                Text
            </th>
            <th>
                Is active
            </th>
            <th>
                Project name
            </th>
            <th>
                User name
            </th>
            {todos.map((todo) => <TodoItem todo={todo} />)}
        </table>
    )
}


export default TodoList