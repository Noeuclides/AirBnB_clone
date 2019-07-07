# AirBnB Clone
![Airbnb Clone](https://camo.githubusercontent.com/70996d3dcffa41c27a6f5d59f56a42d978a4684c/687474703a2f2f696d6775722e636f6d2f4a42434d4844502e706e67)

**AirBnB Clone:** In this clone you'll have some of the original Airbnb features.

## The Console
### How To Start:
In order to use the console you have to clone this repository with the following command:
```bash
$ git clone https://github.com/ryanhudson/AirBnB_clone
```

### Usage
* Then you can run the `console.py` file with the following command:

    * option 1:
    ```sh
    $ ./console.py
    ```

    * option 2:
    ```bash
    $ python3 console.py
    ```
    *You may want to install Python 3.4.3 to use the console rightly.*

### How to use it:
#### a. Interective mode:
When you run one of the last two lines you are in the interactive mode:
![alt text](https://raw.githubusercontent.com/ryanhudson/AirBnB_clone/master/images/Screenshot_2019-07-04%20Holberton%20School's%20awesome%20intranet(1).png)

#### b. No interactive mode
Also, you can run the console in a non-interactive mode:
![alt text](https://raw.githubusercontent.com/ryanhudson/AirBnB_clone/master/images/Screenshot_2019-07-04%20Holberton%20School's%20awesome%20intranet.png)

The console has some classes that the user have access to:

| Class name | Class attributes |
| -------- | ----------------- |
| User|email - password - first_name - last_name|
| State | name |
| City | state_id - name |
| Amenity | name |
| Place | city_id - user_id - name - description - number_rooms - number_bathrooms - max_guest - price_by_night - latitude - longitude - amenity_ids |
| Review | place_id - user_id - text |

Now, in the console, you have access to some methods that you can use in order to change some of the attributes of the classes:

| Method | Description | Usage |
| --- | --- | -------- |
| create | creates a new instance of the class | create <class name> |
| show | prints the string representation of the instance by its class name | show <class name> <id> |
| destroy | deletes an instance based on the class name and id | destroy <class name> <id> |
| all | prints all the string representation of all instance based or not on the class name | all or all <class name> |
| update | updates an instance based on the class name and id by adding or updating attribute | update <class name> <id> <attribute name> "<attribute value>" |


### Example Usage
You can create your own instance:
![create example](https://raw.githubusercontent.com/ryanhudson/AirBnB_clone/master/images/consolecreate.PNG)

Then you can use all command to see what instance have been created:
![all example](https://raw.githubusercontent.com/ryanhudson/AirBnB_clone/master/images/consoleall.PNG)

Use destroy to delete some instance. In the example below we `destroy` an `User`, and then use `show` to see if it was successfully deleted. As you can see the console shows the message `** no instance found **` so we made it:
![destroy example](https://raw.githubusercontent.com/ryanhudson/AirBnB_clone/master/images/consolesdestroy.PNG)

The console allows the user to update some instance attributes as follow:
![update example](https://raw.githubusercontent.com/ryanhudson/AirBnB_clone/master/images/consoleupdate.PNG)
You see that we are updating the attribute `first_name` of the `User` instance, then you can see the changes with the show command.

Also, the console has another syntax that you can use if you want (with the additional feature `<class name>.count()` where you can count the number of instance of that class):
```python
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb)
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")
(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
(hbnb)
(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'age': 89, 'first_name': 'John', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@holbertonshool.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}
(hbnb) User.count()
1
(hbnb)
```
### License
This document is for the first console release (1.0)

### Links & Tech
Operating systems (OS)
* [Linux](https://www.linux.org)
* [Ubuntu 14.04](http://releases.ubuntu.com/14.04/)

Editors
* [vim text editor](https://www.vim.org/)
* [Emacs](https://www.gnu.org/software/emacs/)

Code
* [Source code](https://github.com/ryanhudson/AirBnB_clone)

Compilator
* [Python](https://www.python.org/downloads/release/python-373/)

### Authors

Ryan Hudson <ryan.e.hudson@gmail.com>

Nicolás Martínez <euclidesnoeuclides@gmail.com>

To generate authors file, check this link out:

https://github.com/moby/moby/blob/master/hack/generate-authors.sh