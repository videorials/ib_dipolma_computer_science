// load JSON file from server...
const fs = require('fs');
let data = fs.readFileSync('words.json');
let words = JSON.parse(data);

// import express module and create server instance...
const express = require('express');
const app = express();

// direct node to static pages
app.use(express.static('views'));

// create routes...
app.get('/', (req, res) => {
  res.render('index')
})
app.get('/all', (req, res) => {
  res.send(words);
})
app.get('/add/:word/:score', (req, res) => {
  let data = req.params;
  let word = data.word;
  let score = data.score;
  words[word] = score;

  // saves new data to JSON file...
  data = JSON.stringify(words, null, 2);
  fs.writeFile('words.json', data, (err) => {

    if (err)
      console.log(err);
    else {
      console.log('all set...');
    }

    let reply = {
      word: word,
      score: score,
      status: "success"
    }

    res.send(reply);

  })

})

// set server to listen on port 3000
app.listen(3000, () => { console.log('listening...') }); 