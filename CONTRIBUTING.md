### Install Virtualenv
Virtualenv is the best way to isolate your python environment from the python which is used for the system to run. **It is highly recomended to use virtualenv**
#### Install with pip
```bash
$ sudo pip install virtualenv
```
#### Install with apt-get (Debian based)
```bash
$ sudo apt-get install python3-virtualenv
```
#### Create the virtualenv
```bash
$ mkdir myproject
$ cd myproject
$ virtualenv venv
New python executable in venv/bin/python
Installing setuptools, pip............done.
```

#### Activate virtualenv
```bash
$ . venv/bin/activate
```

### Development
The package *tinyengine* is the core of the project.
The *engine* module is the core of the engine
The app.py file is the file to run the project for tests and development. For further examples of how to use the engine, see what is already written on app.py
