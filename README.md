# SQL-File-Aggregator

## What does it do? 

SQL File Aggregator is a command line program in Python which collates the SQL contained in multiple `.sql` files into a single `.sql` file.

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

### Write File path (required)

*   `--wfilepath` 
*   File path where the output file containing the aggregated SQL will be created
*   Requires double or single quotes around the file path

### Input Files (required) 

*   `--input_files`
*   List of `.sql` files to read from within the specified read file path
  
## Example

![example-running-program-with-arguments](https://github.com/gabrielrowan/SQL-File-Aggregator/assets/86267314/8794673c-2cba-45ed-a749-9b17e66982be)

* This reads the contents of the `sql1.sql` and `sql2.sql` files within the read file path `C:\Users\GabrielRowan\OneDrive\Programming\SQLInput`
* It will create an output `.sql` file containing the condensed SQL to the write file path `C:\Users\GabrielRowan\OneDrive\Programming\SQLOutput`
* The output file will be called `combined_sql_{current_datetime}_core.sql`

### Sample output file 

![sql example output](https://github.com/gabrielrowan/SQL-File-Aggregator/assets/86267314/7b0aeefc-6b8d-48bb-90e7-51b965a04f6c)



