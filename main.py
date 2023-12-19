import os
import time
import random

files = os.listdir("./texts")
#files = ['fairy_tale_snap.txt']

puncuation = ['.', '!', '?']

ignore_word = ['and','to','the','with','how','so','i','it','no','me','.',',',';','!','?','oh','all']

connector_words = ['can','what','the','with']


def remove_items(test_list, item):  
	# using list comprehension to perform the task 
	res = [i for i in test_list if i != item] 
	return res 

def replace_chars(line):
	line = line.replace('.', ' . ')
	line = line.replace(',', ' , ')
	line = line.replace('!', ' ! ')
	line = line.replace('?', ' ? ')
	line = line.replace(';', ' ;')
	line = line.replace(':', '')
	line = line.replace('”', '')
	line = line.replace('’', '')
	line = line.replace(' ll ', '')

	line = line.replace('[', '')
	line = line.replace(']', '')

	line = line.replace('-', '')
	line = line.replace('_', '')
	line = line.replace('+', '')
	line = line.replace('/', '')
	line = line.replace('(', '')
	line = line.replace(')', '')
	line = line.replace('"', '')
	line = line.replace("'", '')
	line = line.replace('„', '')
	line = line.replace('“', '')
	line = line.replace('\n', '')


	return line
distribution_dict = {}
word_list = []
for file_name in files:
	path = 'texts/' + file_name

	
	with open(path) as open_file:

		for line in open_file:
			first_char = line[0:1]
			if first_char != " ":
				line = replace_chars(line)
			

				text = line.split(" ")
				text = remove_items(text, '')
				for w in text:
					word_list.append(w.lower())
				#word_list.extend(text)


word_len = len(word_list)
ix = -1
for word in word_list:
	ix += 1
	if ix >= word_len-1 and ix != 0:
		continue

	w = word
	mx = min(ix,10)
	for i in range(0,mx):
		distribution_dict[w] = []
		w = word_list[ix-i] + '|' + w

print ('> Finished compiling word list')
ix = -1
for word in word_list:
	ix += 1
	if word == None or ix >= word_len-1:
		continue

	w = word
	mx = min(ix,10)
	for i in range(0,mx):
		value = distribution_dict.get(w)
		value.append(word_list[ix+1])
		distribution_dict[w] = value

		w = word_list[ix-i] + '|' + w

print ('\n> Finished distribution_dict compilation')

f = open("distribution_dict.txt", "w")
f.write(str(distribution_dict))
f.close()
print ('\n> Finished writing to disk')

while 1:

	text = input("\ninput: ")
	text = text.lower()

	i = 0
	last_last = ''
	last_couple = []
	last_puncuation = 0
	while 1:
		i += 1
		if i > 100 and rand_word == ".":
			break
		if i > 300:
			print ('\nProcess killed for taking too much time')
			break

		newtext = text
		#for word in ignore_word:
		#	newtext.replace(word, '')

		split = newtext.split(" ")
		last = split[-1]
		get_list = distribution_dict.get(last)
		if get_list == None:
			print ('\nWord not in dictionary')
			break

		found = False
		while not found:
			w = ''
			rsplit = split
			rsplit.reverse()
			for iy, wr in enumerate(rsplit):
				if iy == 0:
					w = wr
				else:
					w = wr + '|' + w

				dist_r = distribution_dict.get(w)
				if dist_r != None:
					random.shuffle(dist_r)
					for each in dist_r:
						if each != last_last:
							rand_word = each
							found = True
							break
				

		text = text + " " + rand_word


		last_last = rand_word


		display_split = text.split(" ")
		display = ''
		prev = '.'
		for each in display_split:
			onew = each
			new = each
			if prev in puncuation:
				new = new.title()
			if new == "," or new == "." or new == "!" or new == "?" or new == ";":
				new = new
			else:
				if new == 'i':
					new = 'I'
				new = " " + new 

			display = display + new
			prev = onew

		print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" + display.strip())
		time.sleep(0.01)


