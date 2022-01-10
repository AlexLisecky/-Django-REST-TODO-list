import React from 'react'
import { useParams } from 'react-router-dom'


const ProjectsDetailItem = ({ item }) => {
    console.log(item)
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.title}</td>
            <td>{item.link}</td>
            <td>{item.users}</td>
        </tr>
    )
}


const ProjectsDetailList = ({ items }) => {

    let { id } = useParams();
    let filtered_items = items.filter((item) => item.id == id)
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>AUTHOR</th>
            </tr>
            {filtered_items.map((item) => <ProjectsDetailItem item={item} />)}
        </table>
    )
}

export default ProjectsDetailList