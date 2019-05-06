---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Note!
Despite being in an "ipython notebook", there won't be writing any python. But I will be showing how to use bash commands. To do so in a notebook, you must prepend the command with an exclamation point (!), also called a "bang".

```python
!pwd
```

```python
!ls
```

All the commands you see could simply be typed into your terminal, just omit the bangs. 


# Unix fundamentals

## Objectives
 * Perform basic file operations from the command line
 * Get help using `man`
 * Configure environment in *.bash_profile*
 * Manage a process with job control
 * Write a simple regular expression
 * Use `grep`/`sed`/`awk`/`cut`/`paste` to process/clean a text file
 * Perform “survival” edits using vi


# Agenda
* About operating systems and unix
* Using a shell
* Files and permissions
* Basic commands


# What is an Operating System?

Operating system: the collection of software that directs a computer's operations, controlling and scheduling the execution of other programs, and managing storage, input/output, and communication resources. (Dictionary.com)

Many pieces

 * Kernel (CPU, memory, processes, users)
 * Device drivers (keyboard, mouse, displays, ...)
 * File manager
 * System processes
 * User interface (shells and GUI)
 * Standard programs



# Windows and Unix

Windows (most desktops and laptops)

 * Made by Microsoft
 * Proprietary
 * More GUI based

Unix

 * Many versions, made by different companies, groups, or people (including Apple since 2002)
 * Originally a commercial product
 * Linux and FreeBSD are *open-source* versions of Unix
 * More command-line based
 * Small, simple commands
 * Everything is a file




# Shells

A shell is a command-line interface that interprets user input, runs programs, and output results.

 * sh (Bourne Shell)
 * ksh (Korn Shell)
 * **bash** (Bourne-again shell)
 * csh (C shell)
 * tcsh
 * zsh

All are also scripting languages.

A terminal is a *window displaying a shell prompt*. The shell is the *process running on a computer that takes commands as input*. You may hear people use "terminal" and "shell" interchangeably, but they are confused. 

