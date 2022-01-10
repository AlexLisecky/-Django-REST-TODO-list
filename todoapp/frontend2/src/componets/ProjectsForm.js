import React from 'react'


class ProjectsForm extends React.Component {
    constructor(props) {
      super(props)
//      console.log(props.users['results'][0]['id'])
      this.state = {title: '', link:'', user: 0}
    }

    handleChange(event)
    {
        this.setState(
                {
                    [event.target.name]: event.target.value
                }
            );
    }

    handleSubmit(event) {
      this.props.createProject(this.state.name,this.state.link, this.state.user)
      event.preventDefault()
    }

    render() {
      return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
            <div className="form-group">
            <label for="login">name</label>
                <input type="text" className="form-control" name="name" value={this.state.name} onChange={(event)=>this.handleChange(event)} />
            </div>

            <div className="form-group">
            <label for="user">user</label>
                <input type="number" className="form-control" name="user" value={this.state.user} onChange={(event)=>this.handleChange(event)} />
            </div>
            <div className="form-group">
            <label for="user">link</label>
                <input type="text" className="form-control" name="link" value={this.state.link} onChange={(event)=>this.handleChange(event)} />
            </div>
          <input type="submit" className="btn btn-primary" value="Save" />
        </form>
      );
    }
  }

  export default ProjectsForm
