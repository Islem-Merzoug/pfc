import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import Header from './components/Header';
import Footer from './components/Footer';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './pages';
import ModelDetails from './pages/modelDetails';
import About from './pages/about';
import Services from './pages/services';
import Contact from './pages/contact';
import SignUp from './pages/signup';
import StepOne from './components/StepOne';

const App = () => {
  return (

    <Router>
        <Navbar />
        <Header />
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/modelDetails' component={ModelDetails} />
          <Route path='/stepOne' component={StepOne} />
          <Route path='/about' component={About} />
          <Route path='/services' component={Services} />
          <Route path='/contact-us' component={Contact} />
          <Route path='/sign-up' component={SignUp} />
        </Switch>
        <Footer />

    </Router>
  );
}

export default App;

