"""Print Line Numbers Which are Different to the Screen, along with the two different lines.
I wrote this because I had two files of about 290MB and 290.5MB, and I want to see what is actually different
between those two files.  Written in python --version 3.7"""


def file_difference(file1, file2, outfile='file_differences.txt'):
    """Finds differences between two text files and records them into a new text file, if differences exist.
    A default file_difference.txt will be created in working directory if user does not supply an outfile"""
    # open all necessary files with context manager
    with open(file1) as f1, open(file2) as f2, open(outfile, 'w+') as w1:
        # get all lines from file 2
        lines2 = [line for line in f2]
        out_lines = list()
        # enumerate lines from f1, so we can get proper index for lines2, want to compare row 1 from file A, with row1
        # from file 2, and do that for all rows between the filess
        for i, lines1 in enumerate(f1):
            # if the lines f rom the two files don't match, we'll add there info to a list
            if lines1 != lines2[i]:
                out_lines.append('File-Line: ' + str(i) + '\n')
                out_lines.append(lines1)
                out_lines.append(lines2[i] + '\n\n\n')
        # if out_lines is empty, the files are identical
        if len(out_lines) == 0:
            print('No Differences Between:')
            print(file1)
            print(file2)
        # if there are differences they'll get written to the outfile
        else:
            for line in out_lines:
                w1.write(line)
            print('Differences Between Files Written To:\t\t' + outfile)


if __name__ == '__main__':
    file_difference('FileComparison/dgrp2L_file1.txt',
                    'FileComparison/dgrp2L_file2.txt',
                    outfile='FileComparison/mixed_differences.txt')
