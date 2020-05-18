"""Example showing Reading In Multiple Text Files Simultaneously"""

# two different files
# file 1
with open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/ReadingText/Gen5b.asc') as f:
    gen = list()
    for line in f:
        gen.append(line.rstrip('\n'))

# file 2
with open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/ReadingText/WGen5b.asc') as f:
    wgen = list()
    for line in f:
        wgen.append(line.rstrip('\n'))

gen[0] # notice how both of these files use '\t' characters as the separator
wgen[0]

# and watch what happens when the string is printed
print(gen[0])
# the tabs get interpreted as tabs

# These two files represent data from the same population of flies
# Each line in the files is an individual fly
# I'd like 1 data list, where information from the same fly, is all in 1 row, instead of 2 rows split over 2 text files
# Column 1 of the 'gen' file, and Column 14 (the final column) of the 'wgen' file, hold the tif name and number, which
# is unique to a fly

# read the files in simultaneously, and combine rows by finding the line in the 2nd text file, which has the same unique
# tif name and number, combine the two lines into 1 line
# This would be like merging two files based on some shared unique column

with open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/ReadingText/Gen5b.asc') as f1, open('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/ReadingText/WGen5b.asc') as f2:
    dat_list = list()
    # iterate through first file
    for x in f1:
        # get the unique tif name info
        f1_tifname = x.split('\t')[0]
        # the information from the f1 file which we want
        xinfo = x.rstrip('\n')
        # iterate through the second file
        for y in f2:
            # get the unique tif name info from file 2
            f2_tifname_temp = y.split('\t')[-1] # we haven't stripped new lines yet, so this is going to be the tif name + '\n'
            f2_tifname = f2_tifname_temp.rstrip('\n')
            # remove the last column from f2 because it will be redundant with f1 now
            yinfo = '\t'.join(y.split('\t')[0:12])
            # combine lines from files 1 and 2, also add a \t between the two, and add a \n
            merged_line = xinfo + '\t' + yinfo + '\n'
            # check if the tifname matches between two lines
            if f1_tifname == f2_tifname:
                # if it matches, we'll add the merged_line to our data_list
                dat_list.append(merged_line)
                # if the tifnames match, we no longer want to iterate through the rest of file 2, so we will break out
                # of the loop, and in this code, python will go to the next iteration of file 1
                break
            else:
                # if the two lines don't have the same tifname, we want to continue
                continue # continue, or pass will have the same effect in this code, but the two statements mean very
                # very different things, and do not always behave the same

dat_list # we now have 1 data list with, the dataframes merged by tifname