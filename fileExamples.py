targets_file = open('targets.txt','r')
lines = targets_file.readlines()
print lines

lines_dictionary = {}
for line in lines:
   one_line = line.split()
   line_key = one_line[0]
   line_value = one_line[1]
   lines_dictionary[line_key] = line_value

print "dictionary is populated"
print lines_dictionary

for key in lines_dictionary.keys():
   targets_string = lines_dictionary[key]
   targets_list = targets_string.split(',')
   targets_number = len(targets_list)
   filename = key + '_' + str(targets_number) + '_targets.txt'
   vuln_file = open(filename, 'w')
   for vuln_target in targets_list:
       vuln_file.write(vuln_target + '\n')
   vuln_file.close()

   
