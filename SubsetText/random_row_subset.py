"""Function to Randomly Subset User Supplied Number of Rows from a Text File, and Write the Random Subset Text File
 to a New Text File.
Also shows the general structure of a python program"""
import random # import the random module so that we can randomly pick items from a list

# function takes two positional and 1 keyword argument.  The keyword argument can act as a default, so if the user doesn't
# supply a value for header, the function defaults to True
def random_subset(filename, sample_size, header=True):
    if header: # this is the pythonic way to do the equality testing here.  You can read this like 'if True'.
        # you could also code this as if header == True, but it's not as pretty
        with open(filename) as f: # this  context manager will open and read only the first line to get the header information
            head_info = f.readline()
        data = [line for line in open(filename)][1:] # if there is a header, we want to get only the data rows so [1:]
    else:
        data = [line for line in open(filename)] # no header so everything is data
    # get the random sample
    sampled_data = random.sample(data, sample_size)
    # we are going to manipulate the filename string, to create a new filename, which will add subset to the name
    filename_split = filename.split('.') # splitting by ., will put the file path in [0] index of list, and txt in [1] index of list
    newfilename = filename_split[0] + '_subset.txt' # add subset.txt to the base filename
    with open(newfilename, 'w+') as f:
        f.write(head_info)
        for line in sampled_data:
            f.write(line)


if __name__ == '__main__':
    # if name is main looks confusing, but conceptually is not that complicated
    # basically what this code does, is that now if cd to the SubsetText folder and run this file as a script in the terminal like...
    # python snptable.txt, the following line of code gets executed
    random_subset('/home/bella/PycharmProjects/Python-ReadingAndWritingTextFiles/SubsetText/snptable.txt', 20)
    # however, if we wanted to use the function we defined in another program, and not run the line of code above..
    # we can do 'import random_row_subset', and have access to the function.  Getting the import to work is tricky
    # because python needs to have access to the folder the script is in, so that it can find it as a module.
    # The concept was pretty confusing to me at first,  so if you have question feel free to e-mail me at transferome1113@gmail.com



