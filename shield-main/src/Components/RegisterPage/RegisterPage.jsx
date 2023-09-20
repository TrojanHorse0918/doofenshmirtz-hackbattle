import React, { useEffect, useState } from "react";
import { useNavigate } from 'react-router-dom';
import './registerpage.css'
import '../../app.css'
import {Link} from 'react-router-dom'

import logo from '../../LoginAssets/shieldLogo.png'
import bg from '../../LoginAssets/loginbg.png'
import {AiOutlineSwapRight} from 'react-icons/ai'
import {BsFillPersonFill} from 'react-icons/bs'

const RegisterPage = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: ''
  });

  const handleInputChange = (e) => {
    const { id, value } = e.target;
    setFormData({ ...formData, [id]: value });
  };


  const handleSubmit = (e) => {
    const req = {
      "username": formData.username,
      "userEmail": formData.userEmail,
      "userPassword": formData.userPassword
    };
    console.log(req);
    console.log(JSON.stringify(req));

    e.preventDefault();

    fetch('http://localhost:8000/create-record/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(req)
    })
      .then(response => response.json())
      .then(data => {
        console.log('User registered:', data);
        //redirect to login
        navigate('/');
      })
      .catch(error => console.error('Error registering user:', error));
  };

  const backgroundStyle = {
    backgroundImage: `url(${bg})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
  };
  return (
    <div className='registerPage flex' style={backgroundStyle}>
      <div className='container flex'>

        <div className="formDiv flex">
          <div className="headerDiv">
            <h3>Register <BsFillPersonFill/></h3>
            <p className='textDiv'>Hello, Welcome aboard!</p>
            <img src={logo} alt='Logo'/>
          </div>

          <form onSubmit={handleSubmit} className='form grid'>
            
            <div className="inputDiv">
              <div className="input flex">
                <input type='text' id='username' placeholder='Full Name' onChange={handleInputChange}/>
              </div>
            </div>

            <div className="inputDiv">
              <div className="input flex">
                <input type='text' id='userEmail' placeholder='Email Address' onChange={handleInputChange}/>
              </div>
            </div>

            <div className="inputDiv">
              <div className="input flex">
                <input type='password' id='userPassword' placeholder='Password' onChange={handleInputChange}/>
              </div>
            </div>

            <button type='submit' className='btn flex'>
              <span>Register</span>
              <AiOutlineSwapRight className='icon'/>
            </button>

            <a href='/home'>Home</a> {/* to make it easier for me to navigate between pages.*/}

            <span className='forgotPassword'>
              <a href="">Forgot password?</a>
            </span>

          </form>
        </div>

      </div>
    </div>
  )
}

export default RegisterPage
