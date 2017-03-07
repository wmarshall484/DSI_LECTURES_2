---
title: AWS + High-Performance Python
date: \today
author: Erich Wellinger
theme: metropolis
header-includes:
    - \usepackage{graphicx}
    - \usepackage{minted}
    - \renewcommand\listingscaption{Source Code}
    - \newminted{python}{linenos, frame=lines, framesep=8pt, fontsize=\scriptsize, bgcolor=shadecolor}
    - \usepackage{hyperref}
    - \usepackage{color}
    - \definecolor{darkblue}{rgb}{0.0,0.0,0.5}
    - \definecolor{shadecolor}{rgb}{0.9,0.9,0.9}
    - \hypersetup{colorlinks=true, linkcolor=darkblue, urlcolor=darkblue}
---

## Morning Goals

* Overview of Cloud Computing
* Amazon Web Services (AWS)
    * Identity & Access Management (IAM) **NEED TO ADD**
    * Elastic Compute Cloud (EC2)
    * SSH Config **NEED TO ADD**
    * Simple Storage Service (S3)
* EC2/S3 Overview and Work Flow


## Overview

* Cloud computing allows us to run programs remotely on distant computers (In the cloud!, a.k.a. a massive server farm located somewhere on land)
* In this scenario, our computer would be the "client" sending jobs to the "server" (e.g. a AWS EC2 instance)
* Advantages
    * Accessibility from anywhere
    * Dynamic Scaling
    * Storage
    * Maintenance


## Overview

### Disadvantages

* Security
    * A third party owns the server
* Cost
    * In the long term, cloud service and cost a lot


## Why Amazon?

* Flexibility of many instance types
* A lot of traction over the years
* Libraries and tools built around AWS
* Behemoth in the cloud computing sector
    * Amazon Web Services owns ~30% of the could computing market


## Identity & Access Management

AWS Identity and Access Management (IAM) allows you to configure what permissions users have in your account.  But why does IAM matter if you are the only one using your account?

This matters because anyone that has access to your root account (e.g. through AWS Access Keys) also has access to your billing information which includes CC info.  Thus we should set up a Admin user account that sandboxed from accessing billing information.


## IAM (Continued)

1. First we need to access IAM after logging into our account

\begin{center} \includegraphics[width=275px]{imgs/IAM-1.png} \end{center}


## IAM (Continued)

2. Next you should customize your sign-in link.  This is the link you will use to sign into the AWS console---bookmark it!

\begin{center} \includegraphics[width=275px]{imgs/IAM-2.png} \end{center}


## IAM (Continued)

3. Now it's time to create a new user!  Click on `Users` under `IAM Resources`

\begin{center} \includegraphics[width=275px]{imgs/IAM-3.png} \end{center}


## IAM (Continued)

4. Create a user name and select `Programmatic access` and `AWS Management Console access`---create a password for this user

\begin{center} \includegraphics[width=275px]{imgs/IAM-4.png} \end{center}


## IAM (Continued)

5. Click on `Attach existing policies directly` and attach the `AdministratorAccess` policy type

\begin{center} \includegraphics[width=275px]{imgs/IAM-5.png} \end{center}


## IAM (Continued)

6. You should now see a success message and an opportunity to download the associated Access Keys

\begin{center} \includegraphics[width=275px]{imgs/IAM-6.png} \end{center}


## Elastic Compute Cloud (EC2)

* Virtual Machine in the cloud
* Can choose what Machine to launch
    * `Ubuntu` (Linux)
    * `RedHat` (Linux)
    * Many, many, others
* Use local Terminal as the client to access remote machine


## Step 1: Machine Image

This is where we will choose what type of image we will start up.  You can either choose one of the default AMIs (Amazon Machine Image), which starts up a fresh copy of your desired OS similar to booting up a new computer, or we can choose from a plethora of community AMIs.

For our purposes we will be using the `DSI-Template` AMI located in the N. Virginia region.

**NOTE**: AMIs are region specific, so if you can't find an AMI you are looking for you might be in the wrong region!


