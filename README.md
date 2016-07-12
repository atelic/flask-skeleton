# Flask Skeleton

Flask starter project with SQLAlchemy, Flask-login, Bourbon/Neat/Bitters, and Reactjs.

## Quick Start

### Basics

1. Activate a virtualenv
```sh
$ mkvirtualenv flask-skeleton
```
2. Install the requirements
```sh
$ pip install -r requirements
```

### Set Environment Variables

Update `project/server/config.py`, and then run:

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.server.config.ProductionConfig"
```

### Create DB

```sh
$ inv init
```

### Run the Application

```sh
$ inv server
```

So access the application at the address [http://localhost:5000/](http://localhost:5000/)

> Want to specify a different port?

> ```sh
> $ inv server --port 4567
> ```

### Testing

Without coverage:

```sh
$ inv test
```

With coverage:

```sh
$ inv cov
```
