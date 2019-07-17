const express = require('express')
const fetch = require('node-fetch')
const app = express()
 
app.get('/', function (req, res) {

    fetch('http://172.18.0.2/bench').then(res => res.json()).then(function(data) {
        res.send(data)  
      });
})
 
app.listen(3000)