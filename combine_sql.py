from datetime import datetime
import argparse
import os
import sys

# Initialize the content of the output .sql file
output_sql_content = ""

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Combine SQL files into a single .sql file")
parser.add_argument("--model_type", nargs=1, help="Core or config")
parser.add_argument("--rfilepath", nargs=1, help="File path to read from", required=True)
parser.add_argument("--wfilepath", nargs=1, help="File path to write to")
parser.add_argument("--input_files", nargs='+', help="List of input .sql files", required=True)

args = parser.parse_args()

# Validate model type
model_type_lowerc = args.model_type[0].lower()

if model_type_lowerc != 'core' and model_type_lowerc != 'config':
    print("Invalid model type - model type argument can only be 'core' or 'config'")
    sys.exit(1)

# Validate read file path
rfilepath_slash_transformed = args.rfilepath[0].replace("\\", "/")

if not os.path.exists(rfilepath_slash_transformed):
    print(f"Error - The specified read file path does not exist: {args.rfilepath}")
    sys.exit(1)

# Validate write file path

wfilepath_slash_transformed = args.wfilepath[0].replace("\\", "/")

if not os.path.exists(wfilepath_slash_transformed):
    print(f"Error - The specified write file path does not exist: {args.wfilepath}")
    sys.exit(1)



# Specify the file path where the input files should exist

for filename in args.input_files:
    # Check if the file exists in the specified file path
    rfile_full_path = os.path.join(rfilepath_slash_transformed, filename)


    if not os.path.exists(rfile_full_path):
        print(f"Error - Could not find {filename} in {rfilepath_slash_transformed}")
    else:
        with open(rfile_full_path, "r") as sql_file:
            output_sql_content += '--' + filename + '\n' + sql_file.read()  + '\n\n'


# Get the current date and time
current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")

# Define the output file name with the current date and time
if args.model_type != '':
    output_filename = f"combined_sql_{current_datetime}_{args.model_type[0]}.sql"
else:
    output_filename = f"combined_sql_{current_datetime}.sql"

wfile_full_path = os.path.join(wfilepath_slash_transformed, output_filename)


# Write the combined content to the output .sql file 
try:
    with open(wfile_full_path, "w") as output_sql_file:
        output_sql_file.write(output_sql_content)
    print(f"Combined SQL files into {output_filename}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
