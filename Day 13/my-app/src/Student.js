import React, { Component } from "react";

export default class Student extends Component {
    render() {
        return (
            <section className="props">
            <h1>Name: {this.props.name}</h1>
            <h1>Email: {this.props.email}</h1>
            </section>
        )
    }
}