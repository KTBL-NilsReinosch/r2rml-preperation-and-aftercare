#### Prep CSV for r2rml Mapping with Python ###
# Todo: 
# Author: Nils Reinosch
# Date:	  2021-11-17
# Version: 0.1
# Purpose: to clean an ontologie from dirty sintax.
# Check csv_prep.py for bevore the mapping
#################



# Information and input from user
print("To clean the ontologie from problems with UTF-8 (like \"ï¿½\" insted of \"ü\") the file name without .ttl")
fileName = str(input("File Name: "))

# Open the file
text = open(fileName +'.ttl', 'r', encoding='utf-8')

# Join everything in the file to one string
text = ''.join([i for i in text])



# What you want to have replaced (make your changes here)
textReplace = ()
# with the replacements
replacements = ()

# The loop to replace everyhting in the file by the informations of the vectors above
for i in range(len(textReplace)):
    text = text.replace(textReplace[i], replacements[i])



# Create new file
x = open(fileName +'_aftercared.ttl', 'w')

# Neues Datei beschreiben
x.writelines(text)
x.close()



# Information for the user
print("Several text pieces have been replaced:")
print("")
for i in range(len(textReplace)):
    print("\"" + textReplace[i] + "\" with \"" + replacements[i] + "\"")
print("")
print("They have been saved in the new file " + fileName + "_aftercared.ttl")
print("")

z = str(input("Press enter to close."))

