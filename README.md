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

Starting db container
```
docker run -d --name my_postgres \
 -v $SRC_DB_DATA:/var/lib/postgresql/data -p 5432:5432 \
 -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
 -e POSTGRES_USER=$POSTGRES_USER \
 -e POSTGRES_DB=$POSTGRES_DB \
 postgres:14
```

### Installing Minio
Adding environment variables
```
SRC_MINIO_DATA=~/minio_data
MINIO_BUCKET=bucket
```

Starting minio container
```
docker run --name my_minio -d -v $SRC_MINIO_DATA:/data \
  -p 9000:9000 \
  -p 9001:9001 \
  minio/minio server /data --console-address ":9001"
```

## Installing minio-client for creating bucket
OS X:
```
wget https://dl.minio.io/client/mc/release/darwin-amd64/mc
```

Linux:
```
wget https://dl.minio.io/client/mc/release/linux-amd64/mc
```

Making executable and rename it 
```
chmod +x mc && mv mc minio-client
```

Creating bucket
```
minio-client alias set minio http://localhost:9000 minioadmin minioadmin
minio-client mb minio/$MINIO_BUCKET
``` 

## Migration db schema using Alembic

Creating new schema version
```
 alembic revision --autogenerate -m "added table items"
```

Starting migrations
```
alembic upgrade head
```

## Starting application

Building
```
docker build -t back_end .
```

Running
```
docker run -p 8080:8080 -it back_end
```

#### Swagger available to http://0.0.0.0:8080/docs

## Author 
[Artem Solovev](https://github.com/sav116)

