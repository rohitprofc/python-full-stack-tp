import React, { Component } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import Home from './Home';
import About from './About';
import Contact from './Contact';

export default class Profile extends Component {
    render() {
        return(
            <>
            <BrowserRouter>
            <Routes>
                <Route path="/Home" element={<Home/>}></Route>
                <Route path="/About" element={<About/>}></Route>
                <Route path="/Contact" element={<Contact/>}></Route>
            </Routes>
            </BrowserRouter>
            </>
        )
    }
}