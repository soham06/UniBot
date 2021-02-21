// initialize/declare variables
const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);
users = [];
connections = [];
http.listen(process.env.PORT || 3000);
console.log("Server running...");
app.get('/', function(req, res) {
    res.sendFile((__dirname + '/index.html'));
});

// Make the chat box ineractive with the following functions:

// Connect to the server
io.sockets.on('connection', function(socket){
    connections.push(socket);

    // Disconnect from the server
    socket.on('disconnect', function(data){
        users.splice(users.indexOf(socket.username), 1);
        updateUsernames();
        connections.splice(connections.indexOf(socket), 1);
    });

    // Send the Message
    socket.on('send message', function(data){
        io.sockets.emit('new message', {msg: data, user: socket.username})
    });

    // Add New user
    socket.on('new user', function(data, callback){
        callback(true);
        socket.username = data;
        users.push(socket.username);
        updateUsernames();
    });

    // username function
    function updateUsernames(){
        io.sockets.emit('get users', users);
    }
});