# Name: Kyle Schaefer

# Computer Science Foundations
# Programming as a Way of Life
# Homework4 (part 2)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1

    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###
total_seq = len(seq)
# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
# Mumber of A and T nucleotides seen so far.
at_count = 0
# The next four variables count for the individual G, c, A, and T content
c_count = 0
g_count = 0
a_count = 0
t_count = 0
# for each base pair in the string,
for bp in seq:
   
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
    # next, if the bg is A or T,
    if bp == 'A' or bp == 'T':
	# increment the count of at
        at_count = at_count + 1
    # the next statment counts specifically for C
    if bp == 'C':
	c_count = c_count + 1
    # this statement counts specifically for G
    if bp == 'G':
	g_count = g_count + 1
   # Checks for individual A 
    if bp == 'A':
        a_count = a_count + 1
    # Checkes for individual T
    if bp == 'T':
	t_count = t_count + 1

# Adds A T G C for one total number
gcat_total = gc_count + at_count
# divide the gc_count by the total_count
gc_content = float(gc_count) / gcat_total
# divide the at_count by the total_count
at_content = float(at_count) / gcat_total
# Gets the ration of AT to GC
atgc_ratio = float(a_count + t_count) / (g_count + c_count)
# this is the first half of the equation to get the percentage of gc 
percent = float(g_count + c_count) / (gcat_total)
# this is the second half of the equation to get the percentage of gc
percentp2 = float(percent * 100)


# This statment determines if the contentis high, lower or moderate
if percentp2 > 60.0:

	classif = "High"

elif percentp2 <= 40.0:
	
	classif ="Low"
else:
	
	classif = "Moderate"

# Print the answer
print "GC-Content:", gc_content
print "AT-Content:", at_content
print "Total G-Count:", g_count
print "Total C-Count:", c_count
print "Total A-Count:", a_count
print "Total T-Count:", t_count
print "Total of gc and at:", gcat_total
print "Total count:", total_count
print "Seq length:", total_seq
print "AT/GC Ratio:", atgc_ratio
print "GC percentage:", percentp2
print "GC Classification:", classif
