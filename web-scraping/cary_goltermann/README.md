## Interactive Mongo Database Setup

Included in this directory is a shell script, `remoteMongoSetup.sh` that can be run on an EC2 instance running Ubuntu 16.04.

Once set up you can live code in class, performing queries on the remote database while your class follows along. Connections can be made from both the Mongo shell and from pymongo.

## Setup Script

**Note: both the setup script and the coffee-tweets.json files should be copied to the EC2 instance before proceeding.**

The script, `remoteMongoSetup.sh`, to be run on an EC2 instance, accepts three arguments. The first is to name the database it will create, the second and third are to create a user and password, respectively, for remote login.

Usage:
```
bash remoteMongoSetup.sh <database_name> <user_name> <password>
```

Example usage:
```
bash remoteMongoSetup.sh lecture class gingerbreadman
```

When the script is run it will download Mongo, create a database with the name passed and credentials to login as specified, setup the configurations so that remote login works and launch the Mongo daemon.

For remote login to work port `27017` needs to be open in the security settings for the EC2 instance. If the port is open after the script is run you will need to restart the Mongo daemon with:

```
sudo service mongod restart
```

## Remote Access

You will need the public IP address to remotely login to the database on the Mongo server.

### Mongo Shell

Connecting to the remote server with the Mongo shell can be done with:

```
mongo mongodb://<user>:<password>@<ip_address>:27017/<database_name>
```

If the IP address of my EC2 instance was 1.2.3.4 then the command to run, continuing from the example above, would be:

```
mongo mongodb://class:gingerbreadman@1.2.3.4:27017/lecture
```

If all is working correctly you should drop into a Mongo shell that looks something like:

```
MongoDB shell version v3.4.6
connecting to: mongodb://class:gingerbreadman@35.166.212.160:27017/lecture
MongoDB server version: 3.4.6
> 
```

### PyMongo

Connecting to the remote server with `pymongo` can be done from a python REPL with:

```python
from pymongo import MongoClient
client = MongoClient("mongodb://<user>:<password>@<ip_address>:27017/<database_name>")
db = client.<database_name>
```

If the IP address of my EC2 instance was 1.2.3.4 then the Python to run, continuing from the example above, would be:

```python
from pymongo import MongoClient
client = MongoClient("mongodb://class:gingerbreadman@1.2.3.4:27017/lecture")
db = client.<database_name>
```
