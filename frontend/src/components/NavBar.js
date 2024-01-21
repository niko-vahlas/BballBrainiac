import React from 'react';
import logo from '../logo.png'; // Adjust the path as necessary
import '../NavBar.css';

const Navbar = () => {
  return (
    <nav className="nav">
      <div className="row">
        <div className="img--wrapper">
          <img src={logo} alt="BBallBraniac Logo" />
        </div>

        <div className="title--wrapper">
          <h1>BBallBraniac</h1>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
