const mysql = require('mysql');
let express = require("express");
const fs = require("fs-extra");
const { request, response } = require('express');
const app = express();

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "root",
    database: 'carRentalJs'
});



app.get('/addCar/:carname/:brandname/:carhp/:enginecapacity/:manufacturedate', function(request, response) {
    var sql = "INSERT INTO CARS (NAME, BRAND, HP, ENGINE_CAPACITY,MANUFACTURE_DATE) VALUES (?)";
    var values = [request.params.carname, request.params.brandname, request.params.carhp, request.params.enginecapacity, request.params.manufacturedate];
    con.query(sql, [values], function(err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });
    return response.send('Car ' + request.params.brandname + ' succesfully inserted')
})


app.get('/showCars', function(request, response) {
    con.query("SELECT * FROM CARS", function(err, result, fields) {
        if (err) throw err;
        console.log(result);
    });
    return response.send('Record succesfully showed')
})

app.get('/removeAllCars', function(request, response) {
    con.query("DELETE FROM cars;", function(err, result, fields) {
        if (err) throw err;
        console.log(result);
    });
    return response.send('Records succesfully deleted')
})

app.get('/addUser/:name/:surname/:pesel', function(request, response) {
    var sql = "INSERT INTO USER (NAME, SURNAME, PESEL) VALUES (?)";
    var values = [request.params.name, request.params.surname, request.params.pesel];
    con.query(sql, [values], function(err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });
    return response.send('User ' + request.params.name + request.params.surname + ' succesfully inserted')
})

app.get('/showAllusers', function(request, response) {
    con.query("SELECT * FROM USER", function(err, result, fields) {
        if (err) throw err;
        console.log(result);
    });
    return response.send('Record succesfully showed')
})

app.get('/removeAllCars', function(request, response) {
    con.query("DELETE FROM USER;", function(err, result, fields) {
        if (err) throw err;
        console.log(result);
    });
    return response.send('Records succesfully deleted')
})

app.get('/addUser/:name/:surname/:pesel', function(request, response) {
    var sql = "INSERT INTO USER (NAME, SURNAME, PESEL) VALUES (?)";
    var values = [request.params.name, request.params.surname, request.params.pesel];
    con.query(sql, [values], function(err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });
    return response.send('User ' + request.params.name + request.params.surname + ' succesfully inserted')
})

app.get('/showAllusers', function(request, response) {
    con.query("SELECT * FROM USER", function(err, result, fields) {
        if (err) throw err;
        console.log(result);
    });
    return response.send('Record succesfully showed')
})

app.get('/removeAllCars', function(request, response) {
    con.query("DELETE FROM USER;", function(err, result, fields) {
        if (err) throw err;
        console.log(result);
    });
    return response.send('Records succesfully deleted')
});

app.get('/addRental/<carId>/<userId>', function(request, response) {
    var sql = "INSERT INTO RENTAL (CAR_ID, USER_ID) VALUES (?)";
    var values = [request.params.carId, request.params.userId];
    con.query(sql, [values], function(err, result) {
        if (err) throw err;
        console.log("Number of records inserted: " + result.affectedRows);
    });
    return response.send('Rental succesfully inserted')
})

app.get('/showRentals', function(request, response) {
    con.query("SELECT * FROM RENTAL", function(err, result, fields) {
        if (err) throw err;
        console.log(result);
    });
    return response.send('Record succesfully showed')
})

app.get('/removeAllRentals', function(request, response) {
    con.query("DELETE FROM RENTAL;", function(err, result, fields) {
        if (err) throw err;
        console.log(result);
    });
    return response.send('Records succesfully deleted')
});





app.listen(3000, function() { // odpalenie serwera i nasłuchiwanie na port 3000
    console.log('Server is listening on port 3000');
});