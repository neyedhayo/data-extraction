# import necessary library
import csv

# target-specified columns (in digits position), but
# can also be represented by their actual column names
extraction_column = [11, 14, 15]  

# relative data-path of the read/extraction file
read_file = 'main-data/main-data-report.csv'
extracted_file = 'extracted-data/extracted-data-record-file.csv'

# open and read the file using the imported library
with open(read_file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # open and modify the initial file into a new file
    with open(extracted_file, mode='w', newline='') as new_file:
        csv_writer = csv.writer(new_file)

        # extract each rows of the selected columns
        for row in csv_reader:
            # Extract the selected columns
            selected_columns = [row[i] for i in extraction_column]

            # Write the selected columns to the new CSV file
            csv_writer.writerow(selected_columns)
