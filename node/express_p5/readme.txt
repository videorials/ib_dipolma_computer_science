Reference...
https://youtu.be/SccSCuHhOw0
https://www.simplilearn.com/tutorials/nodejs-tutorial/nodejs-express

1) download & install Node.js & NPM (Node Package Manager)...

	https://nodejs.org/en/download/

2) open cmd prompt...

	>> check version | node -v
	>> download latest version of npm | npm install -g npm

3) open vs code & new terminal (Ctrl ö)...

	>> create a new directory		| mkdir new_express_project
	>> enter new directory			| cd new_express_project
	>> create basic json package	| npm init -y
	>> install express library		| npm i express

	// automatically monitor and restart server when specified file is modified...
	>> install nodemon package		| npm i --save-dev nodemon


4) modify package.json to include...

	"scripts": {
		"devStart": "nodemon server.js"
	},

5) create server.js file in root folder and add...

	const express = require('express') // import express module
	const app = express()              // create a server instance
	app.listen(3000)                   // set server to listen on port 3000

6) open terminal (Ctrl ö)...

	run nodemon (runs server.js) | npm run devStart

7) Open browser and type the following in the address bar (with no routes for the root it should display Cannot GET /):
	localhost:3000