import React from 'react';

const Logo = () => (
  <img src={process.env.PUBLIC_URL + '/octofitapp-small.png'} alt="Octofit Tracker Logo" className="logo" />
);

export default Logo;
