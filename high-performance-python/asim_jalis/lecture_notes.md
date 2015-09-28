
    %%javascript
    $.getScript('http://asimjalis.github.io/ipyn-ext/js/ipyn-present.js')

<!-- 
The ipynb was auto-generated from markdown using notedown.
Instead of modifying the ipynb file modify the markdown source. 
-->

<h1 class="tocheading">AWS Services</h1>
<div id="toc"></div>

AWS Services
============

AWS Storage + Execution
-----------------------

What are the primary services that Amazon AWS offers?


Name   |Full Name                  |Service
----   |---------                  |-------
EC2    |Elastic Compute Cloud      |Execution
S3     |Simple Storage Service     |Storage
EBS    |Elastic Block Store        |Storage attached to EC2 instances

Pop Quiz
--------

<details><summary>
Q: I want to store some video files on the web. Which Amazon service
should I use?
</summary>
S3
</details>

<details><summary>
Q: I just created an iPhone app which needs to store user profiles on the
web somewhere. Which Amazon service should I use?
</summary>
S3
</details>

<details><summary>
Q: I want to create a web application in PHP. Which Amazon service
should I use?
</summary>
EC2 + EBS or EC2 + S3
</details>



S3 vs EBS
---------

What is the difference between S3 and EBS? Why would I use one versus
the other?


Feature                |S3                   |EBS
-------                |--                   |---
Can be accessed from   |Anywhere on the web  |Particular availability zone
Can be accessed from   |Any EC2 instance     |EC2 instance attached to it
Pricing                |Storage              |Storage + IOPS
Price                  |Cheaper              |More Expensive
Latency                |Higher               |Lower
Throughput             |Varies More          |Varies Less
Performance            |Slightly Worse       |Slightly Better
Max volume size        |Unlimited            |16 TB
Max file size          |5 TB                 |16 TB

Pop Quiz
--------

<details><summary>
Q: What is latency?
</summary>
Latency is the time it takes between making a request and the start of a response.
</details>


<details><summary>
Q: Which is better? Higher latency or lower?
</summary>
Lower is better.
</details>

<details><summary>
Q: Why is S3 latency higher than EBS?
</summary>
One reason is that EBS is in the same availability zone.
</details>


Amazon vs Other Cloud Services
------------------------------

Why do so many companies use Amazon's Web Services for their backend?

- Steve Yegge provides one of the big reasons for AWS's popularity.


Steve Yegge and Decoupled Design
--------------------------------

<img src="img/yegge.jpg">

Who is Steve Yegge?

- Steve Yegge is a developer from Amazon and Google.

- Steve blogged a long [rant][yegge-rant] about Amazon's APIs vs
  Google's APIs.

[yegge-rant]: https://plus.google.com/+RipRowan/posts/eVeouesvaVX

What is the difference between Amazon and Google's APIs?

- At Amazon developers have to use Amazon's public APIs to for their
  internal dependencies.

- At Google developers can use private APIs for dependencies.

- The forced dogfooding makes Amazon's APIs more decoupled.

---

Amazon S3
=========

Buckets and Files
-----------------

What is a bucket?

- A bucket is a container for files.

- Think of a bucket as a logical grouping of files like a sub-domain.

- A bucket can contain an arbitrary number of files.

How large can a file in a bucket be?

- A file in a bucket can be 5 TB.


Bucket Names
------------

What are best practices on naming buckets?

- Bucket names should be DNS-compliant.

- They must be at least 3 and no more than 63 characters long.

- They must be a series of one or more labels, separated by a single
  period. 
  
- Bucket names can contain lowercase letters, numbers, and hyphens. 

- Each label must start and end with a lowercase letter or a number.

- Bucket names must not be formatted as an IP address (e.g., 192.168.5.4).

What are some examples of valid bucket names?

- `myawsbucket`

- `my.aws.bucket`

- `myawsbucket.1`

