Aman Dhar

1. The offline part of my code reads N words in from a text file (O(N)), cleans/sorts each one (O(N * KlogK) for N words if max word length is K), and enters each into a list in a dictionary. After doing this, I sort and join all of my lists of anagrams into a neat string that will be printed should the user request it (O(NlogN) when all words are anagrams of each other). So this step takes O(N(KlogK + logN)) time.

The online part of my code reads in a word, cleans it up (by removing extra spaces, etc.), sorts it, and checks if it is in my dictionary. Again assuming the word is at most K characters long, this step should only take O(KlogK) time (mainly for sorting).

2. I store all N words given in the beginning in their original forms, and I store a key for each list of anagrams (<= 2N words). This consumes O(NK) memory.

3. If I didn’t have enough memory for the offline step, I would have to make some time/memory sacrifices in the online step. During the offline step, I would look for the most common anagrams in the dictionary and try to only preprocess and save those (as long as I can stay under the 2MB limit). For the rest of the words in the dictionary, I would have to look for anagrams during the online step. 

This way, for user input with lots of anagrams, I can maintain O(KlogK) time for sorting and checking in the online step. But for the rest, I would need to read individual words from the dictionary and check for anagrams, which would take O(N(KlogK + logN)) time.

Other:
I used sys to read in arguments from the command line. I also used defaultdict from collections to make all dictionary entries lists by default. 