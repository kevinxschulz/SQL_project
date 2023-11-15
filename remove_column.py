# removing column to have equal csv's

def remove_column(input_file, output_file, column_to_remove):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            values = line.strip().split('|')
            values.pop(column_to_remove)
            outfile.write('|'.join(values) + '\n')


# removing the column numero_tpv from data1.csv and data3.csv because 
# data2.csv does not contain this column. data was shifted into wrong columns

input_file_data1 = 'data1.csv'
output_file_data1 = 'data1_no_numero_tpv.csv'
column_to_remove_data1 = 1 


input_file_data3 = 'data3.csv'
output_file_data3 = 'data3_no_numero_tpv.csv'
column_to_remove_data3 = 1 

# remove column from data1.csv
remove_column(input_file_data1, output_file_data1, column_to_remove_data1)

# remove column from data3.csv
remove_column(input_file_data3, output_file_data3, column_to_remove_data3)
