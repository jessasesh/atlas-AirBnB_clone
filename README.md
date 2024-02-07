<img src="https://github.com/lukeschula/atlas-AirBnB_clone/assets/126801159/88e499f5-38c2-4d16-b33b-4e541177bdd9" width="100%" height="50%" >


# AirBnB Clone

Hey there! This a partner project for school and it's the first step towards building our first full web application. This will be a progressive project that will later include HTML/CSS templating, database storage, API, and front-end integration.

![815046647d23428a14ca](https://github.com/lukeschula/atlas-AirBnB_clone/assets/126801159/1bdf09c5-784b-4404-8411-379bf23ee55e)  

##### Navigating the Project

*  [What is it?](#the-command-interpreter)

*  [How to start it?](#how-to-start)

*  [How to get it?](#installation)

*  [How to use?](#how-to-use)

*  [What's in it?](#contents)

*  [What does it look like?](#examples-of-program-behavior)

*  [Who created it?](#authors)
    
## The Command Interpreter
The AirBnB Clone Console is a Python-based command-line interface (CLI) that allows you to manage AirBnB-like objects, such as users, states, cities, places, and more. With this console, you can perform various operations on these objects, including creating, retrieving, updating, and deleting them.

## How to start
1. Install.
	- Check system requirements.
2. Clone into repository.
3. Check out content and available commands.
4. Run the Program.

### Installation
###### This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3), jQuery (version 3.x), MySQL (version 5.7), Flask, and Chrome (version 57.0).
Clone into the repository <br>
```
git clone https://github.com/lukeschula/atlas-AirBnB_clone.git
```

## How to use
After cloning into the repository, you will need to:
1. Navigate to the project directory. <br>
   `cd atlas-AirBnB_clone`
3. Check out content and available commands.
4. Run the program and have fun:) <br>
   `./console.py`

> A prompt will be printed on the screen (hbnb) and waits for the users input.

#### Contents
| File Name | Description |
|--|--|
|[console.py](https://github.com/lukeschula/atlas-AirBnB_clone/blob/main/console.py)|entry point of the command interpreter|
|[models](https://github.com/lukeschula/atlas-AirBnB_clone/tree/main/models)|directory that defines classes and their attributes |
|[base_model.py](https://github.com/lukeschula/atlas-AirBnB_clone/blob/main/models/base_model.py)|all common attributes/methods for other classes|
|[amenity.py](https://github.com/lukeschula/atlas-AirBnB_clone/blob/main/models/amenity.py)|defines amenity class|
|[city.py](https://github.com/lukeschula/atlas-AirBnB_clone/blob/main/models/city.py)|defines city class|
|[place.py](https://github.com/lukeschula/atlas-AirBnB_clone/blob/main/models/place.py)|defines place class|
|[review.py](https://github.com/lukeschula/atlas-AirBnB_clone/blob/main/models/review.py)|defines review by user class|
|[state.py](https://github.com/lukeschula/atlas-AirBnB_clone/blob/main/models/state.py)|defines state class|
|[user.py](https://github.com/lukeschula/atlas-AirBnB_clone/blob/main/models/user.py)|defines user class|
|[engine](https://github.com/lukeschula/atlas-AirBnB_clone/tree/main/models/engine)|directory that conatins the storage engine needed to save user input|
|[file_storage.py](https://github.com/lukeschula/atlas-AirBnB_clone/blob/main/models/engine/file_storage.py)|converts input for storage|
|[tests](https://github.com/lukeschula/atlas-AirBnB_clone/tree/main/tests)|directory contains all unit test cases for this project|
|[AUTHORS](https://github.com/lukeschula/atlas-AirBnB_clone/blob/main/AUTHORS)|list of who worked on the project|
|[README.md](https://github.com/lukeschula/atlas-AirBnB_clone/blob/main/README.md)|contains information about project|
<details>
<summary> Commands Available </summary>
<br>
	
- `help <command>`
- `create <class>`
- `show <class> <id>`
- `destroy <class> <id>`
- `all` or `all <class>`
- `update <class> <id> <attribute name> "<attribute value>"`
- `EOF`
- `quit`

</details>

### Examples of program behavior  

###### Interactive mode

```
$ ./console.py

(hbnb) help

  

Documented commands (type help <topic>):

========================================

EOF help quit

  

(hbnb)

(hbnb)

(hbnb) quit

$
```

###### Non-interactive mode

```

$ echo "help" | ./console.py

(hbnb)

  

Documented commands (type help <topic>):

========================================

EOF help quit

(hbnb)

$

$ cat test_help

help

$

$ cat test_help | ./console.py

(hbnb)

  

Documented commands (type help <topic>):

========================================

EOF help quit

(hbnb)

$
```

 
  


### Authors
Luke Schula(https://github.com/lukeschula) <br> 
Jess Dison(https://github.com/jessasesh)

![images](https://github.com/lukeschula/atlas-AirBnB_clone/assets/126801159/c7951a80-32c7-4da7-82c9-fc4347038846)
