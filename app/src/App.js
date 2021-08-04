import React, { Component } from 'react';
import { BrowserRouter, Link, Route, Switch } from 'react-router-dom';
import './App.css';
import CreateBudget from './routes/CreateBudget';
import Dashboard from './routes/Dashboard';
import Home from './routes/Home';
import Landing from './routes/Landing';
class App extends Component {
  render() {
    return (
      <BrowserRouter>

        <div className="App">
          <nav>
            <ul>
              <li>
                <Link to="/">Landing</Link>
              </li>
              <li>
                <Link to="/home">Home</Link>
              </li>
              <li>
                <Link to="/createBudget">Create Budget</Link>
              </li>
              <li>
                <Link to="/dashboard">Dashboard</Link>
              </li>
            </ul>
          </nav>

          <Switch>
            <Route exact path="/">
              <Landing />
            </Route>
            <Route path="/home">
              <Home />
            </Route>

            <Route path="/createBudget">
              <CreateBudget />
            </Route>

            <Route path="/dashboard">
              <Dashboard />
            </Route>
          </Switch>

        </div>
      </BrowserRouter>

    );
  }
}


export default App;