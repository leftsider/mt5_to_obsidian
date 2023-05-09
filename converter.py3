
import time 



# create file using timestamp to name file 
# (https://stackoverflow.com/questions/10607688/how-to-create-a-file-name-with-the-current-date-time-in-python)
timestamp = time.strftime("%Y%m%d-%H%M%S")
timestamp_filename = "output/newfile" + timestamp + ".md"
newdoc = open(timestamp_filename, "w+")
newdoc.write('hello world')
newdoc.close()

