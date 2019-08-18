if [ ! -d "node_modules/" ];then
    npm install 
fi
nodemon index.js