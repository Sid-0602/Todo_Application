# Documentation and Syntaxes

## Virtualenv (venv)

[virtualenv](`<a href="https://virtualenv.pypa.io/en/stable/">virtualenv</a>`) is a tool used to create isolated Python environments. It creates a folder which contains all the necessary executables to use the packages that a Python project would need.

### Installations

```text
pip install virtualenv
```

### **Create an Environment**

To create a virtual environment use:

```text
virtualenv --no-site-packages my-env
```

This creates a folder in the current directory with the name of the environment (`my-env/`). This folder contains the directories for installing modules and Python executables.

You can also specify the Python version you want to work with. Just use the argument `--python=/path/to/python/version`.

 Read More at : [FreeCodeCamp](https://www.freecodecamp.org/news/python-virtual-environments-explained-with-examples/)

Note: Before running env on windows, resolve the following issue(if encountered).

#### "Fix for PowerShell Script cannot be loaded because running scripts is disabled on this system error "

[Refer this](https://www.sharepointdiary.com/2014/03/fix-for-powershell-script-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system.html)

## Flask

Flask depends on the WerkZeug WSGI toolkit, the Jinja template engine, and the CLI toolkit.

### Installation

* Python Version:  We recommend using the latest version of Python. Flask supports Python 3.8 and newer.
* Dependencies :-  These distributions will be installed automatically when installing Flask.
* Werkzeug implements WSGI, the standard Python interface between applications and servers.
* Jinja is a template language that renders the pages your application serves.
* MarkupSafe comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.
* Blinker provides support for Signals.

Within the activated environment, use the following command to install Flask:

```
$pipinstallFlask
```

### Issue Fix: "RuntimeError: Working outside of application context."

Solution:

Open the python terminal in your project directory and manually add a context

```python
from project_name import app, db
app.app_context().push()
db.create_all()
```

## Jinja Template

Jinja2 is a modern day templating language for Python developers. It was made after Django's template. It is used to create HTML, XML or other markup formats that are returned to the user via an HTTP request.

#### How To Get Jinja 2

```
pip install jinja2
```

#### Why do we need Jinja 2

1. Sandboxed Execution: It provides a protected framework for automation of testing programs, whose behaviour is unknown and must be investigated.
2. HTML Escaping: Jinja 2 has a powerful automatic HTML Escaping, which helps preventing Cross-site Scripting. (There are special characters like >,<,&, etc. which carry special meanings in the templates. So, if you want to use them as regular text in your documents then, replace them with entities. Not doing so might lead to XSS-Attack.
3. Template Inheritance: This is the most important feature, which I will expand on to later in the post.

#### Delimiters

* `{%....%}` are for statements
* `{{....}}` are expressions used to print to template output
* `{#....#}` are for comments which are not included in the template output
* `#....##` are used as line statements

## SQLAlchemy

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

Issue fix: "[sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table](https://stackoverflow.com/questions/44941757/sqlalchemy-exc-operationalerror-sqlite3-operationalerror-no-such-table)" .

Solution: 

**Very simple solution:** in the app.py or main.py you can just add these lines of code for fixing this issue:

```ruby
@app.before_first_request
def create_tables():
    db.create_all()
```
