if [ ! -d "server/node_modules/" ];then
    cd server
    npm install 
    cd ..
fi
if [ ! -d "app/node_modules" ];then
    cd app
    npm install 
    cd ..
fi
cd docker
docker-compose up --remove-orphans
docker-compose stop