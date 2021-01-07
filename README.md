# dependencies

- flask
- python-dotenv
- Flask-PyMongo
- markdown2

# run

run with `--host=0.0.0.0` for local network testing

### windows

```
> mongod --dbpath .\data\db
> venv\Scripts\activate
> flask run
```

### linux

```
$ mongod --dbpath ./data/db
$ source ./venv/bin/activate
$ flask run
```
