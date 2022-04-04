# REST API with FastAPI, PostgreSQL, Alembic, SQLAlchemy and Minio (S3 cloud storage)

FastAPI is a Python framework and set of tools that allow developers to invoke commonly used functions using a REST interface. 

SQLAlchemy is a package that makes it easier for Python programs to communicate with databases. Most of the time, this library is used as an Object Relational Mapper (ORM) tool, which automatically converts function calls to SQL queries and translates Python classes to tables on relational databases.

Many web, mobile, geospatial, and analytics applications use PostgreSQL as their primary data storage or data warehouse.

Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.

Minio is a popular open source object storage server compatible with Amazon S3 cloud storage.

## How to run the REST API
Get this project from Github
``` 
git clone https://github.com/sav116/RESTful-API
 
```

### Installing PostgreSQL
Adding environment variables
```
SRC_DB_DATA=~/db_data
POSTGRES_DB=back_end
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

Creating directory for volume of database
```
mkdir $SRC_DB_DATA
```

Start db container
```
docker run -d --name my_postgres \
 -v $SRC_DB_DATA:/var/lib/postgresql/data -p 5432:5432 \
 -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
 -e POSTGRES_USER=$POSTGRES_USER \
 -e POSTGRES_DB=$POSTGRES_DB \
 postgres:14
```


### Create a virtual environment
This can be done with 
``` python -m venv env ```

activate the virtual environment with 

``` 
env/bin/activate
```

or 

```
env\Scripts\activate
```



### Install the requirements 

``` 
pip install -r requirements.txt
```

### Create the database
``` python create_db.py ```

## Run the API
``` python main.py ```

## Author 
[Ssali Jonathan](https://github.com/jod35)

