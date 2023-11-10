# SQL File Aggregator

## What does it do? 

SQL File Aggregator is a command line program in Python which collates the SQL contained in multiple `.sql` files into a single `.sql` file.

## How to use 

1) Clone down project
2) Open terminal
3) Navigate to same path as project
4) To run program, type `py combine_sql.py` followed by your arguments

## Arguments List

### Model type (optional)

*   `--model_type`
*   Values accepted: 'Core' or 'Config'
*   When provided, the output `.sql` file will end with the word 'Core' or 'Config'
*   This is to clarify whether the file should be executed on core or config models

### Read File path (required) 

*  `--rfilepath` 
*   File path containing the `.sql` files to read
*   Requires double or single quotes around the file path

### Write File path (optional)

*   `--wfilepath` 
*   File path where the output file containing the aggregated SQL will be created
*   Requires double or single quotes around the file path
*   If no write file path is provided, the real file path is the location used for the output file

### Input Files (required) 

*   `--input_files`
*   List of `.sql` files to read from within the specified read file path
  
# Examples

## Example 1 - All arguments specified

![example sql automation](https://github.com/gabrielrowan/SQL-File-Aggregator/assets/86267314/612f2493-8844-46c0-81c2-7fe6d313aa61)

* Reads the contents of the `sql1.sql` and `sql2.sql` from `C:\Users\GabrielRowan\OneDrive\Programming\SQLInput`
* Create an output `.sql` file containing the condensed SQL in `C:\Users\GabrielRowan\OneDrive\Programming\SQLOutput`
* The output file will follow the naming format `combined_sql_{current_datetime}_core.sql`

## Example 2 - Only required arguments specified

![required_args_only](https://github.com/gabrielrowan/SQL-File-Aggregator/assets/86267314/d4dd4c1c-d9c6-4ffa-976b-5512e9672b8e)

* Reads the contents of `sql5.sql` and `sql9.sql` from `C:\Users\GabrielRowan\OneDrive\Programming\SQLInput`
* Creates an output `.sql` file containing the condensed SQL in `C:\Users\GabrielRowan\OneDrive\Programming\SQLInput`
* The output file will follow the naming format `combined_sql_{current_datetime}.sql`


