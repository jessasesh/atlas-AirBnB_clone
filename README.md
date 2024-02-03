AirBnB Clone
============

<img> 
#Description of the project
This is the first step towards building our first full web application. This will be a progressive project that will later include HTML/CSS templating, database storage, API, and front-end integration.

<img>

Table of contents
<details>
<summary></summary>
</details>


#Description of the command interpreter

##How to start it

Installation and requirements
Link
Download pic
./console.py

##How to use it
This console has the ability to work in both interactive and non-interactive modes. A prompt will be printed on the screen (hbnb), and waits for the users input.

###Interactive mode
'''
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
'''
###Non-interactive mode
'''
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
'''


Command | Example
------- | -------
Run the console | ```./console.py```
Quit the console | ```(hbnb) quit```
Display the help for a command | ```(hbnb) help <command>```
Create an object (prints its id)| ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Destroy an object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"```

##Examples


##Authors
Luke Schula(https://github.com/lukeschula) & Jess Dison(https://github.com/jessasesh)