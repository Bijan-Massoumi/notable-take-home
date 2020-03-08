import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Planner from './components/Calendar'

function App() {
  let containerStyle = {
    marginTop: window.innerHeight * .10,
  }
  return (
    
    <div className="app" style = {containerStyle}>
      <Container >
          <Planner apiEndpoint="http://127.0.0.1:5000/api/"/>
      </Container>
    </div>
  );
}

export default App;
