const express = require('express')
const fileupload = require('express-fileupload')
const cors = require('cors')
const spawn = require('child_process').spawn

const app=express()
app.use(express.json())
app.use(fileupload())
app.use(cors())

app.get('/',(req,res)=>{
    res.send("Hello from server")
})
app.post('/uploadFiles',(req,res)=>{
    req.files.grades.mv('./input/grades.csv')
    req.files.subject_master.mv('./input/subjects-master.csv')
    req.files.names_roll.mv('./input/names-roll.csv')
    if(req.body.isSignature=='true')
        req.files.signature.mv('./input/signature.jpg')
    if(req.body.isStamp=='true')
        req.files.stamp.mv('./input/mohar.jpg')
    res.status(200).send("Successful")
})

app.post('/check-roll',(req,res)=>{
    var dataToSend
    const python = spawn('python3', ['roll_checker.py',req.body.startRoll,req.body.endRoll]);
    
    python.stdout.on('data', function (data) {
        dataToSend = data.toString()
    });
    
    python.on('close', (code) => {
        if(code || dataToSend)
        {
            console.log(`Invalid roll`,code,dataToSend)
            res.sendStatus(422)
        }
        else
        {
            console.log("Valid roll ")
            res.sendStatus(200)
        }
    })
})

app.get('/download',(req,res)=>{
    var dataToSend
    var python = spawn('python3', ['generate_zip.py'])
    python.stdout.on('data', function (data) {
        dataToSend = data.toString()
    });
    python.on('close', (code) => {
        res.status(200).sendFile(__dirname+'/transcriptIITP.zip')
    })
})

app.post('/transcript/entireRange', (req,res)=>{
    var dataToSend
    res.sendStatus(202)
    var python = spawn('python3', ['btech.py',"All",req.body.sign,req.body.stamp]);
    
    python.stdout.on('data', function (data) {
        dataToSend = data.toString()
    });
    
    python.on('close', (code) => {
        console.log("All btech generated successfully")
        var python1 = spawn('python3', ['remaining.py',"All",req.body.sign,req.body.stamp]);
    
        python1.stdout.on('data', function (data) {
            dataToSend = data.toString()
        });
        
        python1.on('close', (code) => {
            console.log("All remaining generated successfully")
            res.app.locals.status = "Done"
        })
    })
})

app.get('/transcript/entireRange/status', (req,res)=>{
    if(res.app.locals.status==="Done"){
        console.log("Entire transcript generated successfully...")
        res.sendStatus(200)
        res.app.locals.status=undefined
    }
    else
        res.sendStatus(202)
})

app.post('/transcript/:course/:roll',(req,res)=>{
    var dataToSend
    var python
    if(req.params.course=='01')
        python = spawn('python3', ['btech.py',req.params.roll,req.body.sign,req.body.stamp]);
    else
        python = spawn('python3', ['remaining.py',req.params.roll,req.body.sign,req.body.stamp]);
    
    python.stdout.on('data', function (data) {
        dataToSend = data.toString()
    });
    
    python.on('close', (code) => {
        if(code || dataToSend)
        {
            console.log("Unsuccessfull",req.params.roll)
            res.send({
                status: '0',
                roll: req.params.roll
            })
        }
        else
        {
            console.log("Successfull ",req.params.roll)
            res.send({
                status: '1',
                roll: req.params.roll
            })
        }
    })
})

app.listen((process.env.PORT || 5000),()=>{
    console.log("Backend started at ",(process.env.PORT || 5000))
})