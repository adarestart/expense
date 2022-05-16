
import React, { Component } from "react";
import ReactEcharts from "echarts-for-react";
import axios from 'axios';

export default class AddButton extends React.Component {

    state = {
        balance:"",
        name:""

    }
  
    componentDidMount() {
        axios.get(`/api/expense_categories/`)
        .then(response => {
            console.log(response.data)
            //this.setState ({ balance: response.data.data.balance});
            //this.setState ({ name: String(response.data.data.firstName)+" "+String(response.data.data.lastName)});
        })
    }
    
    render() {
     
      //console.log(balance)
      /*<form name="expense" onSubmit={this.handleInvoice}>
              <label>Amount
                <input type="text" name="end_date" onChange={this.handleCard} />
              </label>
              <label>
                Category 
                <select onChange={this.handleChoice}>
                  <option value="1">Credit Card</option>
                  <option value="2">Debit Card</option>
                </select>
              </label>
              <button type="submit">Submit a Expense</button>
            </form>
*/
      return (
        <form name="expense">
        <label>Amount
          <input type="text" name="end_date"  />
        </label>
        <label>
          Category 
          <select >
            <option value="1">Credit Card</option>
            <option value="2">Debit Card</option>
          </select>
        </label>
        <button type="submit">Submit a Expense</button>
      </form>
        
        
        
        
  
    )}
}


