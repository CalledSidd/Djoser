import React from "react";
import { useState } from "react";
import { Link, redirect } from "react-router-dom";
import { Connect } from "react-redux";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import "bootstrap/dist/css/bootstrap.min.css";


const Login = () => {
  const [formData, setFormdata] = useState({ email : '', password : ''})
  const {email, password} = formData
  const onChange = e => setFormdata({...formData, [e.target.name] : e.target.value});
  const onSubmit = e => {
    e.preventDefault();

  }


  return (
    <div className="container pt-5">
    <div className="container pt-">
    <div className="row justify-content-center mt-3 mb-3 pt-5">
      <div className="col-md-5">
        <h3>Login</h3>
        <br/>
        <Form onSubmit={e => onSubmit(e)}>
            <div className="mb-3">
              <label class="form-label" for="form2Example2">Username</label>
              <input name="username" type="text" controlId="formBasicUsername" class="form-control" placeholder="Username" value={email} onChange={e => onChange(e)} required/>
            </div>
            <div className="mb-3">
              <label class="form-label" for="form2Example2">Password</label>
              <input type="password" name="password" controlId="formBasicPassword" class="form-control" placeholder="Password" value={password} onChange={e => onChange(e)} minLength='5' required/>
            </div>
          <Button variant="dark" type="submit">
            Login
          </Button>
          <Link to='/signup'>
            <Button variant="dark-outline">
              <span>SignUp</span>
              </Button>
            </Link>
            <p>Forgot Your Password?
              <Link to='/reset-password'>Reset Password</Link>
            </p>
        </Form>
      </div>
      </div>
    </div>
  </div>
  )
}

export default Login