# importing zipfile module
from zipfile import ZipFile

# specifying the zip file name
file_name = "image.zip"

# opening the zip file in READ mode
with ZipFile(file_name, mode='r') as zip_file:
    # printing all the contents of the zip file
    zip_file.printdir()

    # extracting all the files
    print("Extracting files now..")
    zip_file.extractall()
    print("Done!!")
 
