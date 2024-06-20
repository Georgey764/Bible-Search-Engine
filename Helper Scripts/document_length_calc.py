from docx import Document
import os, json, re 

books = ["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua","Judges","Ruth","1\\ Samuel","2\\ Samuel","1\\ Kings","2\\ Kings","1\\ Chronicles","2\\ Chronicles","Ezra","Nehemiah","Esther","Job","Psalms","Proverbs","Ecclesiastes","Song\\ of\\ Solomon","Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel","Hosea","Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah","Haggai","Zechariah","Malachi","Matthew","Mark","Luke","John","Acts","Romans","1\\ Corinthians","2\\ Corinthians","Galatians","Ephesians","Philippians","Colossians","1\\ Thessalonians","2\\ Thessalonians","1\\ Timothy","2\\ Timothy","Titus","Philemon","Hebrews","James","1\\ Peter","2\\ Peter","1\\ John","2\\ John","3\\ John","Jude","Revelation"]
book_name = ["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua","Judges","Ruth","1 Samuel","2 Samuel","1 Kings","2 Kings","1 Chronicles","2 Chronicles","Ezra","Nehemiah","Esther","Job","Psalms","Proverbs","Ecclesiastes","Song of Solomon","Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel","Hosea","Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah","Haggai","Zechariah","Malachi","Matthew","Mark","Luke","John","Acts","Romans","1 Corinthians","2 Corinthians","Galatians","Ephesians","Philippians","Colossians","1 Thessalonians","2 Thessalonians","1 Timothy","2 Timothy","Titus","Philemon","Hebrews","James","1 Peter","2 Peter","1 John","2 John","3 John","Jude","Revelation"]

def main():
	result = {}
	with open("./document_length.txt", "w") as file:
		for book in book_name:
			num_of_chapters = len(os.listdir(f"./Books/{book}")) - 1
			for chapter_num in range(1, num_of_chapters + 1):
				document_name = f"{book}_ch_{chapter_num}.docx"
				path = f"./Books/{book}/{document_name}"
				document = Document(path)
				text = ""
				for paragraph in document.paragraphs:
					text += "\n" + paragraph.text
				doc_length = len([word for word in re.split(r"[ \n\t]+", text) if word.strip(" \t\n0123456789.:[(<>)].,'\"‘’?–-•…") != "" and len(word.strip(" \t\n0123456789.:[(<>)].,'\"‘’?–-•…")) != 0])
				result[document_name] = doc_length
				# print(f"{document_name} {doc_length}")
		file.write(json.dumps(result))

if __name__ == "__main__":
	main()
