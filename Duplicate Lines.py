#####

#####
outputFile = open('UpdatedFile.txt', 'w')

#
inputFile = open('Repeated.text', 'r')

###
lines_seen_so_far = set()
print("Eliminating duplicate lines.......")
######
for line in inputFile:
 input
    ######
if line not in inputFile:

        #####
        outputFile.write(line)

        #######
        lines_seen_so_far.add(line)

######
inputFile.close()
outputFile.close()