const express = require('express');
const app = express();
const mysql = require('mysql');
const PORT = 3030;
const cors = require('cors');
const {encrypt,decrypt} = require('./EncryptionHandler');

app.use(cors());
app.use(express.json());

const db = mysql.createConnection({
    user: 'root',
    host: 'localhost',
    password: 'password' ,
    database: 'passwordmanager'
});

app.post('/addpass', (req, res) => {
    const {password, title} = req.body;

    const hashPass = encrypt(password);
    
    db.query("INSERT INTO passwords (password, title, iv) VALUES (?,?,?)", 
    [hashPass.password, title, hashPass.iv],
    (err, result) => {
        if (err){
            console.log(err);
        }
        else{
            res.send("Worked");
        }   
});
});

app.listen(PORT, ()=> {
    console.log('Server is on.... ');
});