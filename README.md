AirBnB Clone - MySQL Tasks
Overview
This project is an extension of an existing AirBnB clone codebase, focusing on MySQL tasks. The primary goal is to transition from the FileStorage engine to the DBStorage engine using SQLAlchemy, allowing for improved database management.

Project Structure
Bug Free!

Ensure that all unit tests pass without errors using the unittest module.
Use the skipIf feature of the Unittest module to exclude tests that are not relevant for a specific storage type.
Console Improvements

Update the do_create function in console.py to allow for object creation with given parameters.
Command syntax: create <Class name> <param 1> <param 2> <param 3>...
Param syntax: <key name>=<value>
Support string, float, and integer parameters.
MySQL Setup Development

Write a script (setup_mysql_dev.sql) to prepare a MySQL server for development:
Database: hbnb_dev_db
User: hbnb_dev
Password for hbnb_dev: hbnb_dev_pwd
Privileges: All on hbnb_dev_db, SELECT on performance_schema
MySQL Setup Test

Write a script (setup_mysql_test.sql) to prepare a MySQL server for testing:
Database: hbnb_test_db
User: hbnb_test
Password for hbnb_test: hbnb_test_pwd
Privileges: All on hbnb_test_db, SELECT on performance_schema
Delete Object

Update FileStorage to include a new public instance method delete(self, obj=None) that deletes an object from __objects.
Update the prototype of def all(self) to def all(self, cls=None) for optional filtering.
DBStorage - States and Cities

Transition from FileStorage to DBStorage using SQLAlchemy.
Update BaseModel, City, and State classes.
Implement DBStorage with features such as creating tables, querying objects, adding objects, saving changes, and reloading the session.
DBStorage - User

Update the User class to include attributes for SQLAlchemy.
User inherits from BaseModel and Base.
Add or replace class attributes for the table name, email, password, first_name, and last_name.
DBStorage - Place

Update the Place class to include attributes for SQLAlchemy.
Place inherits from BaseModel and Base.
Add or replace class attributes for the table name, city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, and longitude.
