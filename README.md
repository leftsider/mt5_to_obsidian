# mt5_to_obsidian
just something quick and dirty to port an old blog (Movable Type 5) to a new platform. It splits the single MT5 export .txt file into N markdown files, where N is the number of MT posts are in the export.

to use this script:
* create directories "output" and "source_files" relative to the script
* edit line 16 to the name of your export file
* run the script

What you'll get:
1. a basically empty .md file whose name is the timestamp of when the script was run
2. a number .md files with names in zero-based order. 


If you want to have a different filetype or modify the output filename, you can edit line 26.