What are some examples of invalid bucket names? 

- `.myawsbucket`

- `myawsbucket.`

- `my..examplebucket`

Pop Quiz
--------

<details><summary>
Q: Why are these bucket names invalid?
</summary>
Bucket names cannot start or end with a period. And they cannot have a
multiple periods next to each other.
</details>


Creating Buckets
----------------

Q: How can I create a bucket?

- Get your access key and secret key from the `rootkey.csv` that you
  downloaded from Amazon AWS.
  
- Create a file called `~/.aws/credentials` (on Linux/Mac) or
  `%USERPROFILE%\.aws\credentials` (on Windows), and insert the
  following code into it. Replace `ACCESS_KEY` and `SECRET_KEY` with
  the S3 keys you got from Amazon.
  
```
[default]
aws_access_key_id = ACCESS_KEY
aws_secret_access_key = SECRET_KEY
```

- Create a connection to S3.

        import boto
        conn = boto.connect_s3()
        print conn

- List all the buckets.

        conn.get_all_buckets()

- Create new bucket.

        import os
        user = os.environ['USER']
        bucket_name = user + "1"
        bucket_name = bucket_name.lower()
        print bucket_name
        bucket = conn.create_bucket(bucket_name)
        print bucket

Upgrading Boto
--------------

Q: Boto is not able to find the credentials. How can I fix this?

- Older versions of Boto were not able to read the credentials file.

- You might run into this problem on the EC2 instance.

- Here is how to upgrade Boto to the latest version.

        sudo pip install --upgrade boto

Adding Files
------------

Q: How can I add a file to a bucket?

- List files.

        bucket.get_all_keys()

- Add file.

        file = bucket.new_key('file.txt')
        print file
        file.set_contents_from_string('hello world!!')

- List files again. New file should appear.

        bucket.get_all_keys()

Q: How can I get a file from a bucket?

- Get file.

        f = bucket.get_key('file.txt')
        print f.get_contents_as_string()


Creating Buckets With Periods
-----------------------------

Q: How can I create a bucket in Boto with a period in the name?

- There is a bug in Boto that causes `create_bucket` to fail if the
  bucket name has a period in it. 

- Try creating the bucket with a period in its name. This should fail.

        bucket_name_with_period = bucket_name + ".1.2.3"
        bucket_with_period = conn.create_bucket(bucket_name_with_period)
        print bucket_with_period

- To get around this run this code snippet.

        import ssl
        if hasattr(ssl, '_create_unverified_context'):
           ssl._create_default_https_context = ssl._create_unverified_context

- Now try creating the bucket with a period in its name and it should work.

        bucket_name_with_period = bucket_name + ".1.2.3"
        bucket_with_period = conn.create_bucket(bucket_name_with_period)
        print bucket_with_period

- Now lets delete the bucket.

        bucket_with_period.delete()

- For more details see <https://github.com/boto/boto/issues/2836>.


Access Control
--------------

Q: I want to access my S3 file from a web browser without giving my
access and secret keys. How can I open up access to the file to
anyone?

- You can set up Access Control Lists (ACLs) at the level of the
  bucket or at the level of the individual objects in the bucket
  (folders, files).

Q: What are the different ACL policies?

ACL Policy           |Meaning
----------           |-------
`private`            |No one else besides owner has any access rights.
`public-read`        |Everyone has read access.
`public-read-write`  |Everyone has read/write access.
`authenticated-read` |Registered Amazon S3 users have read access.

Q: What does `read` and `write` mean for buckets and files?

- Read access to a file lets you read the file.

- Read access to a bucket or folder lets you see the names of the
  files inside it.


Pop Quiz
--------

<details><summary>
Q: If a bucket is `private` and a file inside it is `public-read` can
I view it through a web browser?
</summary>
Yes. Access to the file is only determined by its ACL policy.
</details>


