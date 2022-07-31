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

def run_hash_quick(starting, u1, u2, fg=False, fs=False):
    fg1 = 0
    fs1 = 0
    first_pull = input("1st pull yield?")
    micron = input("{u1}-{u2} yield?")
    
    if (fg == True):
        fg1 = input("Food grade yield?")
    
    if(fs == True):
        fs1 = input("Full spec yield?")

    other = input("other?")

    total = fg1 + fs1 + first_pull + micron + other
    ypercent = total / starting

    return [first_pull, micron, fg1, fs1, other, total, ypercent]

# do this w/ arrays for custom bag sizes

def run_hash_full(input): 
    fg1 = 0
    fs1 = 0
    first_pull = input("1st pull yield?")
    u220 = input("220")
    u190 = input("190")
    u160 = input("160")
    u120 = input("120")
    u90 = input("90")
    u73 = input("73")
    u40 = input("40")
    u25 = input("25")
    
    if (fg == True):
        fg1 = input("Food grade yield?")
    
    if(fs == True):
        fs1 = input("Full spec yield?")

    other = input("other?")

    total = fg1 + fs1 + first_pull + u220 + u190 + u160 + u120 + u90 + u73 + u40 + u25 + other
    ypercent = total / starting
    
    return [first_pull, fg1, fs1, u220, u190, u160, u120, u90, u73, u40, u25, other, total, ypercent]
    
def run_hash_baglist(starting, baglist):
    bag_holder = { bag : 0 for bag in baglist }
    total_bags = 0
    total_yield = 0

    for bag, n in baglist:
        pull = input("{bag} yield")
        bag_holder(bag = pull)
        total_bags = n
        total_yield += pull

    bag_avg = total_yield / total_bags
    
    
    return [bag_holder, bag_avg, total_yield, total_bags]

def run_compare(run1, run2):
    ratio = 0
    if run1 > run2: 
        ratio = run2 / run1
        print(ratio, " loss vs run 1")

    if run1 < run2: 
        ratio = run1 / run2
        print(ratio, " gain vs run 1")
        
    return

def run_rosin(input, u1, u2, fg=False, fs=False):
    fg1 = 0
    fs1 = 0
    first_pull = input("1st pull yield?")
    micron = input("{u1}-{u2} yield?")
    
    if (fg == True):
        fg1 = input("Food grade yield?")
    
    if(fs == True):
        fs1 = input("Full spec yield?")

    other = input("other?")

    return [first_pull, micron, fg1, fs1, other]




