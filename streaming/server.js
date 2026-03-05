const express = require('express');
const http = require('http');
const { Server } = require('socket.io')
const cors = require('cors');

const app = express();
app.use(cors());

const server = http.createServer(app);
const io = new Server(server, {
    cors: {
        origin: "http://localhost:3000",
        methods: ["GET", "POST"],
    }
});

setInterval(() => {
    const message = `Nueva actualización del tutor: ${new Date().toLocaleTimeString()}`;
    console.log("Enviando mensaje:", message);
    
    io.emit("public-notifications", { message: message }); 
}, 10000);

server.listen(4000, () => {
    console.log('Servidor de streaming en puerto 4000');
});