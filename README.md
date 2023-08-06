# AirBnB clone - MySQL

<img align="center" alt="AirBnb_clone_logo" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/AirBnB_clone.png?raw=true" />

## Table of contents

1. [AirBnB clone Overview](#airbnb-clone-overview)

2. [AirBnB clone - MySQL](#airbnb-clone---mysql)
   * [Diagram](#diagram)
   * [File structure](#file-structure)
   * [Usage](#usage)
   * [Unit tests](#unit-tests)

3. [Authors](#Authors)

## AirBnB clone Overview

 The goal of the project is to build a simple copy of the [AirBnB website](https://www.airbnb.com/)

 Here is a preview of the final product.

 <img align="center" alt="AirBnb_final_product" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/AirBnB_final_product.png?raw=true" />

At the end of the project the complete web application will be composed by:

- __A command interpreter__ to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- __A website (the front-end)__ that shows the final product to everybody: static and dynamic
- __A database or files__ that store data (data = objects)
- __An API__ that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)


### Diagram

The following is a diagram of this stage related with MySQL:

In this stage, the main objectives are:

* Replace the file storage by a Database storage
* Map the models to a table in database by using an O.R.M.

 <img align="center" alt="AirBnb_console_diagram" src="https://github.com/cristian-encalada/holbertonschool-AirBnB_clone/blob/assets/AirBnB_MySQL_storage.png?raw=true" />

### File structure

For the implementation, the following file structure was defined:

```sh
[cristian@ArchKDE holbertonschool-AirBnB_clone_v2]$ tree .
.
├── AUTHORS
├── console.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── db_storage.py
│   │   ├── file_storage.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
├── setup_mysql_dev.sql
├── setup_mysql_test.sql
├── tests
│   ├── __init__.py
│   └── test_models
│       ├── __init__.py
│       ├── test_amenity.py
│       ├── test_base_model.py
│       ├── test_city.py
│       ├── test_engine
│       │   ├── __init__.py
│       │   ├── test_db_storage.py
│       │   └── test_file_storage.py
│       ├── test_place.py
│       ├── test_review.py
│       ├── test_state.py
│       └── test_user.py
└── web_static
    ├── 0-index.html
    ├── 100-index.html
    ├── 101-index.html
    ├── 102-index.html
    ├── 103-index.html
    ├── 1-index.html
    ├── 2-index.html
    ├── 3-index.html
    ├── 4-index.html
    ├── 5-index.html
    ├── 6-index.html
    ├── 7-index.html
    ├── 8-index.html
    ├── images
    │   ├── icon_bath.png
    │   ├── icon_bed.png
    │   ├── icon_group.png
    │   ├── icon.ico
    │   ├── icon_pets.png
    │   ├── icon_tv.png
    │   ├── icon_wifi.png
    │   └── logo.png
    ├── README.md
    └── styles
        ├── 100-places.css
        ├── 101-places.css
        ├── 102-common.css
        ├── 102-filters.css
        ├── 102-footer.css
        ├── 102-header.css
        ├── 102-places.css
        ├── 103-common.css
        ├── 103-filters.css
        ├── 103-footer.css
        ├── 103-header.css
        ├── 103-places.css
        ├── 2-common.css
        ├── 2-footer.css
        ├── 2-header.css
        ├── 3-common.css
        ├── 3-footer.css
        ├── 3-header.css
        ├── 4-common.css
        ├── 4-filters.css
        ├── 5-filters.css
        ├── 6-filters.css
        ├── 7-places.css
        └── 8-places.css

9 directories, 74 files
```

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](./AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](./tests/) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](./models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](./models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](./models/engine/file_storage.py) [/models/_ _init_ _.py](./models/__init__.py) [/models/base_model.py](./models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](./console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](./console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](./console.py) [/models/engine/file_storage.py](./models/engine/file_storage.py) [/models/user.py](./models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](./models/user.py) [/models/place.py](./models/place.py) [/models/city.py](./models/city.py) [/models/amenity.py](./models/amenity.py) [/models/state.py](./models/state.py) [/models/review.py](./models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](./console.py) [/models/engine/file_storage.py](./models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>

### Usage

<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>

### Unit tests

All unittests pass without any errors at anytime in this project, with each storage engine.

__Unit tests related to File storage (JSON format)__

```sh
[cristian@ArchKDE holbertonschool-AirBnB_clone_v2]$ python3 -m unittest discover tests
..........................................................s....Key in loop: BaseModel.b588d112-f39c-4102-b8cd-fb086ed73fa5
.......<class 'models.engine.file_storage.FileStorage'>
..............................................................................................................
----------------------------------------------------------------------
Ran 179 tests in 0.068s

OK (skipped=1)
```

__Unit tests related to DB storage__

```sh
[cristian@ArchKDE holbertonschool-AirBnB_clone_v2]$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests
........s..........s..........s...........s...........s.....ssssssssssssss.................s...........s..........s...........s............s...........s..............s..........s...
----------------------------------------------------------------------
Ran 181 tests in 2.568s

OK (skipped=27)
```

## Authors

* __Cristian Encalada__ - *Holberton Student*
   - Github: [Cristian Encalada](https://github.com/cristian-encalada)
* __Emily Sanchez__ - *Holberton Student*
   - Github: [Emily Sanchez](https://github.com/20Emi)