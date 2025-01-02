import pandas as pd
import os

# Define output directory
output_directory = 'output'

# Check if the directory exists, if not, create it
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

file_name1 = './data/hammer-4-product.csv'
file_name2 = './data/hammer-4-raw.csv'