<details><summary>
Q: If a bucket is `public-read` and a file inside it is `private` can
I view the file through a web browser?
</summary>
No, you cannot. However, if you access the URL for the bucket you will see the file listed.
</details>

Applying Access Control
-----------------------

Q: How can I make a file available on the web so anyone can read it?

- Create a file with a specific ACL.

        file2 = bucket.new_key('file2.txt')
        file2.set_contents_from_string('hello world!!!',policy='private')

- Try reading the file.

        file2_url = 'http://s3.amazonaws.com/' + bucket_name + '/file2.txt'
        print file2_url
        !curl $file2_url

- Now change its ACL.

        file2.set_acl('public-read')
        !curl $file2_url

- Also you can try accessing the file through the browser.

- If you do not specify the ACL for a file when you set its contents,
  the file is `private` by default.


S3 Files to URLs
----------------

Q: How can I figure out the URL of my S3 file?

- As above, you can compose the URL using the region, bucket, and file name. 

- For N. Virginia the general template for the URL is `http://s3.amazonaws.com/BUCKET/FILE`.

- You can also find the URL by looking at the file on the AWS web console.


Deleting Buckets
----------------

Q: How can I delete a bucket?

- Try deleting a bucket containing files. What happens?

        print conn.get_all_buckets()
        bucket.delete()

- To delete the bucket first delete all the files in it.

        for key in bucket.get_all_keys(): 
            key.delete()

- Then delete the bucket.

        print conn.get_all_buckets()
        bucket.delete()
        print conn.get_all_buckets()

---

Amazon EC2
==========

Regions
-------

Q: What are *AWS Regions*?

- AWS is hosted in different geographic locations world-wide. 

- For example, there are 3 regions in the US.


Q: What are the regions in the US

Region       |Name       |Location 
------       |----       |-------- 
us-east-1    |US East    |N. Virginia
us-west-1    |US West    |N. California
us-west-2    |US West 2  |Oregon


Q: How should I choose a region?

- N. Virginia or `us-east-1` is the default region for EC2.

- Using a region other than N. Virginia requires additional configuration.

- If you are not sure choose N. Virginia.


Availability Zones
------------------

Q: What are *AWS Availability Zones*?

- Regions are divided into isolated availability zones for fault
  tolerance.

- Availability zone run on physically separate hardware and
  infrastructure.

- They do not share hardware, or generators, or cooling equipment. 

- Availability zones are assigned automatically to your EC2 instances
  based on your user ID.

<img src="img/aws_regions.png">



<details><summary>
Q: Is it possible for two separate users to coordinate and land on the
same availability zone?
</summary>
1. Availability zones are assigned automatically by the system.
<br>
2. It is not possible for two AWS users to coordinate and be hosted on the same
availability zone.
</details>

----

Connecting to EC2
-----------------

Q: How can I connect to an EC2 instance?

- Login to the AWS console.

- Navigate: EC2 > Launch Instance > Community AMIs > Search community AMIs > `ami-d1737bb8`

- View the instance and get its Public DNS.

- This should look something like `ec2-52-3-161-43.compute-1.amazonaws.com`.

- Use this command to connect to it.

- `ssh -X -i ~/.ssh/keypair.pem user@domain`

- Here is an example. 

- `ssh -X -i ~/.ssh/keypair.pem ubuntu@ec2-52-3-161-43.compute-1.amazonaws.com`

- Make sure you replace the Public DNS value below with the value you
  have for your instance.

Copying Files to EC2
--------------------

Q: How can I copy files to the EC2 instance?

- To copy a file `myfile.txt` to EC2, use a command like this.

- `scp -i ~/.ssh/keypair.pem myfile.txt user@domain:`

- To copy a directory `mydir` recursively to EC2, use a command like
  this. 
  
- `scp -i ~/.ssh/keypair.pem -r mydir user@domain:`

Pop Quiz
--------

