# SQL File Aggregator

## What does it do? :spiral_notepad: :spiral_notepad: :spiral_notepad: :arrow_right: :spiral_notepad:

SQL File Aggregator is a command line program in Python which collates the SQL contained in multiple `.sql` files into a single `.sql` file.

## Prerequisites 

You will need Python installed on your machine

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
*   You can use `.` to select all `.sql` files from the read file path
  
# Examples

## Example 1 - All arguments specified

![all params](https://github.com/gabrielrowan/SQL-File-Aggregator/assets/86267314/7c5f8af1-f2e7-49b8-a418-69b73d3a675c)

* Reads the contents of the `sql1.sql` and `sql2.sql` from `C:\Users\GabrielRowan\OneDrive\Programming\SQLInput`
* Create an output `.sql` file containing the condensed SQL in `C:\Users\GabrielRowan\OneDrive\Programming\SQLOutput`
* The output file will follow the naming format `combined_sql_{current_datetime}_core.sql`

## Example 2 - Only required arguments specified

![optional params](https://github.com/gabrielrowan/SQL-File-Aggregator/assets/86267314/467dcbd4-3a28-4ded-a398-b0b82412fcb3)

* Reads the contents of `sql5.sql` and `sql9.sql` from `C:\Users\GabrielRowan\OneDrive\Programming\SQLInput`
* Creates an output `.sql` file containing the condensed SQL in `C:\Users\GabrielRowan\OneDrive\Programming\SQLInput`
* The output file will follow the naming format `combined_sql_{current_datetime}.sql`

## Example 3 - Read all `.sql` files 

![all files](https://github.com/gabrielrowan/SQL-File-Aggregator/assets/86267314/f8199986-a82b-4462-a372-6d8fc5f62a83)

* Reads all `.sql` files from read file path `C:\Users\GabrielRowan\OneDrive\Programming\SQLInput`
* Creates an output `.sql` file containing the condensed SQL in `C:\Users\GabrielRowan\OneDrive\Programming\SQLInput`
* The output file will follow the naming format `combined_sql_{current_datetime}.sql`




