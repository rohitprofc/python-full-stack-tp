import React from "react";
import { Component } from "react";

class StudentName extends Component {
    render() {
        return(
            <div>
                <h3><u>Details of Us</u></h3>
            </div>
        )
    }
}

class List extends Component {
    render() {
        return(
            <ul>
                <li><h4>{this.props.data.name}: {this.props.data.roll}</h4></li>
            </ul>
        )
    }
}

export default class ReactState extends Component {
    constructor() {
        super();
        this.state = {
            data: [
                {
                    "name": "Rohit",
                    "roll": 51
                },
                {
                    "name": "Rushi",
                    "roll": "L3"
                }
            ]
        }
    }

    render() {
        return (
            <div>
                <h1>React State</h1>
                <StudentName />
                <ul>
                    {this.state.data.map((item) => <List data={item} />)}
                </ul>
            </div>
        )
    }
}