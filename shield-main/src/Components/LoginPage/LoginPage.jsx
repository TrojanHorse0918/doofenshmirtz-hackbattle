import React from 'react'
import './loginpage.css'
import '../../app.css'
import {Link} from 'react-router-dom'

import logo from '../../LoginAssets/shieldLogo.png'
import bg from '../../LoginAssets/loginbg.png'
import {AiOutlineSwapRight} from 'react-icons/ai'
import {BsFillPersonFill} from 'react-icons/bs'

const LoginPage = () => {
  const backgroundStyle = {
    backgroundImage: `url(${bg})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
  };
  return (
    <div className='loginPage flex' style={backgroundStyle}>
      <div className='container flex'>

        <div className="formDiv flex">
          <div className="headerDiv">
            <h3>Login <BsFillPersonFill/></h3>
            <p className='textDiv'>Hello, Welcome back!</p>
            <img src={logo} alt='Logo'/>
          </div>

          <form action='' className='form grid'>
            
            <div className="inputDiv">
              <div className="input flex">
                <input type='text' id='username' placeholder='Email Address'/>
              </div>
            </div>

            <div className="inputDiv">
              <div className="input flex">
                <input type='password' id='password' placeholder='Password'/>
              </div>
            </div>

            <button type='submit' className='btn flex'>
              <span>Login</span>
              <AiOutlineSwapRight className='icon'/>
            </button>

            <a href='/home'>Home</a>

            <span className='forgotPassword'>
              <a href="">Forgot password?</a>
            </span>

            <span className='registerBtn'>
              Not a member yet ?  <a href='/register'>Create Account</a> {/* click here to navigate to register page*/}
            </span>

          </form>
        </div>

      </div>
    </div>
  )
}

export default LoginPage
