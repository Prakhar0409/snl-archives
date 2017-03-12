# Saturday Night Live

## Developer Guide

### Setting up the project

* Go to the desired directory, where you want to get the project code.
* `git clone https://github.com/Prakhar0409/snl-dbms.git`
  * Enter your username and password if and when prompted for to get the code
* `cd snl-dbms`
* `virtualenv -p python3 venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* To check if you can now run the project, see the instructions below

* To set up the database:
  * open postgresql
  * create a user with username: `snl` and password: `snl_live`. 
  * create a database with name `snldb` and owner `snl`
* Get back to you project (in the directory where manage.py resides) and type `python manage.py migrate`


### Running the project

* The project uses python3. To get it running first setup using instruction above and then go to your base project directory where you cloned it. (Activate the virtualenv using `source venv/bin/activate` if not already active)
* `cd snl-dbms/snl`
* `python manage.py runserver 0.0.0.0 8000`
* You should now be able to see the project live at `127.0.0.1:8000`

Note: For installing virtualenv and setting up git config and other proxy config please check out the web. 

## Unforseen Difficulties & Challenges

1. Dataset picked from kaggle was not even in 1NF. The table snl_episode had non atomic values for hosts. It had JSON Array, so we had to write a script to parse the values into atomic fashion and change key to include hosts in the key, since all other attributes would have same values for a entry split.
2. Other anamolies in the dataset. Also various columns had no values.
3. Rows pointed to foreign keys which did not exist in other tables. For this those rows were manually removed to maintain refrential integrity.

## TODO

- [x] Setup for the dataset
- [X] Create views - main page, all episodes, episode x, all seasons, season x, title x, all hosts, all actors, popular (test pages only)
- [ ] Get the backend queries right
- [ ] make a frontend
- [ ] integrate
- [ ] add reporting newer data feature
- [ ] logging in if possible

## BUGS

- Actor ID (aid) has spaces //change them to underscores or something everywhere - or replace underscore with space after getting the aid
