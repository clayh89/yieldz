# yieldz
a calculator utility for expected agricultural yields given known crops and known inputs

This calculator lets you get some metrics on your hemp/cannabis (or other) harvest. it is designed for all users, but particular focus is paid towards METRC compliance (for licensed facilities) and medical home-growers. 

The idea is to give the user/grower tools to make educated decisions about yields when growing for processing, i.e. hash, tincture, and other medicine where the traditional g/W equation breaks down.

A goal of the project is to keep all files in control of the user, allowing a self-admined SAAS / cloud app with local control over individual data. 

Yieldz functions in terms of workflows: processes that have quantatitive data for inputs and outputs. 
Yieldz can create datasets from user polling, and/or calculate expected results from saved data 
The workflows that are (or will be - ***) supported are: 

Dry Flower Yield per X ***
Dry Flower Yield per strain in same space ***
Hash material yield ***
Hash yield for x material ***
Rosin yield for x hash ***
Rosin yield for x flower ***
Metrc harvest compliance (so harvest weight, moisture shrinkage, trim weight, a/b weight, any other) *** 

Start by creating space (flower room, dry room, wash room, press room) - this is environmental details, temperature, indoor/outdoor, lights (or sun), coldroom temp, press, etc 
Then strain - have historic data (relational db? thinking sqlite)

Dry Flower per space per strain per space = find per plant from past yields, average. mult

Hash material per strain (per space?) given historic data = find hash runs that fit and avg

And so on for rosin material from that 

So there are two parts: data collection/genertion and data processing. 

These will likely be accessed at different times or by different gardeners: generation during / just after workflow, processing during the planning stages. 

