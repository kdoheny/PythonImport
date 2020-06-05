"""Function to Subset a text file given a string, it can subset by searching entire line for the string, or searching
particular columns for the string.  Code written/tested with python --version 3.7"""


def col_num_from_name(indexed_header, column_name):
    """Simple Function, Given an Indexed Header, and a column name, returns the column index"""
    index_list = [tup[0] for tup in indexed_header if column_name == tup[1]]
    # check that indexes returned is not greater than 1
    if len(index_list) == 1:
        return index_list[0]
    else:
        print('Error, No Matching Column Name or Not Unique Column Name')


def subset_string(filename, sub_string, **kwargs):
    """Function subsets a text file, takes the filename, the delimiter the file uses, and if it has a header or not"""
    # set kwarg keys
    # either gets delimiter given by user, or sets the default to ','
    delimiter = kwargs.get('delimiter', ',')
    # either gets header given by user, or set the default to False
    header = kwargs.get('header', False)
    # either gets the col_scan info, or sets default to None
    col_scan = kwargs.get('col_scan', None)

    # get possible header, doesn't matter if do this and file doesn't have header
    # get the header line, split and enumerate it, this will make a list of paired column names and column numbers
    # want enumerate to start at 0, and that is default, enumerate returns a generator object, which will be easier
    # to work with as a list.  And the header is not going to be a memory issue anyway
    with open(filename) as f:
        head = f.readline()
        head = head.rstrip('\n')
    head_guide = list(enumerate(head.split(delimiter)))

    # if there is a header, but no specific columns are given to scan
    if header and not col_scan:
        # read in the rest of the file
        data = [line for line in open(filename)][1:]
        # get lines which contain string
        output_data = [line for line in data if sub_string in line]
        # add header back to beginning of list
        output_data.insert(0, head + '\n')
        return output_data

    # if there is a header, and specific columns are given to scan
    if header and col_scan:
        data = [line for line in open(filename)][1:]
        # Using our previously defined function here, in our larger function.  Splitting up the code helps
        # readability in my opinion.  Adding the block of code which col_num_from_name contains here would
        # make subset_string much harder to follow.  And if we thought about it more, we could probably define some
        # other user made functions, which would
        col_scans = col_scan
        # if col_scans is a string, there is only one column to check the sub_string in
        if isinstance(col_scans, str):
            # Using our previously defined function here, in our larger function.  Splitting up the code helps
            # readability in my opinion.  Adding the block of code which col_num_from_name contains here would
            # make subset_string much harder to follow.  And if we thought about it more, we could probably define some
            # other user made functions, which would clean up this larger function, and break it down into smaller
            # sub components. It's really a personal choice, but python does have a pretty extensive document about
            # how to make your code readable
            index = col_num_from_name(head_guide, col_scans)
            # getting the column index, so that we can search for the string in a specific column that's been
            # split by the delimiter
            output_data = [line for line in data if sub_string in line.split(delimiter)[index]]
            output_data.insert(0, head + '\n')
            return output_data
        # if col_scans is a list, there are multiple columns to check the sub_string in,
        # it might be helpful to walk through
        # the following line by line.  For me having a user give more than 1 column to search was tricky, the way
        # I solved it is below, but there is probably a better way
        if isinstance(col_scans, list):
            output_data_list = list()
            index_list = list()
            for kwarg in col_scans:
                index = col_num_from_name(head_guide, kwarg)
                index_list.append(index)
            # print(index_list)
            # get data
            for line in data:
                column_info = [line.split(delimiter)[i] for i in index_list]
                column_test = [sub_string in s for s in column_info]
                if all(column_test):
                    output_data_list.append(line)
            output_data_list.insert(0, head + '\n')
            return output_data_list

    # if no header is given, but column indexes are given
    if not header and col_scan:
        # with no header all we have to do  is read in file
        data = [line for line in open(filename)]
        col_scans = col_scan
        # as with the other time we dealt with col_scan being true, we have to deal with times when a user
        # may give more than one column.
        if isinstance(col_scans, int):
            index = col_scans
            # we need to subtract one from the index because python is 0 based, first column is 0, but users
            # will likely give a 1 for the first column and so on
            output_data = [line for line in data if sub_string in line.split(delimiter)[index - 1]]
            return output_data
        if isinstance(col_scans, list):
            output_data_list = list()
            index_list = col_scans
            for line in data:
                # again gotta watch out for the subtracting a 1
                column_info = [line.split(delimiter)[i - 1] for i in index_list]
                column_test = [sub_string in s for s in column_info]
                if all(column_test):
                    output_data_list.append(line)
            return output_data_list

    # if there is no header, and no columns given to scan, the process is easy
    if not header and col_scan:
        data = [line for line in open(filename)]
        output_data = [line for line in data if sub_string in line]
        return output_data


if __name__ == '__main__':
    # note how the file extension really means nothing, it's more for you to associate files with certain types of data
    # structure, but no matter extension all you need is open() function *there will be exceptions with compressed
    # files and files with strange encoding*

    # running this, 'M' is going to be somewhere in most lines because of the time listing
    # either AM or PM
    # so the subset is working but returns all lines, including the header
    test = subset_string('SubsetText/Output_Landmarks+Veins+Outline.dat', 'M', col_scan=None, delimiter='\t', header=True)
    print(len(test))

    # to deal with the problem in test, we can change col_scan to 'Sex'
    test2 = subset_string('SubsetText/Output_Landmarks+Veins+Outline.dat', 'M', col_scan='Sex', delimiter='\t', header=True)
    print(len(test2))
    # 249 is indeed how many Males are in the file, 250 is because we add a line for the header

    # now if we imagine this file did not have a header, we need to give the column number for the column we want to scan
    # header will default to false, so we can leave it blank
    test3 = subset_string('SubsetText/Output_Landmarks+NoHeader.dat', 'M', col_scan=12, delimiter='\t')
    print(len(test3))
    # now there is 249 lines because there was no header

    # let's try giving it three columns with a header, from a different file than we previously have tested the code with
    # note that we can leave out delimiter, ti will default to comma separated
    # what this should hopefully do, is return all lines where these three haplotypes, have a 'T' for a row (which is a nucelotide position)
    test4 = subset_string('SubsetText/snptable.txt', 'T', col_scan=['line_21', 'line_91', 'line_136'], header=True)
    print(len(test4))
    # appears to work

    # TODO: Currently the multiple column scan is looking that the string is in all columns given, but sometimes
    #  we might only need it to be true in 1 of the columns


