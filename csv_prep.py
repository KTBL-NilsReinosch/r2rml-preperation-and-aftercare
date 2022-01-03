#### Prep CSV with Python for r2rml Mapping ###
# Todo: 
# Author: Nils Reinosch
# Date:	  2021-12-06
# Version: 0.1
#################

# Read me
# This Programm will prepare an csv for r2ml.
# In order to do so it removes all special characters from the columns that have been selected by the user.
# Also all predicates that are selected from thoses will start with lowerchase letter.
# Also there are some costume replacements in the headers that simply can be put in at costumeReplace and costumeReplacements.


import csv

# Set the variables to there start setting
uriRow = []
uriPred = []
coliumnNumber = ()
coliumnPredicate = ()
procede = 'run'
useHeader = (2)
b = 0 

# Get some informations
# What is the name of the file?
print("Enter the file name without .csv")
fileName = str(input("File Name: "))


# What columns needed to be proceded from the user?
print("Which columns do you want to be URI cleaned? Column number start from left to right with 0.")
print("Type \'" + procede + "\' to procede.")
while coliumnNumber != procede:
    coliumnNumber = input("Column number: ")
    if coliumnNumber != procede:
        uriRow.append(int(coliumnNumber))

print('Secelted Columns:')
print(uriRow)

# Which of the columns are for predicates?
print("Which columns of those are predicates (to make the first letter lowercase)?")
print("Type \'" + procede + "\' to procede.")
while coliumnPredicate != procede:
    coliumnPredicate = input("Column number: ")
    if coliumnPredicate != procede:
        if int(coliumnPredicate) in uriRow:
            uriPred.append(int(coliumnPredicate))
        else:
            print('The column number is not contained in the already selected columns!')

print('Secelted Columns:')
print(uriPred)

# If the costume replacements shoulde be active or not
while ((useHeader != 1) and (useHeader != 0)):
    print("Do you wish to enable the costume replacements (need to be changed in the programm)?")
    useHeader = int(input("1 = yes or 0 = no: "))
print(useHeader)


# Which columns need to be turned into suitable URIs?
#uriRow = [0, 2, 3, 4]
#uriPred = [2, 3]
#useHeader = True


# All general signs that need to be removed from a URI
replaceText = (' ', ',', ':', '/', '?', '#', '[', ']', '@', '!', '$', '%', '&', '\'', '(', ')', '*', '+', ';', '=', '-', '.', '_', '~')
replaceWith = ('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')


# For predicates replacing the first capital letter with lowercase ones
capitalLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ä", "Ö", "Ü" ,"ß"]
lowercaseLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ä", "ö", "ü", "s"]

# Special Charakters in Headers need to be removed
specialCharakters = ["Ä", "Ö", "Ü", "ä", "ö", "ü", "ß"]
specialCharaktersReplacemnet = ["Ae", "Oe", "Üe", "ae", "oe", "ue", "s"]

# For URIs to have CamelCase. Replacing all lowercase letters after a space with a capitalcase letter.
capitalLettersSpace = [" " + x for x in capitalLetters]
lowercaseLettersSpace = [" " + v for v in lowercaseLetters]

# Costume Replacements in Header
costumeReplace = ( 'Datentyp', 'Nutzung', 'GgfsAlternativeGebräuchlichEinheiten', 'Überüberbegriff', 'Überbegriff', 'Einheit', 'BezeichnungDerEigenschaft')
costumeReplacements = ('Dat entyp', 'Nut zung', 'XXX AE', 'XUE UE', 'XXX UE', 'XXX E', 'Bez eichnungDerEigenschaft')




# Opens the csv file with reading permition in UTF-8
with open(fileName +'.csv', 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")


    # Create new file, set the delimiter to ',' and open it as UTF-8
    with open(fileName + '_new.csv', 'w', encoding='utf-8') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')

        # This loop is to select every row of the csv
        for j in csv_reader:          
            new_URI = []
            b = b + 1 # Only used to find the first row in the csv
            # This loop is to select ever column of the already selected row
            for i in uriRow:
                r = j[i]

                # Making the URIs CamelCase
                for e in range(len(lowercaseLettersSpace)):
                    r = r.replace(lowercaseLettersSpace[e], capitalLettersSpace[e])

                # Removes all the text pieces you do not want in a URI
                for c in range(len(replaceText)):
                    r = r.replace(replaceText[c], replaceWith[c])

                # Get the costume replacements done if Header was set to 1
                if ((b == 1) and (useHeader == 1)):
                    for a in range(len(costumeReplace)):
                        r = r.replace(costumeReplace[a], costumeReplacements[a])

                # If the column is ment to be a predicate the first letter will be replaced with a lowercase letter of itself
                if ((i in uriPred) and (r)):
                        for y in range(len(capitalLetters)):
                            if r[0] == capitalLetters[y]:
                                r = r.replace(r[0], lowercaseLetters[y], 1)

                # Add r to the list of new URIs that will be added as new columns    
                new_URI.append(r)


            # Write everything of the old file in the new file and add the changed columns as new columns
            csv_writer.writerow(j + new_URI)

           
print("The output was put in the new file \"" + fileName + "_new.csv\"")            
z = str(input("Press enter to close."))

