
import time 
import os




# create file using timestamp to name file 
timestamp = time.strftime("%Y%m%d-%H%M%S")
timestamp_filename = "output/newfile" + timestamp + ".md"
new_doc = open(timestamp_filename, "w+")
new_doc.write('hello world')
new_doc.close()

read_doc = open("source_files/sampletxt.txt", "r")
copy = read_doc.read()

new_doc = open(timestamp_filename, "a")
new_doc.write(copy)
new_doc.close()

read_doc.close

