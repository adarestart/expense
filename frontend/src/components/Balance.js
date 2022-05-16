import React, { Component } from "react";
import { Row, Col, Card,Container, CardGroup,ListGroup,Table,Button, Breadcrumb,ButtonGroup} from 'react-bootstrap';
import ReactEcharts from "echarts-for-react";
import axios from 'axios';
import '../App.css';
import moment from 'moment';

export default class Balance extends React.Component {

    state = {
        balance:"",
        name:"",
        
        expense_categories:[],
        income_categories:[],
        
        queries:[],
        cat_queries:[],

        choice:"",
        amount:0,
        
        month:[],
        month_amount:[],

        category:[],

        expenses:[],
        date:[]
    }
  
    componentDidMount() {
        this.refreshList();
        axios.get(`/api/expense_categories/`)
        .then(response => {
            this.setState ({ expense_categories: response.data.data},() => {
          });
        })
        axios.get(`/api/income_categories/`)
        .then(response => {
            
            this.setState ({ income_categories: response.data.data},() => {
              /*console.log(
                "Status Updated: ",
                this.state.categories
              );*/});
        })
    }
    refreshList = () =>{
      axios.get(`/api/users/1/`)
        .then(response => {
            console.log(response.data.data.balance)
            this.setState ({ balance: response.data.data.balance});
            this.setState ({ name: String(response.data.data.firstName)+" "+String(response.data.data.lastName)});
        })
        axios.get(`/api/expenses/`)
        .then(response => {
            console.log(response.data.data);
            this.setState ({ expenses: response.data.data},() => {
            });
            })
        
        axios.get(`/api/queries/`)
        .then(response => {
            console.log(response.data.data);
            this.setState ({ queries: response.data.data},() => {
              });
        })
        axios.get(`/api/cat_queries/`)
        .then(response => {
            console.log(response.data.data);
            this.setState ({ cat_queries: response.data.data},() => {
              });
        })
    }
    handleExpense = event => {
      event.preventDefault();
      const date1 = moment().format('YYYY-MM-DD');
      console.log(date1)
      axios.post(`/api/expenses/`, {
        id:1,
        user_id:1,
        description: "This is a test",
        amount:this.state.amount,
        date: date1,
        category_id: Number(this.state.choice)
      })
        .then(res => {
          // Refresh Page each time when posting an expense
          this.refreshList();
          console.log(res);
          console.log(res.data);
        })
    }
    handleIncome = event => {
      event.preventDefault();
      const date1 = moment().format('YYYY-MM-DD');
      console.log(date1)
      axios.post(`/api/incomes/`, {
        id:1,
        user_id:1,
        description: "just a test",
        amount:this.state.amount,
        date:date1,
        category_id: Number(this.state.choice)
      })
        .then(res => {
          // Refresh Page each time when posting an income
          this.refreshList();
          console.log(res);
          console.log(res.data);
        })
    }
    handleChoice = event => {
      console.log(event.target.value);
      this.setState({ choice: event.target.value });
      console.log(this.state.choice);
    }
    handleAmount = event => {
      console.log(event.target.value);
      this.setState({ amount: event.target.value });
      console.log(this.state.amount);
    }
    handleDate = event => {
      console.log(event.target.value);
      this.setState({ date: event.target.value });
      console.log(this.state.date);
    }
    render() {

      var balance = String(this.state.balance);
      var name = String(this.state.name)
      
      this.state.month = this.state.queries.map(home => home.date); 
      this.state.month_amount = this.state.queries.map(home => home.amount); 
      
      this.state.category=this.state.cat_queries.map(home => ({name:home.category, value:home.amount})); 
      //console.log(this.state.category)
      /*<label>Date
          <input type="text" name="date" onChange={this.handleDate.bind(this)}/>
        </label>*/

      return (
        <Container fluid>
         

        <Row className="justify-content-md-center">
          <Col>
          <ReactEcharts
            option={{
                title: {
                    text: 'Balance \n $'+String(balance),
                    left: 'center',
                    top: 'center'
                  },
              series: [{ 
                type:'pie',
                data: [{
                    value: 335,
                    name: name
                  }],
                radius: ['50%', '70%']
              }]
            }}
          />
          </Col>
          <Col xs>
          <ReactEcharts
            option = {{
              series: [
                {
                  type: 'pie',
                  data: this.state.category
                } ]
              }}
          />
          </Col>
          <Col xs={12} md={8}>
          <ReactEcharts
            option = {{
              xAxis: {
                data: this.state.month
              },
              yAxis: {},
              series: [
                {
                  type: 'bar',
                  data: this.state.month_amount,
                  barGap: '20%',
                  barCategoryGap: '40%'
                }
              ]
            }}
          />
            
          </Col>
        </Row>
        <Row className="justify-content-center" md="auto">
        <ListGroup>
                 
        </ListGroup>
        </Row>
        <Row className="justify-content-center" md="auto">
          <CardGroup>
          <Card style={{ width: '14rem' }}>
            <Card.Body>
              <Card.Title>Submit an Expense</Card.Title>
              <Card.Text></Card.Text>
              <form name="expense" onSubmit={this.handleExpense}>
                <label>Amount
                  <input type="text" name="amount" onChange={this.handleAmount.bind(this)}/>
                </label>
              
                <label>
                  Category 
                  <select onChange={this.handleChoice.bind(this)}>
                  {this.state.expense_categories.map(home => <option value={home.id}>{home.name}</option>)}
                    
                  </select>
                </label>
                <button type="submit">Submit</button>
              </form>
              <Card.Text></Card.Text>
            </Card.Body>
          </Card>
          <Card style={{ width: '14rem' }} right="center">
          <Card.Body>
              <Card.Title>Submit an Income</Card.Title>
              <Card.Text></Card.Text>
              <form name="income" onSubmit={this.handleIncome}>
                <label>Amount
                  <input type="text" name="amount" onChange={this.handleAmount.bind(this)}/>
                </label>
                
                <label>
                  Category 
                  <select onChange={this.handleChoice.bind(this)}>
                  {this.state.income_categories.map(home => <option value={home.id}>{home.name}</option>)}
                    
                  </select>
                </label>
                <button type="submit">Submit</button>
              </form>
              <Card.Text></Card.Text>
            </Card.Body>
          </Card>
          </CardGroup>
        </Row>
      </Container>

    )}
}

  