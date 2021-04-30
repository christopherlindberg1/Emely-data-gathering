# Emely data gathering
This website is used to gather data for a ML-model. The model shall be trained to ask appropriate follow-up questions in a dialogue. The only purpose with this website is to gather the data, not train the model.

## Tech
The website is built with the following technologies:
* Python
* Flask

## Dependencies
To run this website locally you need to install all of its dependencies.

### Install Python 3.9 to your computer
Python 3.9 is the language that the server is written in. Follow the instructions at https://www.python.org/downloads/ and install Python version 3.9 to your computer.

**Then create a project folder and cd into it:**

```
$ mkdir <project-name>
$ cd <project-name>
```

### Virtual environment
Create a virtual environment for the project.

**Ubuntu Linux**

If you are using Ubuntu Linux you will first have to install the virtual environment module before you can create one:

```
$ sudo apt-get install python3-venv
```

Then create a virtual environment in the project folder that you created earlier:

**Mac & Linux:**
```
$ python3 -m venv <venv-name>
```

**Windows:**
```
$ py -3 -m venv <venv-name>
```

Now activate the virtual environment with the following command:

**Mac & Linux:**
```
$ . venv/bin/activate
```

**Windows:**
```
$ venv\Scripts\activate
```

When the virtual environment is activate its name will be visible to the far left in the search path in the terminal / command prompt.

### Install Flask
Flask is used to build the web server. Install Flask within the virtual environment. The virtual environment must be activated.

```
$ pip install flask
```

```
pip install WTForms
```

```
pip install Flask-WTF
```