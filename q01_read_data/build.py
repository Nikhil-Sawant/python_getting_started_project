# %load q01_read_data/build.py
import yaml

def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    info = open('data/ipl_match.yaml')
    data = yaml.load(info)
    return data

read_data()