The [original computing terminal](https://en.wikipedia.org/wiki/Computer_terminal) was a teletypewriter (TTY). Commands were typed and zapped over to the room-sized computer mainframe. [UNIX](https://en.wikipedia.org/wiki/History_of_Unix) was developed in this environment, so many commands retain the terminology of teletypewriters and tape drives. 


# Processes

A process is a program or task running on a computer.

A single process consists of:
 * One or more threads
 * Program text
 * Memory for stack and heap
 * File descriptors
 * Environment
 * Owner and privilege


To view running processes and their details, type `ps`

```python
!ps
```

By default, `ps` only shows processes started by you (that is, the userid associated with you, and not processes started by other users or the `root` user), and started in the same terminal that you just typed `ps` into. 

To show all processes started by all users in all terminals, typ `ps -waux`

```python
#!ps -waux
```

# File structure

Basic file commands

 * `pwd` (print working directory)
 * `ls` (list directory)
 * `cd` (change directory)

Directories contain files and other directories, with names separated by `/`

Special directories:

 * `/` root, the top-level directory
 * `~` your home directory
 * `.` the current directory
 * `..` the parent directory

Absolute paths start with `/` (or `~`). Relative paths don't.



# Command-line Options

Most commands have can take options.

Usually

 * single-character options are preceded by `-` and can be combined
 * full-word options are preceded by `--`
Usually.

Examples:

 * `python --version`
 * `ls -l`
 * `ls -la`

See `man ` *command* for more details.




# Basic Commands

### Help

 * `man` (read `man man` for more information)

### Files and directories

 * `cat` (output file(s) to STDOUT)
 * `less` (page through files)
 * `head` and `tail` (look at start and end of file)
 * `mv` (move file or directory)
 * `cp` (copy a file, use `cp -r` to copy a directory)
 * `rm` (remove file or directory; use `-rf` *carefully* to remove directory)
 * `mkdir` and `rmdir` (make and remove directory)
 * `touch` (create empty file, or update timestamp)
 * `diff` (compare files)

### Managing processes
 * `ps` (display running processes)
   * `ps waux` (display all processes from all users)
 * `kill` (terminate a process)
   * If you have a process running in your terminal, `<Ctrl>-C` should kill it. If that fails, you'll have to use `kill`.
 * `<bash command> &` (run process in background. [more info](https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html))
   * If you have a process running in your terminal, `<Ctrl>-Z` pauses the process and sends it into the background. It does NOT kill that process. 
 * `jobs` (show background processes running in the current shell session; each process has a _job number_. [more info](http://tldp.org/LDP/abs/html/x9644.html))
   * `bg <job number>` (resume a suspended job and run it in the background)
   * `fg <job number>` (send a background job into the foreground)


### Common Filters

These can be passed a file, or read from STDIN

 * `wc` (count lines/words/characters)
 * `grep` or `egrep` (find lines that contain strings)
 * `sort`
 * `uniq` (combine consecutive identical lines; use `-c` to count)
 * `tr` (translate characters)
 * `cut` (select specific columns of csv or tsv)
 * `paste` (like SQL join; not that common)
 * `sed`, `awk`, and `perl` (languages for file manipulation)



### Other Useful Commands

* `echo` (echo to STDOUT)
* `find` (find files that match something and maybe do something with them)
* `which <bash command>` (show the path to the executable file for that bash command)
* `tar` (archive directories into a single file)


<!-- #region {"hideCode": true} -->
### example: killing a process
<!-- #endregion -->

To kill a misbehaving (or frozen) process, type `kill <PID>` (where `<PID>` is the process id listed in `ps` above).

Sometimes you may have the use the `-9` option of the `kill` command, which you can think of as a "hard shutdown" of a process. `kill -9 <PID>`


Try the following in your terminal (not using the notebook). `$` represents the shell prompt, don't type `$`


```
$ sleep 100 &
$ jobs
$ ps
$ kill <the PID for sleep>
$
```


### example: reading a file, searching through a file

```python
!ls -alh
```

```python
!cat poem.txt
```

```python
!head poem.txt
```

```python
!head -n 4 poem.txt
```

```python
!grep donut poem.txt
```

```python
!grep an poem.txt
```

# Redirection and Pipes

Most commands read from STDIN ("standard input") and write to STDOUT and STDERR.

 * Redirect a file to STDIN with `<`
 * Redirect STDOUT to a file with `>`
 * Redirect STDERR to a file with `2>`
 * Append STDOUT to a file with `>>`
 * Connect the STDOUT of one command with the STDIN of another with `|`


### example: searching through processes, outputting to a file

```python
#!ps waux
```

```python
!ps waux | grep python
```

```python
!ps waux | grep python | sort
```

```python
!ps waux | grep python | sort > processes.txt
```

#### example: echoing text into a new file, appending text to a file

```python
!ls
```

```python
!touch 'garbage.txt'
```

```python
!ls
```

```python
!cat garbage.txt
```

```python
!echo "this is trash" > garbage.txt
```

```python
!cat garbage.txt
```

```python
!echo "i have taken out the trash" > garbage.txt
```

```python
!cat garbage.txt
```

```python
!echo "then i took out the recycling" >> garbage.txt
```

```python
!cat garbage.txt
```

## Downloading from the web with `wget` and `curl`

```python
!ls
```

The default command to retrieve content from web servers is `curl -o` on Mac OS X. 

```python
!curl -o bee2.jpg https://upload.wikimedia.org/wikipedia/commons/7/77/Thomas_Bresson_-_Hym%C3%A9nopt%C3%A8re_sur_une_fleur_de_pissenlit_%28by%29.jpg
```

```python
!ls
```

To many Linux user, `wget` is the go-to tool for downloading; however it is not on Mac OS X by default. If you really like the original `wget` on Mac OS X, try install with `brew`

```python
#!brew install wget
```

```python
!wget https://upload.wikimedia.org/wikipedia/commons/4/42/Apis_mellifera_flying2.jpg
```

```python
!ls
```

# Permissions

[chmod examples & reference](https://www.computerhope.com/unix/uchmod.htm)

Unix can control file access per _user_, _user group_, and _everyone else_. 

Each file has read, write, and execute permissions for the owner, the group, and the world.

Examine with `ls -la`

```python
!ls -la
```

`d` signifies that the listing is a directory. `r`, `w`, and `x` mean "readable", "writable", and "executable".

The first three characters mark the permissions for the use that owns the file, the next three mark the permissions for the user group that owns the file, and the final three are the permissions for everyone else.

To modify these permissions, use `chmod`.


#### examples:
`chmod 400 <file>` gives read-only permissions to the file owner, and no permissions to the group & everyone else

`chmod 777 <file>` gives full read, write, and execute permission for the owner, group, and world


# [Regular Expressions](https://en.wikipedia.org/wiki/Regular_expression)

The `grep` command (and many languages) use regular expressions to match files.

Most characters match themselves. Some don't.

 * `.` matches anything other than a newline
 * `*` match zero or more of previous atom
 * `+` match one or more of previous atom
 * `|` match either previous or next item
 * `[abc0-9]` match any of characters within
 * `\` escape previous character
 * `\(\)` for grouping (use egrep to use without `\`)

[Learn regular expressions](https://regexone.com/)

[Play regex golf](https://alf.nu/RegexGolf)


# Environment Variables

List with `env`

Set with `VAR=foo`, or `export VAR=foo` when run from a script (e.g., your `.bash_profile`)


# Basic vi/vim

Two main modes

 * Insert mode (typing stuff inserts it in file)
 * Command mode (each key has meaning)

The *escape* key brings you to command mode; *i* enters insert mode

Helpful commands

 * `i` (enter insert mode)
 * `a` (enter insert mode after this character)
 * `dd` (delete a line)
 * `100G` (go to line 100)
 * `:wq` (save and exit)
 * `:q!` (exit without saving)


# How does my shell know where all these commands / programs are?

When you type a command, your shell looks for the executable file corresponding to that command. How does bash know where that file is?

For example, when you type `ls`, your shell runs the executable file `ls` in your `/bin` folder.

```python
!which ls
```

```python
#!ls /bin/
```

```python
!which grep
```

```python
!cowsay huh # if you don't have it, do brew install cowsay
```

```python
!which cowsay
```

The paths to all these executables is stored in the environment variable called PATH.

```python
!echo $PATH
```

When you type a command, `bash` looks for an executable with that name in these folders. If none are found, you get an error.

```python
!grok
```

### Customizing your shell

Perhaps you would like every shell session to start with certain environment variables already defined, or other conveniences.

Luckily, there's a file just for this purpose. Put `bash` commands in this file, and they will run every time you start a new shell session (most of the time, this mean "every time you open a new terminal").

On macOS, this file is called `.bash_profile`. On linux, it's called `.bashrc`. In both cases, it must live in your home folder `~`.


One convenient thing you can do is add aliases to common commands. Do you find yourself typing `ls -alh` all the time? Wouldn't it be nicer if that command were shorter? Well, just add 

`alias ll='ls -alh'`

to your `~/.bash_profile` (or `~/.bashrc` on Linux).

In order for these changes to take effect, you must either start a new session or run `source ~/.bash_profile`

## Lecture Credits

 * Moses Marsh
 * Miles Erickson
 * Ben Skrainka
 * Jack Bennetto
