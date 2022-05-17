#!/usr/bin/node

const fs = require('fs');
fs.readFile('./cisfun',
    {encoding:'utf8', flag:'r'},
    function(err, data) {
        if(err)
            console.log(err);
        else
            console.log(data);
    });