#!/bin/bash

if [ "$1" == "-h" ] ; then
    echo "$0 usage: to download, and setup a Mongo database on an EC2 instance for remote access.
  Arguments:
    1: name of database to create
    2: name of user to create
    3: password for user creation"
    exit 0
fi

echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list

sudo apt-get update
sudo apt-get install -y --allow-unauthenticated mongodb-org

sudo service mongod start
sleep 2
mongoimport --db tweets --collection coffee --file coffee-tweets.json
mongo tweets --eval "db.createUser({user:'$2',pwd:'$3',roles:[{role:'readWrite',db:'tweets'}]})"
mongo $1 --eval "db.createUser({user:'$2',pwd:'$3',roles:[{role:'readWrite',db:'$1'}]})"

sudo tee /etc/mongod.conf >/dev/null <<EOF
storage:
  dbPath: /var/lib/mongodb
  journal:
    enabled: true
systemLog:
  destination: file
  logAppend: true
  path: /var/log/mongodb/mongod.log
net:
  port: 27017
security:
  authorization: 'enabled'
EOF

sudo service mongod restart
