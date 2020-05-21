"""Tutorial On How to Write Information to Text File.  Written/Tested with Python --version 3.7"""

# writing text to files is very similar to how one reads from a file
example_info = ['Animal Class\tExample', 'Mollusc\tOctopus', 'Mammal\tLion', 'Bird\tNuthatch', 'Reptile\tIguana']

# here is some fake data, the first item in the list will stand as a header, with the first column being animal class,
# and the second column being an example of that class.  Subsequent items in the list, are rows of data.  In this example
# I'm using \t character as the column separator

# in order to write to the file, we'll use a context manager
# the 'w+', option indicates that we are going to write to this file, and the + is indicating that if the file
# does not already exist, we'll create one. On GitHub the file will already exist for you because I've run this code.
with open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/WritingText/textout1.txt', 'w+') as f:
    # iterate through our data list, writing each item to the file
    for line in example_info:
        f.write(line + '\n') # add new line character to each item

# take a look at the file
# then let's run this code, notice that I've changed the 'w+' option, to 'w'.  The file already exists sso we don't need
# to add the + to create it.  Also notice I've removed the newline character on each iteration through the list
# look at what happens to the file after running this code
with open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/WritingText/textout1.txt', 'w') as f:
    # iterate through our data list, writing each item to the file
    for line in example_info:
        f.write(line)  # do not add new line character to each item

# notice that we've written over the previous version of textout1.txt.  If a file is already created, and you use the
# 'w' or 'w+' option, you will overwrite whatever is in the file, with what you wrote to the file
# So in this example, the file was made blank, and then the items of the list were added to one line of the file, because
# I removed the new lines

# sometimes you're not going to want that behavior, you don't want to write over a file, but append information to the file
# for that the open() function has an 'a' option for appending behavior

new_information = ['here\tis', 'more\tdata', 'you\twant', 'to\tadd', 'to\ta', 'text\tfile']
with open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/WritingText/textout1.txt', 'a') as f:
    # iterate through our data list, writing each item to the file
    for line in new_information:
        f.write(line + '\n')  # add new line character to each item

# notice how this did not overwrite that one line of information we added in the previous file write, it simply appended
# the new information

# See the SubsetText folder for more realistic examples of writing to a text file