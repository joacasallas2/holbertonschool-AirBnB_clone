AirBnB clone - The console
==========================

Concepts
--------

*For this project, students are expected to look at these concepts:*

-   [Python packages](https://intranet.hbtn.io/concepts/66)
-   [AirBnB clone](https://intranet.hbtn.io/concepts/74)


Background Context  
------------------  

Welcome to the AirBnB clone project!  

### First step: Write a command interpreter to manage your AirBnB objects.  

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…  

Each task is linked and will help you to:  

* Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances  
* Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file  
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel  
* create the first abstracted storage engine of the project: File storage.  
* create all unittests to validate all our classes and storage engine  

### What’s a command interpreter?  

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
  
  * Create a new object (ex: a new User or a new Place)  
  * Retrieve an object from a file, a database etc…  
  * Do operations on objects (count, compute stats, etc…)  
  * Update attributes of an object  
  * Destroy an object


Resources
---------

**Read or watch**:

-   [cmd module](https://docs.python.org/3/library/cmd.html)
-   [packages]()
-   [uuid module](https://docs.python.org/3/library/uuid.html)
-   [datetime](https://docs.python.org/3/library/uuid.html)
-   [unittest module](https://docs.python.org/3/library/uuid.html)
-   [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
-   [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/ "explain to anyone"), **without the help of Google**:

### General

- How to create a Python package  
- How to create a command interpreter in Python using the cmd module  
- What is Unit testing and how to implement it in a large project  
- How to serialize and deserialize a Class  
- How to write and read a JSON file  
- How to manage datetime  
- What is an UUID  
- What is *args and how to use it  
- What is **kwargs and how to use it  
- How to handle named arguments in a function


More Info
---------

### Execution  

Your shell should work like this in interactive mode:

`
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
`
But also in non-interactive mode: (like the Shell project in C)  

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`


![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240716%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240716T215649Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ddf21d1e57903b883496753a932775ff3ec00ea0f255b6a6c8dae458da4b5a64)  


## Tasks ##  
0. [0. README, AUTHORS](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/README.md)
0. [0. README, AUTHORS](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/AUTHORS)
1. [1. Be pycodestyle compliant!](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/console.py)
1. [1. Be pycodestyle compliant!](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/models/base_model.py)
1. [1. Be pycodestyle compliant!](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/models/user.py)
1. [1. Be pycodestyle compliant!](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/models/place.py)
1. [1. Be pycodestyle compliant!](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/models/state.py)
1. [1. Be pycodestyle compliant!](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/models/city.py)
1. [1. Be pycodestyle compliant!](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/models/amenity.py)
1. [1. Be pycodestyle compliant!](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/models/review.py)
1. [1. Be pycodestyle compliant!](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py)
1. [2. Unittests](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/tests/)
1. [3. BaseModel](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/models/base_model.py)
1. [4. Create BaseModel from dictionary](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/models/base_model.py)
1. [5. Store first object](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py)
1. [6. Console 0.0.1](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/console.py)
1. [7. Console 0.1](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/console.py)
1. [8. First User](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/models/user.py)
1. [9. More classes!](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/models/state.py)
1. [10. Console 1.0](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/console.py)
1. [11. All instances by class name](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/console.py)
1. [12. Count instances](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/console.py)
1. [13. Show](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/console.py)
1. [14. Destroy](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/console.py)
1. [15. Update](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/console.py)
1. [16. Update from dictionary](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/console.py)
1. [17. Unittests for the Console!](https://github.com/joacasallas2/holbertonschool-AirBnB_clone/blob/main/tests/test_console.py)

## Autor:  joacasallas :information_desk_person:  
contact:  joacasallas@gmail.com
