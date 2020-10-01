# flask-jobs

[![Language](https://img.shields.io/badge/language-python-brightgreen?style=flat-square)](https://www.python.org/)

Hello everyone! This is the repository of Flask REST-API for [mezidia-jobs](https://github.com/mezidia/mezidia-jobs).

> This project is experimental

## Table of contents

- [Table of contents](#table-of-contents)
- [Motivation](#motivation)
- [Build status](#build-status)
- [Badges](#badges)
- [Screenshots](#screenshots)
- [Tech/framework used](#techframework-used)
- [Features](#features)
- [Installation](#installation)
- [Fast usage](#fast-usage)
- [Contribute](#contribute)
- [Credits](#credits)
- [License](#license)

## Motivation

I have just wanted to try make my own REST API, so I choosed **Flask** and started working.🔨

## Build status

Here you can see build status of [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration):

![Lint Code Base](https://github.com/mezidia/flask-jobs/workflows/Lint%20Code%20Base/badge.svg)
[![Build Status](https://travis-ci.com/mezidia/flask-jobs.svg?branch=master)](https://travis-ci.com/mezidia/flask-jobs)

I have direct [continuous deployment](https://en.wikipedia.org/wiki/Continuous_deployment) to [Heroku](https://www.heroku.com/).

## Badges

[![Theme](https://img.shields.io/badge/Theme-REST_API-brightgreen?style=flat-square)](https://uk.wikipedia.org/wiki/REST)
[![Platform](https://img.shields.io/badge/Platform-Flask-brightgreen?style=flat-square)](https://flask.palletsprojects.com/en/1.1.x/)


## Screenshots

## Tech/framework used

**Built with**

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)

## Features

On the website you can **see** all available jobs, **search** one, **create** and **edit** jobs, if you have administrator rights.

## Installation

1. Clone this repository by the command in terminal or by [GitHub CLI](https://cli.github.com/):

```bash
# git
git clone https://github.com/mezidia/flask-jobs.git
# GitHub CLI
gh repo clone mezidia/flask-jobs
```

2. Create virtual environment:

```bash
python -m venv .venv
```

3. Activate this environment:

```bash
.venv/Scripts/activate.bat
```

4. Install packages with [pip](https://pip.pypa.io/en/stable/):

```bash
pip install -r requirements.txt
```

## Fast usage

1. Rename `.env_sample` to `.env` and set your values:

2. Start the development server:

```python
python app.py
```

3. Open in browser `http://127.0.0.1:5000/`

## Contribute

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Also look at the [CONTRIBUTING.md](https://github.com/mezidia/flask-jobs/blob/master/CONTRIBUTING.md).

## Credits

Links to video which inspired me to build this project: 

- [REST API With Flask & SQL Alchemy](https://www.youtube.com/watch?v=PTZiDnuC86g)

## License

MIT © [mezgoodle](https://github.com/mezgoodle)
