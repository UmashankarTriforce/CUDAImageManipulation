const express = require('express')
const fetch = require('node-fetch')
const app = express()

app.get('/', function(req, res) {

    fetch('http://172.19.1.2/bench', {
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(req.query)
    }).then(res => res.json()).then(function(data) {
        res.header("Access-Control-Allow-Origin", "*");
        res.header("Access-Control-Allow-Headers", "X-Requested-With");
        res.send(data)
    });
})


app.listen(80)