import React, { Component } from "react";
import ReactEcharts from "echarts-for-react";
import axios from 'axios';

export default class Charts extends React.Component {

    state = {
        balance:"",
        name:""

    }
  
    componentDidMount() {
        axios.get(`/api/users/1/`)
        .then(response => {
            console.log(response.data.data.balance)
            this.setState ({ balance: response.data.data.balance});
            this.setState ({ name: String(response.data.data.firstName)+" "+String(response.data.data.lastName)});
        })
    }
    
    render() {
      //console.log(this.state.vehicles);
      var balance = String(this.state.balance);
      var name = String(this.state.name)
      console.log(balance)
      return (
        
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

        
        
  
    )}
}

  