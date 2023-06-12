
import time 
import os
import mmap




# create file using timestamp to name file 
timestamp = time.strftime("%Y%m%d-%H%M%S")
timestamp_filename = "output/newfile" + timestamp + ".md"
new_doc = open(timestamp_filename, "w+")
new_doc.write('just a file whose filename tells you when the other files in this folder were created')
new_doc.close()

with open('source_files/leftsider.txt', 'r') as f:
   # memory-map the file
   mmapped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

   # split the file by specific delimiter, in this case newline characters
   delimiter = "--------\n"
   lines = mmapped_file.read().split(delimiter.encode())

# create new md files for split items   
   for i, line in enumerate(lines):
	   with open(f"output/{i}.md", "w") as f:
		   f.write(line.decode())   
   print(f"Created {len(lines)} new files.")



