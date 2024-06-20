from docx import Document
import re

book_name = "1 Corinthians"
chapter_number = 4

read_document_path = f"./Books/{book_name}/{book_name}_ch_{chapter_number}.docx"
read_document = Document(read_document_path)
paragraphs = read_document.paragraphs

def extract_digits(query):
	done = False
	counter = 0
	result = ""
	while not done and counter < len(query):
		if query[counter].isdigit():
			result += query[counter]
			counter += 1
		else:
			done = True
	return int(result)

text = ""

for paragraph in paragraphs:
	text = text + "\n" + paragraph.text

for paragraph_index, paragraph in enumerate(paragraphs):
	write_document_path = f"./verses/{book_name}/{book_name}_ch_{chapter_number}.txt"
	words = re.split(r"[ \n\t]+", paragraph.text)
	starting_index = 0
	first_match = True
	verses = []
	for word_index, word in enumerate(words):
		if(re.match(r"^\d+\D.*", word) and not len(word) < 2 and ":" not in word):
			if not first_match:
				verses.append(" ".join(words[starting_index: word_index]))
				starting_index = word_index
			else:
				starting_index = word_index
				first_match = False
		elif word_index == len(words) - 1 and not first_match:
				verses.append(" ".join(words[starting_index:]))
				edited_verses = [f"Verse {extract_digits(line.split(" ")[0])}:\t" + line for line in verses]
				with open(write_document_path, "w") as file:
					file.write("\n".join(edited_verses))
	

# print(text.split(" ")[66])
# print((re.match(r"^\d+[a-zA-Z]+$", "123213Hi")))