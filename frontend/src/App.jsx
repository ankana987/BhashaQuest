import React from 'react';
import{Routes,Route}from'react-router-dom';
import Navbar from'./components/Navbar';import Home from'./pages/Home';import Setup from'./pages/LanguageSelection';import Game from'./pages/Game';import Profile from'./pages/Profile';
export default function App(){return <><Navbar/><Routes><Route path="/" element={<Home/>}/><Route path="/setup" element={<Setup/>}/><Route path="/game" element={<Game/>}/><Route path="/profile" element={<Profile/>}/></Routes></>}
