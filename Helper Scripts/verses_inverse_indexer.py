import re, hashlib, json

books = ["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua","Judges","Ruth","1 Samuel","2 Samuel","1 Kings","2 Kings","1 Chronicles","2 Chronicles","Ezra","Nehemiah","Esther","Job","Psalms","Proverbs","Ecclesiastes","Song of Solomon","Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel","Hosea","Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah","Haggai","Zechariah","Malachi","Matthew","Mark","Luke","John","Acts","Romans","1 Corinthians","2 Corinthians","Galatians","Ephesians","Philippians","Colossians","1 Thessalonians","2 Thessalonians","1 Timothy","2 Timothy","Titus","Philemon","Hebrews","James","1 Peter","2 Peter","1 John","2 John","3 John","Jude","Revelation"]
inverse_index = {}

def make_name(term, max_len=4):
	query = term.lower().encode("UTF-8")
	return "{}.txt".format(hashlib.md5(query).hexdigest()[:max_len])

def make_json(keyword, inverse_index, left_txt, starting_index):
	max_ngram = 6
	for i in range(3, min(max_ngram, len(keyword)) + 1):
		ngram = keyword[:i]
		if (not ngram in inverse_index) and len(ngram) != 0:
			print(ngram)
			file_name = make_name(ngram.lower())
			inverse_index[ngram] = file_name
			txt_json = {
				left_txt: [starting_index]
			}
			with open(f"./hashed_documents/{file_name}", "a") as file:
				file.write(f"\n{ngram}\t{json.dumps(txt_json)}")
		elif len(ngram) != 0:
			file_name = inverse_index[ngram]
			txt_json = {}
			all_lines = []
			with open(f"./hashed_documents/{file_name}", "r") as file:
				all_lines = file.readlines()

			found = False
			for index, line in enumerate(all_lines):
				if line.split("\t")[0].lower() == ngram.lower():
					found = True
					txt_json = json.loads(line.split("\t")[1])
					if not left_txt in txt_json:
						txt_json[left_txt] = [starting_index]
					else:
						txt_json[left_txt].append(starting_index)
					all_lines[index] = f"{ngram}\t{json.dumps(txt_json)}"

			if len(ngram) != 0 and found == False:
				txt_json = {
					left_txt: [starting_index]
				}
				all_lines.append(f"{ngram}\t{json.dumps(txt_json)}")

			with open(f"./hashed_documents/{file_name}", "w") as file:
				file.write("\n".join([line.strip() for line in all_lines]))

def hash_verse(verse_line, book_name, chapter_number, verse_number):
	verse = verse_line.split("\t")[1]
	for word_index, word in enumerate(verse.split(" ")):
		stop_words = {"a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"}
		word = word.strip(" \t\n0123456789.:[(<>)].,'\"‘’?--!•…")
		if not word.lower() in stop_words and len(word) != 0:
			starting_index = word_index
			left_txt = f"{book_name},{chapter_number},{verse_number}"
			make_json(word, inverse_index, left_txt, starting_index)

def main():
	book_name = "Genesis"
	chapter_number = 1
	read_document_path = f"./verses/{book_name}/{book_name}_ch_{chapter_number}.txt"
	with open(read_document_path) as file:
		lines = file.readlines()
		for line in lines:
			verse_number = line.split("\t")[0].split(" ")[1].strip(":")
			hash_verse(line, book_name, chapter_number, verse_number)

if __name__ == "__main__":
	main()