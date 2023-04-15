
# Section 1: Task 2

### Parsing a Complex JSON File


• "ubo1.json" file is a complex JSON file having multiple nesting.

• "Nested_JSON_File_to_DF_and_Parquet.ipynb" is the notebook having the workings. PySpark is used for efficiently reading the JSON file.

• A dataframe is created to store nested JSON content in tabular format. Both ArrayType and StructType are used to explode and flatten columns respectively. 

• The dataframe was printed to check its tabular format. 

• The dataframe was converted to parquet format to store all the columns and the schema was printed to check if all the fields are incorporated in different nested levels of the original JSON file.

• "Full Nested Table Fomat.pdf" gives a fully parsed view of the tabular format. This is to cross check the results derived from code.
