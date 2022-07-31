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

