from bs4 import BeautifulSoup
import re

# Get all articles, import their text as data 

# Run filters to build a database of the following:
# {event: {date, count, location, description}}

# Get samples

regions = []
with open("list2.txt","r") as file:
	regions = file.read().split("\n")[:-1]

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
samples = [] 

def getSamplesFromXML():
	with open('examples/articles.xml', 'r') as file:
		data = file.read()
	data = data.lower()
	data = data.replace('\n', '')
	data = data.replace('\t', '')
	for number in numbers.keys():
		data = data.replace(number, numbers[number])
	soup = BeautifulSoup(data, "lxml")
	for child in soup.xml.children:
		ret = {}
		for grandchild in child:
			if grandchild.name == "details":
				ret['count'] = int(grandchild.count.get_text())
				ret['date'] = grandchild.date.get_text()
				ret['loc'] = grandchild.loc.get_text()
				print ret['loc']
			else:
				ret['text'] = grandchild.get_text().lower()
		samples.append(ret)


def sanitizeText(text):
	pass

def displaySamples():
	getSamplesFromXML()
	for sample in samples:
		print "Count: {}, Date: {}, Location: {}\n{}".format(sample['count'], sample['date'], sample['loc'], sample['text'])

# Set up sample patterns 
countPatterns = [
	re.compile(r"kill(?:ed|ing|s)?[^.]*?(\d+).*?(?:men|women|children|people)?"),
	re.compile(r"(\d+)[^\d.]*?(?:men|women|children|people)?[^\d.]*?(?:dead|died)"),
	re.compile(r"(\d+)[^\d.]*?(?:men|women|children|people)?[^\d.]*?(?:were|have been)? (?:killed|drowned|murdered)"),
]
datePatterns = []

descriptPatterns = [
	#re.compile(r"")
]

# Run articles through patterns
def filter(article):
	stats = {}
	stats['count'] = countFilter(article)
	stats['date'] = dateFilter(article)
	stats['loc'] = locFilter(article)
	return stats

def countFilter(article):
	for pattern in countPatterns:
		if pattern.search(article):
			print "count:", pattern.search(article).group(1), " from:", pattern.search(article).group()
			return int(pattern.search(article).group(1))

def dateFilter(article):
	pass

def locFilter(article):
	for region in regions:
		if region in article:
			print region
			return region

# Tests to ensure that there are patterns to describe various article types
def countTest(sliceEnd):
	tot = 0
	passed = 0
	for x in range(len(samples)):
		tot += 1
		if samples[x]['count'] == countFilter(samples[x]['text'][:sliceEnd]):
			print "Article {} Passed countTest".format(x+1)
			passed += 1
		else:
			print "Article {} Failed countTest".format(x+1)
	print passed * 100.0 / tot, "% Pass Rate"
	return passed * 100.0 / tot

def countStats():
	stats = []
	good = []
	for x in range(max([len(x['text']) for x in samples])):
		stats.append(countTest(x))
	#print stats
	#print len(stats)
	for x in range(len(stats)):
		if stats[x] == 100.0: good.append(x)
	#print good
	print "Spread: {} - {}".format(min(good), max(good))

def regionTest():
	tot = 0
	passed = 0
	for x in range(len(samples)):
		tot += 1
		print samples[x]['loc']
		if samples[x]['loc'] == locFilter(samples[x]['text']):
			print "Article {} Passed locTest".format(x+1)
			passed += 1
		else:
			print "Article {} Failed locTest".format(x+1)
	print passed * 100.0 / tot, "% Pass Rate"
	return passed * 100.0 / tot

def test3():
	pass

if __name__ == "__main__":
	getSamplesFromXML()
	#countTest(350)
	regionTest()
	#countStats()
	#print test2()
	#displaySamples()
