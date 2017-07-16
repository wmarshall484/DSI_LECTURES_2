echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

sudo apt-get update
sudo apt-get install -y --allow-unauthenticated mongodb-org

sudo service mongod start
sleep 3
mongo lecture --eval "db.createUser({user:'class',pwd:'gingerbreadman',roles:[{role:'readWrite',db:'lecture'}]})"

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
