import sys
from collections import defaultdict

if __name__ == '__main__':

	# Offline Step
	path = sys.argv[1]
	given_words = defaultdict(list)	
	with open(path) as f:
		words = [word.strip() for word in f.readlines()]
		for word in words:
			cleaned_word = word.lower()
			sorted_word = ''.join(sorted(cleaned_word))
			given_words[sorted_word].append(word)
	
	# Preprocessing anagrams into string to be printed
	for key in given_words.keys():
		anagrams = sorted(given_words[key])
		given_words[key] = ' '.join(anagrams)
	
	# Online Step
	while True:
		word = input()
		if word == '':
			break
		cleaned_word = word.strip().lower()
		sorted_word = ''.join(sorted(cleaned_word))
		if given_words[sorted_word]:
			print(given_words[sorted_word])
		else:
			print('-')