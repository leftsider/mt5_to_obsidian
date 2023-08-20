# mt5_to_obsidian
just something quick and dirty to port an old blog (Movable Type 5) to a new platform. A few tools here:
1. converter
2. renamer
3. arranger

### converter
It splits the single MT5 export .txt file into N markdown files, where N is the number of MT posts are in the export.

to use this script:
* create directories "output" and "source_files" relative to the script
* edit line 16 to the name of your export file
* run the script

What you'll get:
1. a basically empty .md file whose name is the timestamp of when the script was run
2. a number .md files with names in zero-based order. 


If you want to have a different filetype or modify the output filename, you can edit line 26.


### renamer
It checks if the directory exists, iterates over all the files in the directory. And renames them based on the BASENAME included in a MT5 blog post's metadata.

This script first checks if the directory exists. If it does not exist, the script prints an error message and exits. It also checks only for .md files, so if you have other file types they will be skipped. If the basename is not found in an .md file, the script prints an error message and continues to the next file. Just to be safe, if the basename already exists in the directory, the script creates a new name by appending a consecutive number to the basename. It will keep doing this until it finds a value that doesn't already exist. Then it renames the file to the new name.

to use this script:
* place the path to the directory where your files are located in line 6 and line 38. I placed it in the same folder and used "../directory/" but it should work from anywhere
* check the number of characters in row 20. My row started with "BASENAME: " so I set line[] to 10. Your mileage may vary.
* run the script

What you'll get:
1. error reporting for any .md files that don't get renamed.
2. a directory with renamed md files

If you want to have a different filetype, you can edit line 27.