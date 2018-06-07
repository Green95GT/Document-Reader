import sys

def print_words(fopen):
	
	f = open(fopen,'r')
	letters = []
	word = []
	word_size = []
	
	"""iterate over the lines in the file"""
	for line in f:
		if line != '\n': 
			"""iterate over each letter in line"""
			for printable in line:
				if not printable.isspace():
					letters.append(printable)
				else: 
					word_size.append(len(letters))
					"""concatenate letters list into words"""
					result = ''
					for element in letters:
						result += str(element)
					word.append(result)	
					letters.clear()
		elif line == '\n\n':
			letters.append('\n\n\n')
		elif line == '\n':
			letters.append('\n\n')		
	
	"""Calculating the median size of word length"""
	word_size.sort()
	if len(word_size) % 2 == 0:
		median = (word_size[int(len(word_size)/2 - 1)] + word_size[int(len(word_size)/2)]) / 2
	else:
		median = word_size[int((len(word_size)-1)/2)] 

	print ('The amount of words in this document is: ', len(word))
	print ('The median length of word is: ', median)
	
	decision = input('Would you like the program to read the document (y/n)? ')
	if decision == 'y':
		result1 = ''
		for elements in word:
			result1 += str(elements)
			result1 += ' '
		print (result1)
	else:
		f.close()

def main():
	if len(sys.argv) != 2:
		print ('usage: ./median_word_length.py file')
		sys.exit(1)
	filename = sys.argv[1]
	print_words(filename)

if __name__ == '__main__':
	main()	
