# AirBnB clone - The Console

## Table of contents
* [Description of the project](#description-of-the-project)
* [Command Interpreter](#command-interpreter)

## Description of the project
This is the first step towards building a full web application: the **AirBnB clone**.

## Command Interpreter
* [Description](#description)
* [How to start](#how-to-start)
* [How to use](#how-to-use)
* [Examples](#examples)

## Description
The **Command Interpreter** is created for manage the AirBnB objects. With the **Command Interpreter** you can create a new object, retrieve an object from a file, do operations on objects, update attributes of an object, destroy an object among other.
 
 
 
## How to start
To start the **Command Interpreter** just type **./console.py** and will be prompt **(hbnb)** to write the commands.
 
 
 
## How to use
This **Command Interpreter** has some commands implemented such as:
 
```
$ help
$ EOF
$ quit
$ create
$ show
$ destroy
$ all
$ update
```
 
 
Some of these commands need arguments to retrieve some information.
 
**See Examples**
 
 
 
## Examples
 
#### *Start the Command Interpreter*
 
```
user@ubuntu:~/AirBnB$ ./console.py
(hbnb)
```
 



#### *Using help command*
 
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
 
If type *help* with other command you can retrieve the documentation of that command.
```
(hbnb) help quit
Quit command to exit the program

(hbnb) quit
user@ubuntu:~/AirBnB$
```
 


 
#### *Using EOF command*
To exit the program
 
```
user@ubuntu:~/AirBnB$ ./console.py
(hbnb) EOF
user@ubuntu:~/AirBnB$
```
 
 


#### *Using quit command*
To exit the program
 
```
user@ubuntu:~/AirBnB$ ./console.py
(hbnb) quit
user@ubunt:~/AirBnB$
```
 
 


#### *Using create command*
Create a new instance based in a class and print the id. This command need a class name as argument.
 
```
user@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) quit
user@ubuntu:~/AirBnB$
```




#### *Using show command*
Prints the string representation of an instance. This command nedd a class name and id as argument.

```
user@ubuntu:~/AirBnB$ ./console.py
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) quit
user@ubuntu:~/AirBnB$
```




#### *Using destroy command*
Delete an instance. This command need a class name and id as argument.

```
user@ubuntu:~/AirBnB$ ./console.py
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
*** no instance found ***
(hbnb) quit
user@ubuntu:~/AirBnB$
```




#### *Using all command*
Prints all string representation of all instances based or not on the class name. 

```
user@ubuntu:~/AirBnB$ ./console.py
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}", "[State] (0986ef5c-467c-4f82-9521-a772ea7123er) {'id': '0986ef5c-467c-4f82-9521-a772ea7123er', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[City] (76tgff9a-6318-451f-87b6-910505c89675) {'first_name': 'Betty', 'id': '76tgff9a-6318-451f-87b6-910505c89675', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) quit
user@ubuntu:~/AirBnB$
```




#### *Using update command*
Updates an instance based on the class name and id by adding or updating attribute.

```
user@ubuntu:~/AirBnB$ ./console.py
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) quit
user@ubuntu:~/AirBnB$
```
