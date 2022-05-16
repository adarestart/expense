import logo from './logo.svg';
import './App.css';
import { Row, Col, Card,Container, Table,Button, Breadcrumb,ButtonGroup} from 'react-bootstrap';
import moment from 'moment';
import Balance from './components/Balance.js';


function App() {
  //<img src={logo} className="App-logo" alt="logo" />
  return (
    <div className="App">
     <Balance/>
    </div>
  );
}

export default App;
