AirBnB Clone Web Framework

Introduction
This project is a Flask web framework for an AirBnB clone, implementing various features and functionalities. 
The following README provides details on each task, including how to set up and run the web application.

Tasks
0. Hello Flask!
Description: Write a script that starts a Flask web application.
Routes:
/: Display "Hello HBNB!"
Notes: Make sure the application is listening on 0.0.0.0:5000 and use strict_slashes=False in the route definition.
1. HBNB
Description: Write a script that starts a Flask web application.
Routes:
/: Display "Hello HBNB!"
/hbnb: Display "HBNB"
Notes: Make sure the application is listening on 0.0.0.0:5000 and use strict_slashes=False in the route definition.
2. C is fun!
Description: Write a script that starts a Flask web application.
Routes:
/: Display "Hello HBNB!"
/hbnb: Display "HBNB"
/c/<text>: Display "C " followed by the value of the text variable (replace underscores with spaces)
Notes: Make sure the application is listening on 0.0.0.0:5000 and use strict_slashes=False in the route definition.
3. Python is cool!
Description: Write a script that starts a Flask web application.
Routes:
/: Display "Hello HBNB!"
/hbnb: Display "HBNB"
/c/<text>: Display "C " followed by the value of the text variable (replace underscores with spaces)
/python/<text>: Display "Python " followed by the value of the text variable (replace underscores with spaces). 
The default value of text is "is cool".
Notes: Make sure the application is listening on 0.0.0.0:5000 and use strict_slashes=False in the route definition.
4. Is it a number?
Description: Write a script that starts a Flask web application.
Routes:
/: Display "Hello HBNB!"
/hbnb: Display "HBNB"
/c/<text>: Display "C " followed by the value of the text variable (replace underscores with spaces)
/python/(<text>): Display "Python " followed by the value of the text variable (replace underscores with spaces). 
The default value of text is "is cool"./number/<n>: Display "n is a number" only if n is an integer.
Notes: Make sure the application is listening on 0.0.0.0:5000 and use strict_slashes=False in the route definition.
5. Number template
Description: Write a script that starts a Flask web application.
Routes:
/: Display "Hello HBNB!"
/hbnb: Display "HBNB"
/c/<text>: Display "C " followed by the value of the text variable (replace underscores with spaces)
/python/(<text>): Display "Python " followed by the value of the text variable (replace underscores with spaces).
The default value of text is "is cool"./number/<n>: Display "n is a number" only if n is an integer.
/number_template/<n>: Display an HTML page only if n is an integer:
H1 tag: "Number: n" inside the BODY tag.
Notes: Make sure the application is listening on 0.0.0.0:5000 and use strict_slashes=False in the route definition.
6. Odd or even?
Description: Write a script that starts a Flask web application.
Routes:
/: Display "Hello HBNB!"
/hbnb: Display "HBNB"
/c/<text>: Display "C " followed by the value of the text variable (replace underscores with spaces)
/python/(<text>): Display "Python " followed by the value of the text variable (replace underscores with spaces).
The default value of text is "is cool".
/number/<n>: Display "n is a number" only if n is an integer.
/number_template/<n>: Display an HTML page only if n is an integer:
H1 tag: "Number: n" inside the BODY tag.
/number_odd_or_even/<n>: Display an HTML page only if n is an integer:
H1 tag: "Number: n is even|odd" inside the BODY tag.
Notes: Make sure the application is listening on 0.0.0.0:5000 and use strict_slashes=False in the route definition.
7. Improve engines
Description: Before using Flask to display our HBNB data, you will need to update some part of our engine:
Update FileStorage: Add a public method def close(self): Call reload() method for deserializing the JSON file to objects.
Update DBStorage: Add a public method def close(self): Call remove() method on the private session attribute (self.__session) or close() on the class Session.
Update State (if not already present): If your storage engine is not DBStorage, add a public getter method cities to return the list of City objects from storage linked to the current State.
8. List of states
Description: Write a script that starts a Flask web application.
Routes:
/states_list: Display an HTML page:
H1 tag: "States"
UL tag: List of all State objects present in DBStorage sorted by name (A->Z)
LI tag: Description of one State: <state.id>: <B><state.name></B>
Notes:
Use the option strict_slashes=False in your route definition.
Make sure you have a running and valid setup_mysql_dev.sql in your AirBnB_clone_v2 repository.
Make sure all tables are created when you run echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db 
9. Cities by states
Description: Write a script that starts a Flask web application.
Routes:
/cities_by_states: Display an HTML page:
H1 tag: "States"
UL tag: List of all State objects present in DBStorage sorted by name (A->Z)
LI tag: Description of one State: <state.id>: <B><state.name></B> + UL tag: List of City objects linked to the State sorted by name (A->Z)
LI tag: Description of one City: <city.id>: <B><city.name></B>
Notes:
Use the option strict_slashes=False in your route definition.
Make sure you have a running and valid setup_mysql_dev.sql in your AirBnB_clone_v2 repository.
Make sure all tables are created when you run echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db
10. States and State
Description: Write a script that starts a Flask web application.
Routes:
/states: Display an HTML page:
H1 tag: "States"
UL tag: List of all State objects present in DBStorage sorted by name (A->Z)
LI tag: Description of one State: <state.id>: <B><state.name></B>
/states/<id>: Display an HTML page:
If a State object is found with this id:
H1 tag: "State: <state.name>"
H3 tag: "Cities:"
UL tag: List of City objects linked to the State sorted by name (A->Z)
LI tag: Description of one City: <city.id>: <B><city.name></B>
Otherwise:
H1 tag: "Not found!"
Notes:
Use the option strict_slashes=False in your route definition.
Make sure you have a running and valid setup_mysql_dev.sql in your AirBnB_clone_v2 repository.
Make sure all tables are created when you run echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db 
11. HBNB filters
Description: Write a script that starts a Flask web application.
Routes:
/hbnb_filters: Display an HTML page like 6-index.html, which was done during the project 0x01. AirBnB clone - Web static. Copy files 3-footer.css, 3-header.css, 4-common.css, and 6-filters.css from web_static/styles/ to the folder web_flask/static/styles. Copy files icon.png and logo.png from web_static/images/ to the folder web_flask/static/images. Update .popover class in 6-filters.css to allow scrolling in the popover and a max height of 300 pixels. Use 6-index.html content as the source code for the template 10-hbnb_filters.html: Replace the content of the H4 tag under each filter title (H3 States and H3 Amenities) by &nbsp;. State, City, and Amenity objects must be loaded from DBStorage and sorted by name (A->Z).
Notes:
Use the option strict_slashes=False in your route definition.
Make sure you have a running and valid setup_mysql_dev.sql in your AirBnB_clone_v2 repository.
Make sure all tables are created when you run echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
12. HBNB is alive!
Description: Write a script that starts a Flask web application.
Routes:
/hbnb: Display an HTML page like 8-index.html, done during the project 0x01. AirBnB clone - Web static. Copy files 3-footer.css, 3-header.css, 4-common.css, 6-filters.css, and 8-places.css from web_static/styles/ to the folder web_flask/static/styles. Copy all files from web_static/images/ to the folder web_flask/static/images. Update .popover class in 6-filters.css to enable scrolling in the popover and set max height to 300 pixels. Update 8-places.css to always have the price by night on the top right of each place element, and the name correctly aligned and visible. Use 8-index.html content as the source code for the template 100-hbnb.html: Replace the content of the H4 tag under each filter title (H3 States and H3 Amenities) by &nbsp;. Make sure all HTML tags from objects are correctly used (example: <BR /> must generate a new line). State, City, Amenity, and Place objects must be loaded from DBStorage and sorted by name (A->Z).
Notes:
Use the option strict_slashes=False in your route definition.
Make sure you have a running and valid setup_mysql_dev.sql in your AirBnB_clone_v2 repository.
Make sure all tables are created when you run echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db
