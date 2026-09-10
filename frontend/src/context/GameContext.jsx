import React, { createContext, useContext, useEffect, useMemo, useState } from 'react';

//import{createContext,useContext,useState}from'react';
const C=createContext();
const blank={xp:0,streak:1,completed:[],badges:[],attempts:0,learned:[],scores:[]};export function GameProvider({children}){const[settings,setSettings]=useState({nativeLanguage:'en',targetLanguage:'hi',area:'garden'});const[progress,setProgress]=useState(()=>{try{return JSON.parse(localStorage.getItem('bq-progress'))||blank}catch{return blank}});const[currentLevelId,setCurrentLevelId]=useState(1);const[currentChallengeIndex,setCurrentChallengeIndex]=useState(0);const save=x=>{setProgress(x);localStorage.setItem('bq-progress',JSON.stringify(x))};const record=(score,word)=>save({...progress,xp:progress.xp+(score>=90?20:score>=70?10:0),attempts:progress.attempts+1,learned:[...new Set([...progress.learned,word])],scores:[...progress.scores,score]});const complete=l=>save({...progress,xp:progress.xp+l.xp,completed:[...new Set([...progress.completed,l.id])],badges:[...new Set([...progress.badges,l.badge])]});return <C.Provider value={{settings,setSettings,progress,currentLevelId,setCurrentLevelId,currentChallengeIndex,setCurrentChallengeIndex,record,complete}}>{children}</C.Provider>}export const useGame=()=>useContext(C);


