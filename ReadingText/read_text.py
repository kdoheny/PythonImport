"""Tutorial on Reading in Text Files in Python.  Using Python 3.7"""

# the main function used in reading/writing text files is 'open()'
# a main difficulty is supplying the appropriate file path, Python distributions like Anaconda allow you to create
# environments which can shorten the amount of info you need to supply for file paths

snptable = open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/ReadingText/snptable.txt')

# the file is now stored as a file object, which is very different from what we're used to with R
print(snptable)

# notice that mode is set to 'r', which means 'read', and we could have coded reading in the file this way...
snptable = open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/ReadingText/snptable.txt', 'r')
# however it's not needed, because it will default to 'r', when no option is given

# in order to get the information from the file, we need to call a 'method', which is a special function, associated
# with file objects
line_list = snptable.readlines()
print(line_list[0:10]) # print first 10 lines of file

# what's nice about these file objects, is that you can read in the lines of the text file into a list
# however, an important behavior, is that column separators are also read in
# snptable.txt is actually a 'csv' comma separated value text file
line_list[0] # note the commas inbetween the individual values, and the newline character at the end of the string
# but now watch what happens when we print that information to the screen
print(line_list[0]) # commas remain but the newline character is interpreted as a physical new line

# expanding on this, consider the following string, a bunch of \n newline characters
newlines = '\n\n\n\n\n\n\n\n\n'
newlines # we see the new line characters
print(newlines) # we see the new line characters interpreted as newlines

# IMPORTANT, when reading in files this way, you have to manually close them when you are done interacting with them
# otherwise you could have information lost within the opened file
# so let's close the snptable.txt file
snptable.close()

# So a better way to open files is with what's called a context manager, it will automatically close the file when the
# block of code within the context manager is all executed
# in this opening line, we will now refer to the file object as f
with open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/ReadingText/snptable.txt') as f:
    line_list = f.readlines()
# and no need to close the file
# at this point the file is closed, but the information has been read into python and stored into memory as a list
print(line_list[0:10])

# But there's some stuff about our data which is bothersome, such as the '\n' character at the end of each line
# However, we can filter information out of the text file as we read it into python

with open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/ReadingText/snptable.txt') as f:
    line_list = list() # creating empty list to store processed lines
    # even though f is a weird file object thing, we can still iterate through each line one at a time
    for line in f:
        # process the line by removing the '\n' character
        processed_line = line.rstrip('\n') # calling string method rstrip, removing first '\n' encountered from right
        line_list.append(processed_line) # add the processed line to our empty list

print(line_list[0:10]) # notice that the '\n''s are gone

##### python's built-in string, list, and operators can handle most complicated manipulations you might want
# to do to a text file

# read in only the first 8 columns of the text file
with open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/ReadingText/snptable.txt') as f:
    line_list = list() # creating empty list to store processed lines
    # even though f is a weird file object thing, we can still iterate through each line one at a time
    for line in f:
        # because 'n' is at end of string, and we are taking the first 8 columns, don't need to remove it
        split_line = line.split(',')[0:8] # comma separated text file, so columns are separated by ',''s
        # split_line is now a list, with each columns value, and item in that list, first line would look like
        # ['2L', 'Ref', 'line_21', 'line_31', 'line_38'...]
        # the [0:8], let's us slice out only the first 8 items in the list
        processed_line = ','.join(split_line) # now that we have first 8 items, join then back together with the ','
        line_list.append(processed_line)


# maybe we also want to exclude any rows, which contain an 'N', for this data N means missing information
# read in only the first 8 columns of the text file
with open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/ReadingText/snptable.txt') as f:
    line_list = list()  # creating empty list to store processed lines
    # even though f is a weird file object thing, we can still iterate through each line one at a time
    for line in f:
        # because 'n' is at end of string, and we are taking the first 8 columns, don't need to remove it
        split_line = line.split(',')[0:8]  # comma separated text file, so columns are separated by ',''s
        # split_line is now a list, with each columns value, and item in that list, first line would look like
        # ['2L', 'Ref', 'line_21', 'line_31', 'line_38'...]
        # the [0:8], let's us slice out only the first 8 items in the list
        processed_line = ','.join(split_line)  # now that we have first 8 items, join then back together with the ','
        # add conditional statement, to exclude rows from our list which contain N values
        if 'N' in processed_line:
            continue # go to next iteration of loop
        else:
            line_list.append(processed_line) # so when lines don't contain an N, they get added to our list

# Note that the above code is removing rows which, the subset 8 columns do not contain an N, and it is not removing
# any row which contains an N


# What if we wanted to get all rows, where the first columns is a value between 90,000 and 99,999
# There are numerous ways to do that, and in this situation, we know that those values will have to start with a 9, and
# has to contain 6 digits
example1 = '90876'
# there is a method to check if a string starts with something
example1.startswith('9')
# and the length function can tell us how many digits are in our number
len(example1)

# so to get only lines between 90,000 and 99,999
with open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/ReadingText/snptable.txt') as f:
    line_list = list()  # creating empty list to store processed lines
    # even though f is a weird file object thing, we can still iterate through each line one at a time
    for line in f:
        # multiple condition if statement, if 'True' and 'True': execute
        # to test the length of the number, we have to split the line by ',', and take out the first element [0]
       if line.startswith('9') and len(line.split(',')[0]) == 5:
           line_list.append(line.rstrip('\n')) # strip off new line while adding to list


# Note the above method is treating the numbers as strings, and not actually as numbers
# we could do it by treating them as numbers
# so to get only lines between 90,000 and 99,999
with open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/ReadingText/snptable.txt') as f:
    line_list = list()  # creating empty list to store processed lines
    # even though f is a weird file object thing, we can still iterate through each line one at a time
    for line in f:
        number = line.split(',')[0]
        num = int(number) # we have to convert the string number, into an integer number
        if 90000 <= num <= 99999:
            line_list.append(line.rstrip('\n')) # strip off new line while adding to list

# the above code is returning an error, because we cannot convert '2L' into an integer, it contains a letter
with open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/ReadingText/snptable.txt') as f:
    line_list = list()  # creating empty list to store processed lines
    # even though f is a weird file object thing, we can still iterate through each line one at a time
    for line in f:
        if not line.startswith('2L'): # only deal with lines which do not start with '2L'
            number = line.split(',')[0]
            num = int(number) # we have to convert the string number, into an integer number
            if 90000 <= num <= 99999:
                line_list.append(line.rstrip('\n')) # strip off new line while adding to list

print(line_list)