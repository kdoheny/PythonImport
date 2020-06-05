# **Python-ReadingAndWritingTextFiles** #
Examples reading, and writing information from/to text files.  
--Scripts Written/Tested with Python Version--Python 3.7--

###  **Why learn base python methods of reading/writing files?** ###
  
Python has a module named PANDAS, which makes manipulating data similar to R.  PANDAS includes some powerful code, which
can make certain data processing tasks simple.  However, I think knowing how to read and write data in base Python,
will help you better understand Python, and greatly increase your ability to do custom data manipulation, which is extremely useful,
because it's not always possible to find an adequate solution to your data problem on say 'Stack Overflow'.

### **Repository Overview** ###

1. **ReadingText** Folder

    Contains 3 different text files, 2 have .asc extensions, but those are still text files.
    Also contains 2 python scripts.
    * 'read_text.py' has various examples of reading in text from a file and manipulating it.
    * 'read_multiple_text_simultaneously.py' demonstrates a useful ability to read in two files at the same time, and manipulate them.
 
2. **WritingText** Folder

    Contains python script 'write_text.py'
    * 'write_text.py' writing information out to a text file, demonstrating creating new text files, and appending to
    existing text files.  The text file textout1.txt is created while running the script.
    
3. **SubsetText** Folder

    A folder to contain user defined functions, to subset a text file in specific ways.
    * 'random_row_subset.py' defines a function, which given a text file, and a user specified number of rows, will
    randomly sample that number of rows from the file ( without replacement ), and create a new text file, which 
    is the random sample of rows.
    * 'transpose_data.py' defines functions which you can use to make the columns of a dataframe the rows, and vice versa
    * 'string_subsetter.py' trying to make a versatile function/module for sub-setting text files, given some string,
    setup to handle header or no header, and different delimiters
    
4. **FileComparison** Folder
   
    A folder to contain user defined functions which somehow compare text files.
    * 'file_differences.py', given two text files, this will create a new text file, showing the lines
    which differ between the two text files
 




