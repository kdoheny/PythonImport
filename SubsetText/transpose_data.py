"""Function to Tranpose a Dataframe, it will make the columns the rows, and the rows the columns.  Written/Tested with
python --version 3.7"""
# looking at position_as_row.txt, there is a header line, the first column is nucleotide position, and every column after
# is the nucleotide identity of a haplotype at that position, with 106 haplotypes total, so the total columns is 107
# The problem is, to get another program to work, I want the columns to be the rows.  So that each row is a haplotype,
# and each column is a nucleotide position.  Basically we want the rows to be columns, and the columns to be rows.
# The easiest way I've found to do that, is to turn the datframe into a matrix, and transpose it, then turn it back into a list.
import numpy as np


def txt_to_list(filename):
    """Function reads in \t delimited text file, and creates a nested list.  Each item in the list, is a list which is a
     line split into a list by the \t delimiter"""
    txt_list = list()
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n') # remove newline character
            line_as_list = line.split('\t')
            txt_list.append(line_as_list)
    return txt_list


def check_list_lengths(txt_to_list_data):
    """Check if all lines, have the same number of elements in their lists"""
    # creates a list of either True or False, depending on if the length of the list, is equal to the length of the first
    # line
    tester_list = [len(x) == len(txt_to_list_data[0]) for x in txt_to_list_data]
    # following returns true if all items in list are True ( I think this might also return true if all values are false
    # but that's never going to happen because first value will always be True )
    return all(tester_list)


def transpose_data(txt_to_list_data):
    """Transforms data so that rows are columns, and columns are rows"""
    # convert our nested list into a numpy array
    data_array = np.array(txt_to_list_data)
    # now that data_array is numpy object array, we can call the .transpose() method on it
    data_transposed = data_array.transpose()
    # now we'll convert it back to a list from the numpy array object
    transposed_data = data_transposed.tolist()
    # and now let's join lines back together with '\t', and add new lines to the end of each of the new rows
    return ['\t'.join(line_list) + '\n' for line_list in transposed_data]


def write_text(filename, txt_list):
    """Given a filename, writes lines of text to a file as is"""
    with open(filename, 'w+') as f:
        for line in txt_list:
            f.write(line)


if __name__ == '__main__':
    # read in text file, with each line being split into a list, creating a nested list
    original = txt_to_list('SubsetText/position_as_row.txt')
    # in order for the tranposition to work, all lists, within the nested list, must be the same length
    check_list_lengths(original)
    # transpose the txt list into the new dataframe
    trans = transpose_data(original)
    # write the new transposed dataframe to a text file
    write_text('SubsetText/haplotypeID_as_row.txt', trans)
    # note that 'Pos' would technically need to be changed to 'haplotypeID', but other than that the file now has haplotypes
    # as the rows