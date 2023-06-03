# worknotes
_just scrap paper where I track my progress and thoughts. Half journal of effort; half talking to the duck._


## 2023 06 03
1. ~~script that makes markdown file~~
2. ~~script that makes markdown file with text~~
3. ~~script that makes markdown file with text from a source~~ 
4. script that makes markdown file with a portion of text from a source
5. script that makes markdown file for each portion of text from a source

Not sure where to start here. I'm guessing use regex to define the beginning and and of a post, but maybe instead of copying the excerpt instead I should copy the whole file as a series of excerpts in an array? If the latter, I wouldn't have to figure out how to ensure the script keeps its place when copying and creating files.

[This link](https://www.pythonforbeginners.com/files/the-fastest-way-to-split-a-text-file-using-python) makes me think the latter is the best move. The only thing is that the example seems to make divisions based on the number of lines? As I have blog posts, I'm assuming that I'll have multiple lines because of multiple paragraphs. So that won't work. 

The only parameter I have to separate posts is that every post segment starts with AUTHOR and ends with eight hyphens ("--------"). So I may need to do more than just copy code here to get this to work. [Most answers](https://stackoverflow.com/questions/16289859/splitting-large-text-file-into-smaller-text-files-by-line-numbers-using-python
) seem based on number of lines.

Oh wait, [here we go maybe](https://www.tutorialspoint.com/what-s-the-fastest-way-to-split-a-text-file-using-python#): At the bottom it talks about importing an `mmap` module that memory maps the entire file (without actually putting it in memory) and then allows you to specify delimiter for the `.split` function. It then can save each segment in a list. It doesn't tell you how to create new files for each item in the list tho. Still gonna give it a shot.

...sooooooo I cheated. I asked google bard to write python that took items from a list and created markdown files for each of them. This is what it gave me:

```
lines = ["This is line 1", "This is line 2", "This is line 3"]

for i, line in enumerate(lines):
	with open(f"{i}.md", "w") as f:
		f.write(line)

print(f"Created {len(lines)} new files.")
```

Game over, yall. The future is here. Now any schmuck who knows enough to copy paste code can also have code written that's legible enough to copy paste. LOL. It's really the future. 


## 2023 06 01
1. ~~script that makes markdown file~~
2. ~~script that makes markdown file with text~~
3. ~~script that makes markdown file with text from a source~~ *NEW*
4. script that makes markdown file with a portion of text from a source
5. script that makes markdown file for each portion of text from a source

got an idea for a different approach from [here](https://automatetheboringstuff.com/chapter8/). probably not the most efficient since you keep having to open and close the file, but it does the work. Probably a more efficient way _on that page_ but don't let that stop progress. ha. Maybe I'll read it in full later?

We have a script that copies from a source and puts to a new file destination!


## 2023 05 31
1. ~~script that makes markdown file~~
2. ~~script that makes markdown file with text~~
3. script that makes markdown file with text from a source
4. script that makes markdown file with a portion of text from a source
5. script that makes markdown file for each portion of text from a source

using info from the guru99 link from earlier to copy text, and I'm using info from [here](https://www.askpython.com/python/built-in-methods/python-print-to-file) to paste that text. Getting an error where I didn't correctly define the location of my sample text. Researching how to do that effectively. 


## 2023 05 08
Found the exported textfile from my blog, copied it to source_files/leftsider.txt  
Created file where I'll do the bulk of work, converter.py3  
Current idea: python script that breaks posts into markdown files?  

1. script that makes markdown file
2. script that makes markdown file with text
3. script that makes markdown file with text from a source
4. script that makes markdown file with a portion of text from a source
5. script that makes markdown file for each portion of text from a source

Looking up creating a file... I should know this...   
Good info [here](https://www.guru99.com/reading-and-writing-files-in-python.html); might be able to skip some steps  

going to uplevel this by making the filename a timestamp. that way I can track my outputs as I test. I think I did this before in another project; looking before I bother writing something  

[Found it and used it](https://stackoverflow.com/questions/10607688/how-to-create-a-file-name-with-the-current-date-time-in-python). We now have a script that makes a file and can write text to it. Going to stop here for the day.