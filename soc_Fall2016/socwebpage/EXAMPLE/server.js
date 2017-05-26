var express = require('express');
var bodyParser = require('body-parser');
var path = require('path');
var passport = require('passport');
var session  = require('express-session');
var cookieParser = require('cookie-parser');
var flash    = require('connect-flash');

var app = express();
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'public')));
var server = app.listen(3000, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Example app listening at http://%s:%s", host, port);
});
app.use(express.static('public'));
var urlencodedParser = bodyParser.urlencoded({ extended: false })
app.use(cookieParser());
app.use(session({ secret: 'keyboard cat', resave: false, saveUninitialized: false }))

app.use(bodyParser.urlencoded({ extended: false }));

app.get("/customerRetension",function(req,res){
	res.render('index',{});
});

 
