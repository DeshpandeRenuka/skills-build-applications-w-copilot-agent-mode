
import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import Logo from './components/Logo';

function App() {
  return (
    <Router>
      <div className="App">
        <header>
          <Logo />
          <nav>
            <Link to="/">Home</Link>
            <Link to="/activities">Activities</Link>
            <Link to="/leaderboard">Leaderboard</Link>
            <Link to="/teams">Teams</Link>
            <Link to="/users">Users</Link>
            <Link to="/workouts">Workouts</Link>
          </nav>
        </header>
        <div className="container mt-4">
          <Routes>
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
            <Route path="/" element={
              <div className="text-center">
                <h1>Welcome to <span style={{ color: '#3a86ff' }}>Octofit Tracker</span>!</h1>
                <div style={{ maxWidth: '28rem', margin: '2rem auto', background: '#fff', borderRadius: '12px', boxShadow: '0 2px 8px rgba(58,134,255,0.08)' }}>
                  <div style={{ padding: '2rem' }}>
                    <h5 style={{ color: '#4361ee' }}>Track your fitness, join teams, and compete!</h5>
                    <p>Use the navigation bar above to get started with activities, teams, leaderboards, and more.</p>
                    <Link to="/activities">
                      <button>Get Started</button>
                    </Link>
                  </div>
                </div>
              </div>
            } />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
