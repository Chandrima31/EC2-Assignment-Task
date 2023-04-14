
# Section 1: Task 1

### Creating an API Endpoint


• The "main.py" file has the reference of creating FastAPI app (object)

• uvicorn main:app --reload was run from the command prompt to run the live server

• The "import_data.py" file has the steps to import "titanic.csv" data using SQLite. The database created has the name "demo.db" and the table created was named as "titanic_data". A snapshot view from SQLite Viewer is pasted for reference. 

• Initially, the "import_data.py" file is run. Then, from API endpoint ‘http:/localhost:8000/titanic’ the "main.py" file was run. 

• Three snapshots from FastAPI swagger are pasted for reference. When passengerId = 43 was passed as input, the output correctly displayed the record of "Name": "Kraeff, Mr. Theodor".
