import React from 'react';
import { BrowserRouter, Route, Switch, Link } from 'react-router-dom';
import './App.css';
import UserList from './componets/users';
import ProjectList from './componets/projects';
import TodoList from './componets/todos';
import CreateFooter from './componets/footer';
import LoginForm from './componets/auth';
import Cookies from 'universal-cookie'
import axios from 'axios';
import ProjectsForm from './componets/ProjectsForm'

const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': null
        }
    }

    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users', { headers })
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({ users: [] })
            })
        axios.get('http://127.0.0.1:8000/api/todo', { headers })
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({ todos: [] })
            })
        axios.get('http://127.0.0.1:8000/api/project', { headers })
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({ projects: [] })
            })
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({ 'token': token }, () => this.load_data())
    }

    is_authenticated() {
        return !!this.state.token
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({ 'token': token }, () => this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', { username: username, password: password })
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    deleteProject(id) {
    const headers = this.get_headers()
    axios.delete(`http://127.0.0.1:8000/api/project/${id}`, {headers})
        .then(response => {
          this.setState({projects: this.state.projects.filter((project)=>project.id !== id)})
        }).catch(error => console.log(error))
    }

    createProject(name, user) {
    const headers = this.get_headers()
    const data = {name: name, user: user}
    axios.post(`http://127.0.0.1:8000/api/project/`, data, {headers})
        .then(response => {
          let new_project = response.data
          const project = this.state.projects.filter((item) => item.id === new_project.user)[0]
          console.log(project)
          new_project.user = project
          console.log(project)
          this.setState({projects: [...this.state.projects, new_project]})
        }).catch(error => console.log(error))
  }



    render() {
        return (
            <div className='container'>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/project'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/todo'>Todos</Link>
                            </li>
                            <li>
                                <Link to='/project/create'>Create</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/todo' component={() => <TodoList todos={this.state.todos} />} />
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                        <Route exact path='/project' component={() => <ProjectList projects={this.state.projects} deleteProject={(id)=>this.deleteProject(id)} />} />
                        <Route exact path='/project/create' component={() => <ProjectsForm projects={this.state.projects} createProject={(name, user) => this.createProject(name, user)} />} />
//                        <Route exact path='/project/create' component={() => <ProjectsForm />}  />
                        <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>
                <div><CreateFooter /></div>
            </div>
        )
    }
}



export default App;
