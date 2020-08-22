import sys

args = sys.argv

if len(args) == 1:
	print('Usage: hexdecode [file]')
	sys.exit()

f = open(args[1], 'r')

phrase = f.read()
phrase = phrase.split()

output = ""

for num in phrase:
	output += f'{int(num, 16)} '

print(output)



