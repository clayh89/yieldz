"""
this program calculates and stores expected yields of various processes 
(harvest weight, trim weight, dry weight, hash, rosin)
including various grades etc
versus inputs (watts, nutrients, etc)
to generate expected yields for a known clone in a known space 

storage of past runs, predictions, etc via local text file and nothing else. no clouds. 

by Henry Clay @clayh89 on github
"""
import sys
import json
import sqlite3
"""
saves data to a text file
takes filename (provided by calling function) and JSON-ready data array 
"""

def txt_save(target_name, run_data):
    f = open(target_name, "w")
    f.write(json.dumps(run_data))
    f.close()
    # again could do sanitization here, do values from run_data individually

    return

"""
loads data from a text file
takes filename (provided by user probbably?), returns data array
"""

def txt_load(target_name):
    # opens and reads json from file into python object 
    f = open(target_name, "r")
    target_data = json.loads(f.read()) 
    # could do input stuff here like read from the JSON to the return array 

    # closes file for nice filesystem stuff
    f.close()


    return target_data

"""
fills a dict w/ the info the thing needs

per run things: 
veg time
flower time
strain
watts
harvest weight
trim weight wet
trim weight dry
waste weight 
prewash
a buds
b buds
c buds

hash: input
- 1st pull
- 2nd pull 
- b grade
- food grade
- total 

rosin: input
- 1st press
- 90-120 
- b grade
- full spec 
- food grade
- total

per plant things:
tag#
harvest weight


so this is what the below will need to do. I think I need to do it in steps. 
like, poll @ harvest, @ trim, @ hash 
csv-compatible is the goal 

"""
def collect_data(data_holder):
    run_data = {
        'strain': "",
        'watts': 1,
        'plants': 1


    }

    return

"""
error and help message handlers - for bad program input
"""

def help_msg():
    msg = """
    Yieldz Help  
    
    Yieldz calculates flower, hash, and rosin runs by processing data stored by the user. 

    To generate data, use the -i or -input option. This will begin polling. 
    Using -if, -ih, or -ir will instead select Flower, Hash, or Rosin polling, respectively
    (useful for repeatable workflows, cli, and csv applications)

    -i -f will allow you to specify an output path

    To process data, use the -o or -output option. This will generate reports based on the options you select at runtime. This is the default mode 

    -o -f will allow you to specify a path to process 

    """
    return msg

def error_msg():
    msg = """
    Options are 
    yieldz | -i(nput) -if -ih -if -o(utput) -of -oh -or | -f | -fg | -fs  
    
    """
    return msg

"""
calculates based on read or supplied info
"""

def calculate(data_holder):
    return

def main(option = "g", filename = "default"): 
    print("welcome to yieldz")
    if option == "input":
        return
    elif option == "output":
        return
    elif option == "help":
        print(help_msg())
        return 
    else:
        print(error_msg())
        return


"""
options: 
- generate run, will poll parameters and record, display results, can supply filename
- recall run, will display results of target
- compare runs, will sort multiple runs given restrictions 
- clone success rates??? idk 

- so thats a mode and a target 
- optional filename, required filename, folder? or wildcard or maybe matching name search - would be cool
"""
if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv [1])
    else:
        main()