## Step 2: Specifications

This is where we will choose what kind of resources our machine will have including the number of CPUs, GPUs, and Memory.  Each instance will have a varying hourly cost associated with it that fluctuates with current demand.

As a rough guideline, a `m3.xlarge` instance which has 4 CPUs and 15GB of memory costs approximately $0.25 - $0.30 per hour.


## Step 3: Configuration

* Spot instances are available to reduce price starting from `m3.medium`
* Bid the machine with the price you set (as max)
* Takes longer to start
* Cannot stop and restart instance
* Much cheaper in general
* Otherwise expensive to use larger instances


## Step 4: Storage

* By default we will have a root EBS volume (more on this later) for storing OS and other files
* We can choose to up this or add on other hard drives


## Step 5: Tagging

* First Key is by default "Name"
* This controls the name that shows up in the Instances section of your EC2 dashboard.
* All this does is help you keep track of which machine is which


## Step 6: Security Group

* Here we will configure the security settings of our instance
* For example we could configure our instance to only accept `ssh` connections from our home or work IP Addresses
* It's also possible for our instance to run a Jupyter server that we can access remotely, but there are some important settings that need to be configured for this to work (ask me if you're interested in doing this)


## Create `pem` file

In order to access our machine through `ssh` we need to have a `pem` file which is essentially a cryptographic key.

**CAUTION**: Make sure you have the `.pem` file locally, otherwise create a new key pair


## Change `pem` permissions {.fragile}

* Once we have downloaded the `pem` file we need to make sure that it has the proper permission settings
* Run this line in the terminal:

\begin{minted}[frame=lines, framesep=8pt, bgcolor=shadecolor]{bash}
chmod 400 my-key-pair.pem
\end{minted}

* Once we do this, you should move it into your `~/.ssh` folder for ease of access


## Logging into EC2 {.fragile}

\begin{minted}[frame=lines, framesep=8pt, bgcolor=shadecolor]{bash}
ssh -i keypair.pem User@Domain
\end{minted}

* User: ubuntu (if you chose a different OS this might be different!)
* Domain: IP Address associated with your instance


## Copying files to EC2 {.fragile}

\begin{minted}[frame=lines, framesep=8pt, fontsize=\scriptsize, bgcolor=shadecolor]{bash}
scp -i keypair.pem  File.txt  User@Domain:/path/where/file/should/go
scp -i keypair.pem -r Folder User@Domain:/path/to/folder
\end{minted}


## Running Scripts and `tmux`
When running scripts on a AWS EC2 instance (or any remote client for that matter), we should be using `tmux`.  But what is `tmux`?

* `tmux` is a terminal multiplexer which allows us to muliplex several virtual consoles
* This enables us to create terminal "sessions" that we can then detach from without stopping any running processes
* This works because a `tmux` session's clients aren't bound to a specific physical or virtual console


## `tmux` Session Management

`tmux` sessions are useful for completely separating work environments.

* `tmux new -s session_name`
    * Creates a new `tmux` session named `session_name`
* `tmux attach -t session_name`
    * Attaches to an existing `tmux` session named `session_name`
* `tmux list-sessions` or `tmux ls`
    * Lists all existing `tmux` sessions
* `tmux detach` or prefix + `d`
    * Detaches from the currently attached session
* `tmux kill-session -t session_name`
    * Kills session `session_name`


## `tmux` Window Management

When inside a particular session, we can open up new tabs, called "Windows"

* `tmux new-window` or prefix + `c`
    * Create a new window
* prefix + `w`
    * List Windows
* prefix + `n`
    * Next Window
* prefix + `p`
    * Previous Window


## Useful `tmux` commands

By default we can access shortcuts using the `ctrl-b` prefix plus the given shortcut.  Below is a short list of useful commands...

* `?` - Lists available commands
* `:` - Brings up prompt
* `d` - Detach
* `c` - Creates a new window
* `w` - Lists windows
* `[` - Enter Copy Mode
* `&` - Kill window
* `x` - Kill pane


