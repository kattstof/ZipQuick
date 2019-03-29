#! python3
# zipquick - Simple and quick zipfile maker/extracter 
import shutil
from zipfile import ZipFile, ZIP_DEFLATED
print("ZipQuick")
print("[1] Unzipper")
print("[2] Create Zip")
menu = input()
if menu == '1':
    file_name = input("input file to unzip:")
    with ZipFile(file_name, 'r') as zip:
        zip.printdir()
        directory = input("Input folder/directory to extract to:")
        print("Extracting all files now....")
        zip.extractall(directory)
        print("Done!")
elif menu == '2':
    print("[1] Create zip from file")
    print("[2] Create zip from Folder")
    zip_choice = input("Enter Choice")
    if zip_choice == '1':
        file_name = input("Enter file to compress:")
        name_zip = input("Enter desired name of archive:")
        zf = ZipFile(name_zip, mode='w')
        ZipFile.write(zf, file_name)
    elif zip_choice == '2':
        dir_name = input("Enter directory name that you want to zip")
        out_name = input("Enter desired output file name")
        shutil.make_archive(out_name, 'zip', dir_name)
    
