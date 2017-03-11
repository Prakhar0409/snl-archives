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

### Running the project

* The project uses python3. To get it running first setup using instruction above and then go to your base project directory where you cloned it. (Activate the virtualenv using `source venv/bin/activate` if not already active)
* `cd snl-dbms/snl`
* `python manage.py runserver 0.0.0.0 8000`
* You should now be able to see the project live at `127.0.0.1:8000`

Note: For installing virtualenv and setting up git config and other proxy config please check out the web. 