import re
# pattern creating tool

# Simply place your number after the colon where it says 'count'
# Then place your test sentence or paragraph into the quotes. 
# If you understand the syntax, feel free to put multiple examples in at the same time.
#samples = [{
#	'count': 6,
#	'text': "Six people were murdered today in the state of Denmark"
#},]
samples = [{
	'count': 5,
	'text': ""	
}]

numbers = {
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9',
	'ten': '10',
	'eleven': '11',
	'twelve': '12',
	'thirteen': '13',
	'fourteen': '14',
	'fifteen': '15',
	'sixteen': '16',
	'seventeen': '17',
	'eighteen': '18',
	'nineteen': '19',
	'twenty': '20'
} 

# Set up sample patterns 
countPatterns = [
	re.compile(r"kill(?:ed|ing|s)?[^.]*?(\d+).*?(?:men|women|children|people)?"),
	re.compile(r"(\d+)[^\d.]*?(?:men|women|children|people)?[^\d.]*?(?:dead|died)"),
	re.compile(r"(\d+)[^\d.]*?(?:men|women|children|people)?[^\d.]*?(?:were|have been)? (?:killed|drowned|murdered)"),
]

def countFilter(article):
	for pattern in countPatterns:
		if pattern.search(article):
			print "count:", pattern.search(article).group(1), " from:", pattern.search(article).group()
			return int(pattern.search(article).group(1))

def dateFilter(article):
	pass

def locFilter(article):
	pass

# Tests to ensure that there are patterns to describe various article types
def countTest():
	samples[0]['text'] = samples[0]['text'].replace("\t","").replace("\n","").lower()
	for number in numbers.keys():
		samples[0]['text'] = samples[0]['text'].replace(number, numbers[number])
	
	tot = 0
	passed = 0
	for x in range(len(samples)):
		tot += 1
		if samples[x]['count'] == countFilter(samples[x]['text']):
			print "Article {} Passed countTest".format(x+1)
			passed += 1
		else:
			print "Article {} Failed countTest".format(x+1)
			pass
	print passed * 100.0 / tot, "% Pass Rate"
	return passed * 100.0 / tot

if __name__ == "__main__":
	countTest()

