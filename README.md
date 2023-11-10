# SQL-File-Aggregator

# What does it do? 

SQL File Aggregator is a command line program in Python which collates the SQL contained in multiple `.sql` files into a single `.sql` file.

# Arguments List

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
  