This is far from a comprehensive guide to using `tmux`.  For more information see [http://bit.ly/2dZzTI3](http://bit.ly/2dZzTI3).


## Stopping Instances

* Make sure to Stop/Terminate your instance if you are not running tasks
* Stop Vs. Terminate
    * Stopping simply shuts the computer down (e.g. you turn off your laptop/desktop).  Everything will still be there when you restart the instance
    * Terminating your instance deletes it (e.g. you throw your laptop/desktop in the trash)
* NOTE: If you start and then stop an instance immediately, you will still be charged for a full hour!

## SSH Configuration

* Setting up an SSH configuration streamlines the process of accessing our instance (or any remote host) by aliasing all the details for a particular host into a name of our choosing
* The configuration file is located at `~/.ssh/config` (create that folder and file if it doesn't exist already)

## SSH Configuration Example

The following is an example of an entry in our configuration file.  This is specifying a Host located at `54.174.93.43`, the user `ubuntu`, communication over port 22, and points to an identity file located at `~/.ssh/ewellinger-aws.pem`.  Using this configuration we could access our instance by simply typing `ssh MyNewInstance`

\begin{minted}[frame=lines, framesep=8pt, bgcolor=shadecolor]{text}
Host MyNewInstance
    Hostname 54.174.93.43
    User ubuntu
    Port 22
    IdentityFile ~/.ssh/ewellinger-aws.pem
\end{minted}


## AWS Elastic IP Address

There's just one problem...  When we shut down our instance, the next time we start it back up we don't know what IP Address it will be assigned.  Thus the details we outlined in our config file will no longer be correct.  

While we could go in and change our config file every time, it's not exactly the most elegant solution.  For that we turn to Elastic IP Addresses!

Elastic IP Addresses allow us to reserve a particular IP Address for our instance so that, when we start it back up, it will always be associated with the same address!

## AWS Elastic IP Address Setup

1. Locate the `Elastic IPs` button under the `NETWORK & SECURITY` drop down on the left hand side of the EC2 Management Console

\begin{center} \includegraphics[width=275px]{imgs/elastic-ip-1.png} \end{center}


## AWS Elastic IP Address Setup

2. Click on `Allocate New Address` to reserve a new IP Address

\begin{center} \includegraphics[width=275px]{imgs/elastic-ip-2.png} \end{center}


## AWS Elastic IP Address Setup

3. Click on `Yes, Allocate` and you should see a success message telling you what this new address is

\begin{center} \includegraphics[width=275px]{imgs/elastic-ip-3.png} \end{center}


## AWS Elastic IP Address Setup

4. Next we need to associate this address with our instance by right clicking on the address and clicking `Associate Address`

\begin{center} \includegraphics[width=275px]{imgs/elastic-ip-4.png} \end{center}


## AWS Elastic IP Address Setup

5. In the `Instance` field we can start typing in the name we gave our instance earlier and we should see it pop up as the only one that is running

\begin{center} \includegraphics[width=275px]{imgs/elastic-ip-5.png} \end{center}


## AWS Elastic IP Address Setup

6. Click `Associate`

7. Now when we look back at our instance details we can see that the Public IP address has changed to our Elastic IP Address!

\begin{center} \includegraphics[width=275px]{imgs/elastic-ip-6.png} \end{center}



## Simple Storage Service (S3)

* Storage space for big data
* S3 Storage --> Permanent and big data
* EBS (Elastic Block) Storage --> Temporary and small data


## S3 Operations

* Upload
* Download
* Read
* Write


## S3 Cost

* Extremely cheap
* First 1 TB per month is approximately $0.03 per GB


## Buckets

* An S3 Bucket is where your data will live
* Can contain folders and files
* Permissions can be configured to dictate access


## Create Bucket

* Bucket name must be unique (i.e. no one has ever used it before)
* Must be all lower case
* Must not have underscores


## Bucket Permissions

* We can add a permission dictating that everyone can read the contents of your bucket
* **WARNING**: Don't give everyone the ability to write or modify your bucket


## Bucket Permissions {.fragile}

* Below is an example bucket policy

\begin{minted}[frame=lines, framesep=8pt, fontsize=\scriptsize, bgcolor=shadecolor]{json}
{
"Version": "2008-10-17",
"Statement": [
  {
     "Sid": "AllowPublicRead",
     "Effect": "Allow",
     "Principal": {
        "AWS": "*"
     },
     "Action": "s3:GetObject",
     "Resource": "arn:aws:s3:::<your bucket name>/*"
     }
]
}
\end{minted}


## Uploading Data

* We can do this through AWS's GUI
* This kind of sucks though, Python for the win!


## Pandas S3 {.fragile}

Pandas has an easy API to read from S3

\begin{pythoncode}
import pandas as pd
df = pd.read_csv('https://s3.amazonaws.com/bucket/samplefile.csv')
\end{pythoncode}

We can also specify a chunk size if the data is very large...

\begin{pythoncode}
data_chunks = pd.read_csv(url, chunksize=100)
df_chunk = data_chunks.get_chunk()
\end{pythoncode}


## Writing, Deleting, and Managing buckets {.fragile}

* Pandas is great but doesn't allow us to do these other import tasks
* For this we will use `Boto`, a package for interacting with AWS in Python

\begin{pythoncode}
import boto

# Connect to S3
conn = boto.connect_s3(access_key, access_secret_key)

# List all the buckets
all_buckets = [b.name for b in conn.get_all_buckets()]
print all_buckets
\end{pythoncode}


## Create a new bucket {.fragile}

\begin{pythoncode}
bucket_name = 'testbucket'

if conn.lookup(bucket_name) is None:
    b = conn.create_bucket(bucket_name, policy='public-read')
else:
    b = conn.get_bucket(bucket_name)
\end{pythoncode}


## Read / Write Files {.fragile}

\begin{pythoncode}
# Write new file
file_object = b.new_key('sample.txt')
file_object.set_contents_from_string("Stuff 'N' Things",
                                    policy='public-read')

# Read from file
print file_object.get_contents_as_string()
\end{pythoncode}


## List / Delete Files {.fragile}

\begin{pythoncode}
# Print all the files in the bucket
filenames = [f.name for f in b.list()]
print filenames

# Delete a file
a = b.new_key('somefilename')
a.delete()
\end{pythoncode}


## Delete Bucket {.fragile}

\begin{pythoncode}
# Delete Bucket
# Must delete all files in bucket before deleting bucket
conn.delete_bucket('galvanizebucket')
\end{pythoncode}


## Usefulness of Boto

* Can read/write anything to S3 from anywhere
* Either from EC2 or locally
* Almost unlimited storage


## EC2 / S3 Usage

* When data is too big to fit locally
* Scripts that take a long time to run
* Have to run continuously (Hosting Web Apps)


## Work Flow

1. Upload/Access data on S3
2. Use `pandas`/`boto` to pull a subset down to local
3. Develop script locally
4. Upload script to EC2
5. Run script on EC2 on full set
6. Write results to S3


## Afternoon Goals

* Motivation
* Intro to Computing Resources
* Multi-core Processing
    * Parallelism
* Threading
    * Concurrency


## Motivation

Let's say we want to count the words in a set of documents.  To do this in a normal Python script we might set a `count` variable to 0, read in each file in turn, and loop through each line counting the words and adding that value to our `count` variable.

While this works fine for a reasonably sized number of documents, what if we wanted to do this for thousands or even millions of documents?  Clearly this approach would be suboptimal.


## Motivation

Instead we could count the words of each document in parallel.  This works by calling our counting function (e.g. `count_words(file)`) for each file in parallel where the result is the word count for that particular file.

To then get our total word count we would simply add all these values up!


## Motivation

* Process biggish data ($\ge 5$GB depending on the task)
* Saves time which allows for more coffee breaks
* More efficient use of CPU resources


## Types of Computing Resources

* **Central Processing Unit (CPU)**
    * Unit: GHz (instructions/second)
* **Random Access Memory (RAM/Memory)**
    * Unit: GB (Gigabytes)


## CPU Cores

* A CPU can hold multiple cores
* Each core is a self-contained processor that can execute programs
* Internal (OS) Programs are almost always configured to take advantage of these multiple cores by distributing the job to each of your cores.
* External Programs (e.g. a Python script you've written) will generally only use a single core unless specified otherwise


## What happens when a program runs?

* When we tell our program to run it translates our Python code into instructions for the CPU by breaking it up into **processes**.  A process consists of:
    * Process ID (PID)
    * Program Code
    * CPU Scheduling
    * Memory
* We can take a look at these things by looking at the Activity Monitor on a Mac or running `top` or `htop` (if you have it installed)


# Multicore Processing

## Parallelism

Now that we understand the CPU, Memory, and Processes fit together, how do we go about writing code that will leverage the multiple cores our computer has?

For this we will use the built-in `multiprocessing` package for specifying how the processes should be split up.


## `multiprocessing` Sample Code {.fragile}

\begin{pythoncode}
from multiprocessing import Pool, cpu_count
import os

# Count the number of words in a file
def word_count(f):
    with open(f):
        count = sum(len(l.split()) for l in f)
    return count

def sequential_word_count(lst_of_files):
    return sum(word_count(f) for f in lst_of_files)
\end{pythoncode}


## `multiprocessing` Sample Code {.fragile}

\begin{minted}[linenos, frame=lines, framesep=8pt, fontsize=\scriptsize, bgcolor=shadecolor, firstnumber=last]{python}

# Use multiple cores to count words in files
def parallel_word_count(lst_of_files):
    # Set to use all available cores
    pool = Pool(processes=cpu_count())
    results = pool.map(word_count, lst_of_files)
    return sum(results)
\end{minted}


## Concurrency and Threading

* A *Thread* is the smallest sequence of programmed instructions that can be managed by a scheduler
* Generally speaking a thread is component of a process which means...
    * Multiple threads can exist within a single process
    * They will execute *concurrently*
    * They will share resources such as memory (in contrast, separate processes do not share resources)
* When being run on a single processor, threads are implemented using *time slicing*
    * The CPU switches between different *software threads*
    * Happens quickly enough that users perceive the threads or tasks as running in parallel
* Threads within *the same process* are **not** parallel, instead the CPU will rapidly switch between multiple tasks


## Sharing between Threads

* All threads in the process share:
    * Memory allocated to the process
    * Code of the process
    * Context (i.e. variables)


# Parallelism vs. Concurrency Analogy

## Parallelism Use Case

* Problems that are CPU-intensive
* Tasks that use heavy computations with no wait time in between lend themselves well to running in parallel


## Concurrency Use Case

* I/O bound problems
    * Read/Writing of files
    * Making Web Requests
* When reading, writing, and making web requests, we can thread these processes so as soon as there is downtime we switch to a new thread


## `threading` Sample Code {.fragile}

\begin{pythoncode}
import threading

threads = []

# Configure target_function to save result
def thread_target_function(arg1, arg2):
    self = threading.current_thread()
    self.result = target_function(arg1, arg2)
\end{pythoncode}


## `threading` Sample Code {.fragile}

\begin{pythoncode}
# Initiate Threads
for i in range(num_threads):
    t = threading.Thread(target=thread_target_function,
                         args=(arg1, arg2))
    threads.append(t)

# Start Threads
for thread in threads: thread.start()
# join to make sure each thread is finished
for thread in threads: thread.join()
# Access the result, if any
results = [t.result for t in threads]
\end{pythoncode}


## Summary

* Parallelism on multiple cores
* Threading within a core
* `multiprocessing` for parallelism
* `threading` for concurrency
* Parallelism --> CPU-bound problems
* Concurrency --> I/O-bound problems
