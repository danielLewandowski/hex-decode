import sys

args = sys.argv

if len(args) == 1:
	print('Usage: hexdecode [options] [file]')
	print('-a Convert output to ASCII characters')

	sys.exit()

f = open(args[1], 'r')

phrase = f.read()
phrase = phrase.split()

dec = ""
chars = ""

for num in phrase:
	conv = int(num, 16)

	dec += f'{conv} '
	chars += f'{chr(conv)}'

print(dec)

div = ""
for x in range(0, len(dec)):
	div += '-'
print(div)
print(chars)
