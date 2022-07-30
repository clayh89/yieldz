"""
this program calculates and stores expected yields of various processes 
(harvest weight, trim weight, dry weight, hash, rosin)
including various grades etc
versus inputs (watts, nutrients, etc)
to generate expected yields for a known clone in a known space 

storage of past runs, predictions, etc via local text file and nothing else. no clouds. 
"""
import sys
import json

"""
loads data from a text file
"""

def txt_save(target_name):
    return

"""
loads data from a text file
"""

def txt_load(targert_name):
    return

"""
fills a dict w/ the info the thing needs
"""
def collect_data(data_holder):
    return

"""
calculates based on read or supplied info
"""

def calculate(data_holder):
    return

def main(option = "g", filename = "default"): 
    print("welcome to yieldz")
    if option == "recall":
        return
    elif option == "compare":
        return
    elif option == "generate":
        return
    else:
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
