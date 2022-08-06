"""
Holds equations for yieldz

by Henry Clay @clayh89 on github
"""


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

from tracemalloc import start

# ??? ^^^
import json
import sqlite3

# so we need the concept of varieties 

# takes a list of strains, runs compare functions on them 
def hash_compare(strains):
    val = {}
    for strain in strains:
        val[strain] = hash_yield_per_plant(strain)

    return val


# heavily prototyped, this needs refinement.  but this should tell me what else I need to build 
def hash_yield_per_plant(strain):
    # looks up historical data 
    # open datafile folder
    # holder 
    val = {}
    # name of hypothetical data storage 
    datafile = open('./archive')
    # for each saved file, if the name includes the strain, dump into json variable and pull date and yield per plant
    for file in datafile:
        # this should be grep or regex or something
        if file.name() == strain:
            f = file.open(file)
            data = json.dumps(f)
            date = data['date']
            yhash = data['hash_yield']
            val[date] = yhash
            f.close()

    hashy, count = 0

    for entry in val:
        hashy += val[entry]
        count += 1

    avg = (hashy / count)

    return avg

def gpwatt(grams, watts):
    ratio = grams / watts
    return ratio

def total_bud_weight(i1, i2, i3, i4, i5):
    return 

def gpweek(grams, veg_time, flower_time):
    total = veg_time + flower_time
    ratio = grams / total 
    return ratio 

def trim_total(w, d):
    return (w + d)

def bud_total(a,b,c):
    return a + c + c

def shrinkage_dry(harvest, waste, trim, buda, budb, budc):
    dry = bud_total(buda, budb, budc)
    total = harvest
    total -= trim
    total -= waste
    total -= dry 
    return total

def shrinkage_wet(harvest, waste, trim, pre):
    total = harvest
    total -= trim
    total -= waste
    total -= pre 
    return total 

# not sure I like this VVV
# just a very fast 2 bag run? idk 
# obsolete just passing a baglist w/ that one

def run_hash_quick(starting, u1, u2, fg=False, fs=False):
    fg1 = 0
    fs1 = 0
    first_pull =  int(input("1st pull yield?"))
    micron =  int(input("{u1}-{u2} yield?"))
    
    if (fg == True):
        fg1 =  int(input("Food grade yield?"))
    
    if(fs == True):
        fs1 =  int(input("Full spec yield?"))

    other =  int(input("other?"))

    total = fg1 + fs1 + first_pull + micron + other
    ypercent = total / starting

    return [first_pull, micron, fg1, fs1, other, total, ypercent]

# do this w/ arrays for custom bag sizes

#polls the user and stores values in a dict it returns for a hash run of all bags w/ extras. 
# gives yield percent for starting material (and a detailed breakdown of what)
# food grade and full spec should not be double counted, so if this is just a how much of 
# everything by micron, skip it. but if its a usable by micron plus other stuff, this will capture it

def run_hash_full(starting, fs = False, fg = False): 
    
    val = {
        'food_grade' : 0,
        'full_spec' : 0,
        'first_pull': 0,
        '220u' : 0,
        '190u' : 0,
        '160u' : 0,
        '120u' : 0,
        '110u' : 0,
        '90u' : 0,
        '73u' : 0,
        '40u' : 0,
        '25u' : 0,
        'other' :0,
        'total' : 0,
        'ypercent' : 0,
        'input' : starting
    }
    
    val['first_pull'] = int(input("1st pull yield?"))
    val['220u'] = int(input("220"))
    val['190u'] = int(input("190"))
    val['160u'] = int(input("160"))
    val['120u'] = int(input("120"))
    val['90u'] = int(input("90"))
    val['73u'] = int(input("73"))
    val['40u'] = int(input("40"))
    val['25u'] = int(input("25"))
  
    if (fg == True):
        val['food_grade'] =  int(input("Food grade yield?"))
    
    if(fs == True):
        val['full_spec'] =  int(input("Full spec yield?"))

    val['other'] =  int(input("other?"))

    val['total'] = val['food_grade'] + val['full_spec'] + val['first_pull'] + val['220u'] + val['190u'] + val['160u'] + val['120u'] + val['90u'] + val['73u'] + val['40u'] + val['25u'] + val['other']
    val['ypercent'] = val['total'] / val['starting']
    
    return val
    
def run_hash_baglist(starting, baglist):

    val = {
        'food_grade' : 0,
        'full_spec' : 0,
        'first_pull': 0,
        'other' :0,
        'total' : 0,
        'ypercent' : 0,
        'total_bags' : 0,
        'input' : starting,
        'bag_avg' : 0,
        'ypercent' : 0
    }

    for bag in baglist:
        pull = int(input("{bag}?"))
        val[bag] = pull
        val['total_bags'] +=1
        val['total_yield'] += pull

    val['bag_avg'] = val['total_yield'] / val['total_bags']
    
    val['ypercent'] = val['total_yield'] / starting

    return val


def run_compare(run1, run2):
    ratio = 0
    if run1 > run2: 
        ratio = run2 / run1
        print(ratio, " loss vs prev")
        return [ratio, run1]

    if run1 < run2: 
        ratio = run1 / run2
        print(ratio, " gain vs prev")
        return [ratio, run2]

# this is gonna use a sorting algorithm to sort via 
# the run_compare function above. because it's bubble
# hash, I'm going to use the bubblesort algorithm. 
# there are theoretically better performing ones, 
# but I really don't care at this time (7/22) 
# because... bubble hash. bubble sort. come on.

def bag_sort(bags):
    runs = {}
    for i in range(len(bags)):
        for j in range(0, len(bags) - i - 1):

              if bags[j] > bags[j+1]:
            
                # swapping elements if elements
                # are not in the intended order
                temp = bags[j]
                bags[j] = bags[j+1]
                bags[j+1] = temp



def run_rosin(input, fg=False, fs=False):

    val = {
        'food_grade' : 0,
        'full_spec' : 0, 
        'first_pull' : 0,
        'other' : 0,
        'range': ""
    }

    val['range'] = input("micron range?")

    val['first_pull'] = input("1st pull yield?")

    int(val['first_pull'])

    if (fg == True):
        val['food_grade']= input("Food grade yield?")
        int(val['food_grade'])
    if(fs == True):
        val['full_spec'] = input("Full spec yield?")
        int(val['full_spec'])


    val['other'] = int(input('other yield?'))

    return val 

#noticing a pattern here - this should help fill in the variables I use in each run poll function
# helper that takes an array/list of strings to make a dict 
def val_helper(values):
    val = {

    }
    for item in values:
        val[item] = 0
    
    return val