<details><summary>
Q: When you copy a file to EC2 with `scp` will this show up in S3?
</summary>
No. The file will be stored on the disk on the EC2 instance. It will
not be in S3.
</details>


High-Performance Python
=======================

Multi-Processing vs Multi-Threading
-----------------------------------

Q: What is the difference between *multi-processing* and
*multi-threading*?

- Multi-threading (also known as concurrency) splits the work between
  different threads running on the same processor. 
  
- When one thread is blocked the processor works on the tasks for the
  next one.

- Multi-processing splits work across processes running on different
  processors or even different machines.

- Multi-threading works better if you need to exchange data between
  the threads. 

- Multi-processing works better if the different processes can work
  heads down without communicating very much.

Pop Quiz
--------

<details><summary>
Q: I have to process a very large dataset and run it through a
CPU-intensive algorithm. Should I use multi-processing or
multi-threading to speed it up?
</summary>
Multi-processing will produce a result faster. This is because it will
be able to split the work across different processors or machines.
</details>


<details><summary>
Q: I have a web scraping application that spends most of its time
waiting for web servers to respond. Should I use multi-processing or
multi-threading to speed it up?
</summary>
Multi-threading will produce a bigger payoff. This is because it will
ensure that the CPU is fully utilized and does not waste time blocked
on input.
</details>

Analogies
---------

Multi-Threading  |Multi-Processing
-----------      |----------------
Laundromat       |Everyone has a washer-dryer
Uber or Carpool  |Everyone has a car


Multi-Threading
---------------

Q: How can I write a multi-threaded program that prints `"hello"` in
different threads?

- Define print as a function.

        def print2(x): print x
        print2("hello")

- Create 2 threads that are going to print.

        import threading
        t1 = threading.Thread(target=lambda:print2('hello'))
        t2 = threading.Thread(target=lambda:print2('hello'))

- Start the threads.

        t1.start()
        t2.start()

- Wait for threads to finish.

        t1.join()
        t2.join()

Multi-Processing
----------------

Q: Calculate the word count of strings using multi-processing.

- Import `Pool`

        from multiprocessing import Pool

- Define how to count words in a string.

        def word_count(string):
            return len(string.split())

- Define counting words sequentially.

        def sequential_word_count(string_list):
            return sum([word_count(s) for s in string_list])

- Define counting words in parallel.

        def parallel_word_count(string_list):
            pool = Pool(processes=4)
            results = pool.map(word_count, string_list)
            return sum(results)

- Create `word_count` version that saves result in thread object.

        def thread_word_count(string):
            self = threading.current_thread()
            self.result = word_count(string)

- Define counting words using `Thread`.

        def concurrent_word_count(string_list):
            threads = []
            for string in string_list:
                thread = threading.Thread(
                    target=thread_word_count,
                    args=(string,))
                threads.append(thread)
            for thread in threads: thread.start()
            for thread in threads: thread.join()
            results = []
            for thread in threads: results.append(thread.result)
            return sum(results)

Q: Time all 3 versions.

- Create a sample input.

        string_list = [
            'hello world',
            'this is another line',
            'this is yet another line']

- Time each one

        %time print sequential_word_count(string_list)
        %time print concurrent_word_count(string_list)
        %time print parallel_word_count(string_list)

Pop Quiz
--------

<details><summary>
Q: Between sequential, parallel, and concurrent, which one is the
fastest? Which one is the slowest? Why?
</summary>
1. Sequential is the fastest. Concurrent is second. Parallel is the
slowest.
<br>
2. Concurrent and parallel have a higher setup overhead. This is not
recovered for small problems.
<br>
3. Use these only if your processing takes longer than the setup
overhead.
</details>

Cleaning Up Zombie Python Processes
-----------------------------------

Here is how to kill all the processes that `multiprocessing` will
bring up in the background.

```sh
ps ux | grep IPython.kernel | grep -v grep | awk '{print $2}' | xargs kill -9
```
