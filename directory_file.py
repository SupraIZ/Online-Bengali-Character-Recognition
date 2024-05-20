import glob
import os
import fnmatch
import itertools

fileContent = ""
buckets = []
countlineIndex = 0

current_directory = os.getcwd()
pattern = 'data0*'
mydirectories = os.listdir(current_directory + "/Dataset")
# mylist = fnmatch.filter(os.listdir(current_directory+"/equi distant data/scalled_coordinate/64-point-A"), pattern)
# print(mylist)

for directory in mydirectories:
    # print("directory list >>> "+directory+"\n")
    directoryPath = current_directory + "/Dataset" + directory
    newdirectory_name = directory + "-Strocks"
    isdir = os.path.isdir(directoryPath + "/" + newdirectory_name)
    newdirectory_path = directoryPath + "/" + newdirectory_name
    access_rights = 0o755
    if isdir == False:
        try:
            os.makedirs(newdirectory_path, access_rights)
        except OSError:
            print("Creation of the directory %s failed" % newdirectory_path)
        else:
            print("Successfully created the directory %s" % newdirectory_path)

    # print(isdir)
    myFilelist = fnmatch.filter(os.listdir(directoryPath), pattern)
    for filelist in myFilelist:
        print(filelist)
        buckets = []
        sourcefile = directoryPath + "/" + filelist
        with open(sourcefile, "r") as my_file:
            for line in my_file:
                if line.endswith(" 0\n") and fileContent != "":
                    buckets.append(fileContent)
                    fileContent = ""
                fileContent += line
            if fileContent != "":
                buckets.append(fileContent)
                fileContent = ""
            for bucket in buckets:
                countlineIndex += 1
                # print("bucket>>>"+ str(countlineIndex)+"\n"+ bucket)
                name_of_file = filelist + "-" + str("{:02d}".format(countlineIndex)) + "-strocks"
                completeName = newdirectory_path + "/" + name_of_file + ".txt"
                file1 = open(completeName, "w")
                toFile = bucket
                file1.write(toFile)
                file1.close()
                print("****** Sucessfully data append >>>> %s" % name_of_file + "\n" + bucket)
        countlineIndex = 0
    # if countlineIndex >= 3:
    # print(bucket+" 0\n" if countlineIndex!=len(fields) else bucket)
    # print("********************")

    # It is good practice to close the file at the end to free up resources

    print("*******PROCESS END******")
    # my_file.close()
    # filename = os.listdir("d:/Python/splitdata/Characters/equi distant data/scalled_coordinate/"+directory)

    # print(os.path.join('C:\\Users\\asweigart', filename))
# myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in myFiles:
# print(os.path.join('C:\\Users\\asweigart', filename))
