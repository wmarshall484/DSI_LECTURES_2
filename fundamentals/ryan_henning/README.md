# Unix Fundamentals

By the end of this lecture you'll be able to:
1. Make "survival" edits in `vim`.
1. Interpret Unix file permissions from the `ls -l` command.
1. Understand the special files `stdin`, `stdout`, and `stderr`.
1. Use Unix _file redirection_ and _pipes_ to enhance the power of each simple Unix command.
1. Understand and modify the special `PATH` environment variable.
1. Understand and modify the special `PS1` environment variable.
1. Set `bash` configuration through the `.bashrc` file.
1. Create aliases and store them in the `.bashrc` file.
1. Build an executable python script which is easy-to-use and reusable.
1. Start a collection of reusable, Unix-style scripts.

## `vim` survival skills

From [Vim's Website](http://www.vim.org/about.php):
> Vim is often called a "programmer's editor," and so useful for programming that many consider it an entire IDE. ... Vim isn't an editor designed to hold its users' hands. It is a tool, the use of which must be learned.

`vim` is the "`vi` i**M**proved" editor. `vi` is an old-school Unix text-editor program.

In `vim` you are either in:
- _insert mode_, or
- _command mode_

In _insert mode_, you get to type into the document.

In _command mode_, you get to move the cursor around and instruct vim to do high-level commands.

By default, you start in _command mode_. This leads to confusion for all new users who want to immediately begin editing the file. There are many ways to enter _insert mode_ from _command mode_, the most simple way is to press `i` on the keyboard ('i' for insert).

Now that you are in _insert mode_, you can type into the document. When you are ready, return to _command mode_ by pressing _escape_ on the keyboard.

Now that you are in _command mode_, let's learn a command. Enter `:w` then press enter. You just saved the file. Now enter `:q` and press enter. You just exited vim. (Btw, you can save _and_ exit with the command `:wq`.)

If you ever get totally lost in `vim`, just hit _escape_ a bunch then type `:q!`, which tells vim to exit _without_ saving the file.

You can now survive `vim` when necessary. If you want to dive deeper, see [Vim Adventures](https://vim-adventures.com/) and also [Ryan's Vim Config](https://github.com/acu192/config-vim)

## Unix File System and Unix File Permissions

Everything is a file in Unix. Yes, EVERYTHING! Even devices (like your webcam and your speakers) are represented as files.

Also, there is only one file tree in Unix. The root of the file tree is `/`. File paths (which are just strings) represent where files reside. A file path which begins with a `/` is called an "absolute" path since it is specified from the root of the file tree. Paths which do not begin with `/` are relative file paths, meaning they represent the path to the file from the current directory.

Every file has a set of permissions associated with it. The easiest way to see the permissions on a file is to run the command `ls -l` in whatever directory you care about. You'll see something like this:
```
-rwxr-x---   1 ryan  staff         319 Jan 17 15:37 do_work.bash
```

See that part that says `-rwxr-x---`? That's the cryptic way Unix describes the file permissions. The first `rwx` means that the "user" has _read_, _write_, and _execute_ permissions on the file. The second section which says `r-x` means that the "group" only has _read_ and _execute_ permissions. The final `---` means "others" have no permissions.

On a normal file, _read_ permissions are self-explanatory, it means the user in question may read the file's contents. _write_ permissions means the user can write (or overwrite) the file's contents. _execute_ is more complicated--it means the user is allowed to run the file like a program! (We'll come back to this topic when we write a bash script.)

## stdin, stdout, stderr

Every process on Unix gets a special input "file" named _stdin_, a special output "file" name _stdout_, and another special output "file" named _stderr_. I put "file" in quotes because everything in Unix is a file, but these are necessarily normal files. For example, all three of these (stdin, stdout, and stderr) are _usually_ connected to your terminal screen!

Let's do an example in Python:
```python
import sys

while True:
    line = sys.stdin.readline()
    if not line: break
    line = line[0:-1]   # stip new line character
    revsd = line[::-1]  # reverse the string
    sys.stdout.write(revsd + '\n')
```

Name the script `reverse.py`.

Notice we don't have to open stdin or stdout, we just import them and use them. Btw, `raw_input` and `print` use stdin and stdout, respectively.

## File Redirection and Pipes

Let's use that python script we just wrote above to reverse every line of a large file and save the result to a new (equally-large) file. How can we do that?

One idea, we can modify the python script to read the large file. And also modify the script to write to a file. Or... maybe there's a way to **NOT** modify our script!

Enter this on the command line:
```bash
$ python reverse.py < some_large_file
```

That's cool.

Now run this:
```bash
$ python reverse.py < some_large_file > some_new_file
```

This is file redirection. We're telling `bash` in the first example to redirect the "some_large_file" file into the process _as_ stdin. So our script reads from stdin just like normal, but it will actually be reading from our file!

In the next command we use _more_ file redirection. This time we're redirecting the output (i.e. redirecting what is written to stdout) into a new file.

Often you want to redirect the output (stdout) of one command into the input (stdin) of anther command. We could use a temporary file for this, or (better option) we can use "pipes".

Run the following command to see pipes in action:
```bash
$ cat data/2015_sp100.csv | grep GOOG | sort | python data/plot_stock_prices.py
```

## The PATH variable

When you type a command into your shell, it must first _find_ the program you're trying to run. E.g. when you type `python my_script.py` into your shell, the shell must find the `python` program before it can run it. Where does it look?

Does it look _everywhere_? No... that would be bad for many reasons.

Does it look only in your current directory? No... actually by default it _doesn't_ look there even.

Well, someone at some point decided it would look at all the paths in the `PATH` environment variable. Run the command `echo $PATH` to see which directories are in your system's `PATH` variable.

Run the command `which python` to see which directory the system find which contains the python command. The `which` command also looks through the PATH variable to find commands, which is handly for diagnosing some things when they go wrong.

## The PS1 variable

Another special variable which `bash` looks at is the `PS1` variable. It tells `bash` what to print as your prompt!

Run this in your bash shell `PS1="talk to me > "`

See what happend?

If you want a cool prompt (with colors and handy info), check out [Ryan's bash config repo](https://github.com/acu192/config-bash).

## The `.bashrc` file (and friends)

When `bash` starts (e.g. when you open a new terminal window), it loads a few config files before showing the first prompt. This is your chance to configure bash the way you like it. You can do stuff like add directories to the PATH (like `psql`) and set the PS1 variable to something sensible.

Let's use `vim` to edit your `.bashrc` file. Type `vim ~/.bashrc`

You can also take a look at `.profile` and `.bash_profile`. Google for the difference between these three files.

Btw, whenever you modifiy any of those three files, **be sure to restart your shell!** (e.g. close your terminal window and open a new one)

Btw #2, we'll be editing these files periodically throughout the rest of the DSI (and your life as a data scientists / software engineer), so be sure to get familiar with it now.

Again, if you want a coolish bash config, check out [Ryan's bash config repo](https://github.com/acu192/config-bash).

## Aliases

Typing sucks, so let's not do that so much. Aliases are one way to type less!

Add the following alias to your `.bashrc` file:
```
alias lla='ls -alhF'
```

Close and reopen your terminal and try out the alias by typing `lla` and hitting enter.

## Scripts

(Hopefully everything will come together in this section.)

Did you know `bash` has if-statements and for-loops? Yep, it really does. They're very ugly though. Python is way prettier. So, we'll forgo the usual example of a bash script and just write an _executable_ Python script instead.

Remember that reversing python script from several sections back? Let's make that an executable script.

First, modify it to look like this. (Notice the _one_ new line at the top of the file. Check [this](http://stackoverflow.com/questions/5709616/whats-the-difference-between-these-two-python-shebangs) if you want to know what that line means.)
```python
#!/usr/bin/env python

import sys

while True:
    line = sys.stdin.readline()
    if not line: break
    line = line[0:-1]   # stip new line character
    revsd = line[::-1]  # reverse the string
    sys.stdout.write(revsd + '\n')
```

Now, let's check the permissions of the file:
```bash
$ ls -l reverse.py
```

You see something like:
```
-rw-r--r--  1 ryan  staff  220 Mar 30 23:10 reverse.py
```

We need to make Unix consider `reverse.py` executable, which it currently doesn't consider it. Run `chmod +x reverse.py`. The permissions should now look like:
```
-rwxr-xr-x  1 ryan  staff  220 Mar 30 23:10 reverse.py*
```

The `x` in the permissions means it's now executable. That means we can run it like this on the command line:
```bash
$ ./reverse.py
```

(Notice we don't have to run it like we used to with `python` written out. Yay, less typing again.)

It gets better. We don't even need the `.py` anymore. (Unix doesn't look at file extensions.)

```bash
$ mv reverse.py reverse
$ ./reverse
```

Yay, less typing again.

It gets better still. You might be wondering why I have to type the `./` in front of the name of my script when I run it. That's because the current directory is (probably) not in your `PATH` variable. Instead of fixing that problem, let's just move our script somewhere it makes sense to be. Let's create a `bin` directory and put our script there. (Then in the future we can add all our cool re-usable scripts there as well.)

```bash
$ mkdir bin
$ mv reverse bin/
$ cd bin/
$ pwd
```

I print the absolute path to the new bin directory above because we next need to add it to our `PATH` variable.

Back to the `.bashrc`, run `vim ~/.bashrc` and add the following line:
```
export PATH=$PATH:<path_to_your_bin>
```

Save, close your terminal, reopen a new terminal, and try your reverse script from any directory! (It should work!)

```bash
$ cd somewhere_arbitrary
$ reverse whatever_file_of_interest
```

Notice we don't need the `./` anymore. Our reverse script is a full citizen on our system (at least for our own user account) now!

Btw, here's [Ryan's bin repo](https://github.com/acu192/config-bin).

## Know Your Unix!

Be familiar and adhere to the [Unix Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy). Then you will prosper.

## Next helper script to build: a dataset down-sampling script.

Often when you first receive a (large) dataset, it's best to down-sample it so that you can work with it **quickly** to do EDA and preliminary modeling. Once you have a strong feel for the smaller (down-sampled) dataset, then you can begin using the full (large) dataset.

Similar to how we made the "reverse" script, make another reusable, Unix-style script which down-samples a dataset using the [Reservoir Sampling algorithm](https://en.wikipedia.org/wiki/Reservoir_sampling).

