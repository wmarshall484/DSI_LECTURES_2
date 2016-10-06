## MongoDB

MongoDB is an example of a NoSQL database. The key distinguishing feature of such a NoSQL database is that we are not constrained by the relational structure and schemas that characterize relational databases. As such, each document in a non-relational database can take a different structure and contain different information. This makes it a very flexible tool for storing large amounts of raw information without defining in advance the type or structure of that information.

In the lecture & assignments, we will be working with MongoDB directly as well as through Python with a module called `pymongo`. The instructions below outline how to get setup.

### Installing MongoDB

For greater detail on the installation process and options, refer to the [MongoDB documentation for installation on OS X](https://docs.mongodb.org/manual/tutorial/install-mongodb-on-os-x/ 'Install MongoDB').

1. Install [Homebrew](http://brew.sh/ 'Homebrew'), if not already installed. Homebrew facilitates installation of programs.


2. Open a terminal window and execute these two commands:

    ```bash
    brew update
    brew install mongodb
    ```

    If you run into any issues with the brew install mongodb step, you can run
    `brew doctor` to verify that your Homebrew is working properly

3. To use Mongo, we need to set up the default data directory to which Mongo will write data. We also need to adjust the permissions of the data folder (the second two commands).

    ```bash
    sudo mkdir -p /data/db
    sudo chmod 0755 /data/db
    sudo chown -R `id -u` /data/db
    ```

4. Verify that you have the permissions set up correctly by running the following command:

    ```bash
    ls -ld /data/db
    ```

    You should get a result that looks something like this:

    ```
    drwxr-xr-x  17 username  wheel  578 May 17 11:11 /data/db
    ```

    In particular, verify that the first part is the same `drwxr-xr-x` (this specifies the permissions of the file, explained [here](https://www.linux.com/learn/understanding-linux-file-permissions) if you later want to read more).

5. To check that it's installed correctly, open a terminal window and run `mongod`.

    Open another terminal window and run `mongo`. This should look like this:

    ```
    $ mongo
    MongoDB shell version: 3.2.6
    connecting to: test
    >
    ```

##### Debugging:

* If you get the following error, your computer can't find mongo.

    ```
    -bash: mongod: command not found
    ```

    Open the file `~/.bash_profile` and add the line `export PATH=$PATH:/usr/local/bin/`. Reopen the terminal and try step 5 again.

* If you get the following error, you tried running `mongo` before running `mongod`.

    ```
    $ mongo
    MongoDB shell version: 3.2.6
    connecting to: test
    2016-08-17T17:59:12.202-0700 W NETWORK  [thread1] Failed to connect to 127.0.0.1:27017, reason: errno:61 Connection refused
    2016-08-17T17:59:12.203-0700 E QUERY    [thread1] Error: couldn't connect to server 127.0.0.1:27017, connection attempt failed :
    connect@src/mongo/shell/mongo.js:229:14
    @(connect):1:6

    exception: connect failed
    ```

    Make sure that `mongod` is *still running* before running `mongo`.

### Installing PyMongo

We will also want to interact with Mongo through Python. We need to install PyMongo, which is available in the Conda package manager.

1. In a terminal window, type

    ```bash
    conda install pymongo
    ```

2. To verify proper installation and to see what version of PyMongo you are running, we'll run python and then check if we can import pymongo.

    Run `ipython` to start a python terminal and then run `import pymongo`. Here's what you should get:

    ```
    $ ipython
    Python 2.7.10 |Anaconda 2.1.0 (x86_64)| (default, Oct 19 2015, 18:31:17)
    Type "copyright", "credits" or "license" for more information.

    IPython 3.1.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: import pymongo
    ```

    If you get the error `ImportError: No module named pymongo`, you did not successfully install `pymongo`.
