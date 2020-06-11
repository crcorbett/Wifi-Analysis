import csv
filename = ['scans/loungeroom_wifi_scan.csv']
file_input = open(filename[0], 'r')
file_output =  open('output.csv', 'w')
writer = csv.writer(file_output, delimiter = ',')

removeStrings = ['bssid=', ' channel=', ']', '[',  ' bytes = ', 'width=', 'cc=', ' type=', ' rssi=', ' rsn=mcast=', ' ucast=', ' auths=', ' caps=', ' wpa=', ' wep=', ' ibss=', ' ph=', ' swap=', ' hs20=', ' airport=', ' ']


data = csv.reader(file_input)

firstLine = ['NetworkName','BSSID','Channel','Width','Country','Type','RSSI','RSNMCast','RSNUSCast','Auth','Caps','WPA','WEP','IBSS','PH','SWAP','hs20','Airport']
firstLine = str(firstLine)
for i in range(len(removeStrings)):
	firstLine = str.replace(firstLine, removeStrings[i], '')
writer.writerow(str(firstLine).split(','))

for line in data:
	line = str(line)
	new_line = line
	print(new_line)
	for i in range(len(removeStrings)):
		new_line = str.replace(new_line, removeStrings[i], '')
	new_line = str.replace(new_line, ' {length = ', ', ')
	new_line = str.replace(new_line, '<HIDDEN>', 'NA')
	new_line = str.replace(new_line, '(null)', 'NA')
	new_line = str.replace(new_line, '{ aes_ccm }', 'aes_ccm')
	new_line = str.replace(new_line, ' aes_ccm', 'aes_ccm')
	writer.writerow(new_line.split(','))

file_output.close()