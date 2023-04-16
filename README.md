
# Section 1: Task 1

### Creating an API Endpoint


• The "main.py" file has the reference of creating FastAPI app (object)

• uvicorn main:app --reload was run from the command prompt to run the live server

• The "import_data.py" file has the steps to import "titanic.csv" data using SQLite. The database created has the name "demo.db" and the table created was named as "titanic_data". A snapshot view from SQLite Viewer is pasted for reference. 

• Initially, the "import_data.py" file is run. Then, from API endpoint ‘http:/localhost:8000/titanic’ the "main.py" file was run. 

• Three snapshots from FastAPI swagger are pasted for reference. When passengerId = 43 was passed as input, the output correctly displayed the record of "Name": "Kraeff, Mr. Theodor".

• There are three more component files "database.py", "models.py", "schemas.py". In "database.py" file, SQLAlchemy is used. It provides an object relational mapper (ORM) which maps our database demo.db (and table titanic_data) to Python objects, so that we can more easily and natively interact with them. In this exercise, SQLAlchemy is used with SQLite. The declarative_base() base class contains a MetaData object where newly defined Table objects are collected.

• In "models.py" file, we import the Baseclass, defined in the database.py file above, into the models.py file below to use declarative_base(). This file creates the model for the table "titanic_data" in our database.

• In "schemas.py" file, we write our schema for Pydantic. When we define objects in Pydantic, it is inherited from the BaseModel. Pydantic guarantees that the data fields of the resultant model conform to the field types we defined, using standard Python data types, for the model.
