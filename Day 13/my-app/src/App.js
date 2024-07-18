import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import ReactState from './ReactState'

import './App.css';
import logo from './logo.svg'
import ClassComponent from './ClassComponent';
import FunctionalComponent from './FunctionalComponent';
import Student from './Student';
import Profile from './MyProfile/Profile';

function App() {

  function Head() {
    return (
      <Row>
        <Col>
          <img src={logo} className='App-logo' alt='logo' />
        </Col>
      </Row>
    )
  }

  return (
    <div className='App'>
      <Head />

      <Container>
        <Row>
          <h1 style={{ color: "yellow" }}>Day 13</h1>
          <Col>
            <ClassComponent />
            <FunctionalComponent />
          </Col>

          <Col>
            <Student name="Rohit" email="rohitprofc@gmail.com" />
            <Button variant="primary" onClick={() => alert('Made with Bootstrap')}>Hire Me</Button>
          </Col>
        </Row>
        <br /><hr /><br />
        <Row>
          <h1 style={{ color: "yellow" }}>Day 16</h1>
          <Col>
            <ReactState />
          </Col>
          <Col>
            <h1>Routes</h1>
            <Profile />
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default App;
