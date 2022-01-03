# r2rml-preperation-and-aftercare

The two Python programs are used to prepare and post-process a csv or ttl file.

The data can be stored in an Excel file and then converted to a csv UTF-8 file. After that, some preparations in the csv are useful:

- setting the delimiter to "," 
- create a new file as a copy of the old file with additional new columns that are copys of specific old ones with changes:
        > URIs that are free of special characters and in camelCase starting with upper case for classes and lower case for properties
        > replace Ä, Ö, Ü, ß, etc. with Ae, Oe, Ue, s, etc.
        > replacedments in the header
        

For after care the other programm makes sure UFT-8 is applyed.
