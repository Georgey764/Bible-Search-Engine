import json, hashlib, math, os, re
from docx import Document

_stop_words = {"a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"}
_total_num_files = len(os.listdir("./hashed_documents"))
_document_length_dict = {}
with open("./document_length.txt", "r") as file:
	lines = file.readlines()
	_document_length_dict = json.loads(lines[0])

def _make_hash_name(term, max_len=4):
	max_ngram = 6
	query = term.lower()[:min(max_ngram, len(term))].encode("UTF-8")
	return "{}.txt".format(hashlib.md5(query).hexdigest()[:max_len])

def _get_bm25_score(document_length, num_of_doc_containing_key, keyword_freq_in_doc):
	idf = math.log(((_total_num_files - num_of_doc_containing_key + 0.5) / (num_of_doc_containing_key + 0.5)) + 1)
	k1 = 0
	b = 0
	avg_len_of_docs = 800
	second_part = (keyword_freq_in_doc * (k1 + 1)) /  ((keyword_freq_in_doc + k1) * (1 - b + (b * (document_length / avg_len_of_docs))))
	return idf * second_part	

def _parse_query(query, bm25_scores):
	for keyword in (" ".join(query.split("\n"))).split(" "):
		max_ngram = 6
		keyword = keyword.strip(" \t\n0123456789.:[(<>)].,'\"‘’?--•…")
		if not keyword.lower() in _stop_words and keyword:
			keyword = keyword[:min(max_ngram, len(keyword))]
			print(keyword)
			file_name = _make_hash_name(keyword.lower())
			if os.path.exists(f"./hashed_documents/{file_name}"):
				with open(f"./hashed_documents/{file_name}") as file:
					all_lines = file.readlines()
					for line in all_lines:
						if line.split("\t")[0] == keyword.lower():
							term = line.split("\t")[0]
							txt_json = json.loads(line.split("\t")[1])
							num_of_doc_containing_key = len(txt_json)
							for document, value in txt_json.items():
								keyword_freq_in_doc = len(value)
								document_length = _document_length_dict[document]
								if not document in bm25_scores:
									bm25_scores[document] = _get_bm25_score(document_length, num_of_doc_containing_key, keyword_freq_in_doc)
								else:
									bm25_scores[document] = bm25_scores[document] + _get_bm25_score(document_length, num_of_doc_containing_key, keyword_freq_in_doc)

def return_bm25_scores(query):
	bm25_scores = {}
	_parse_query(query, bm25_scores)
	sorted_bm25 = sorted(bm25_scores.items(), key=lambda x:x[1], reverse=True)
	return sorted_bm25

def get_chapter(book, chapter):
	path = f"./Books/{book}/{book}_ch_{chapter}.docx"
	document = Document(path)
	text = ""
	for line in document.paragraphs:
	    text += "\n" + line.text
	return text.split("\n")

def return_keyword_indices(query, book, chapter):
	keywords = set()
	for keyword in (" ".join(query.split("\n"))).split(" "):
		max_ngram = 6
		keyword = keyword.strip(" \t\n0123456789.:[(<>)].,'\"‘’?--•…")
		if len(keyword) != 0:
			keywords.add(keyword.lower())
	text = get_chapter(book, chapter)
	keywords_index = {}
	for line_index, line in enumerate(text):
		for word_index, word in enumerate(re.split(r"[ \t]+", line)):
			para_keyword = word.strip(" \t\n0123456789.:[(<>)].,'\"‘’?--•…")
			if para_keyword.lower() in keywords:
				if line_index not in keywords_index:
					keywords_index[line_index] = []
				keywords_index[line_index].append(word_index)
	return keywords_index

def return_preview_text(query, book, chapter):
	keywords_index = return_keyword_indices(query, book, chapter)
	if len(keywords_index) != 0:
		maxVal = max(keywords_index.items(), key=lambda x:len(x[1]))
		text = get_chapter(book, chapter)
		line_index = maxVal[0]
		preview_text = text[line_index]
	else:
		preview_text = "No preview text available."
	return preview_text

def return_preview_indices(query, book, chapter):
	keywords_index = return_keyword_indices(query, book, chapter)
	if len(keywords_index) != 0:
		maxVal = max(keywords_index.items(), key=lambda x:len(x[1]))
	else:
		maxVal = [-1,[-1]]
	return maxVal

def main():
	query = """
	In the beginning the god created the sky
	"""
	result = return_bm25_scores(query)
	print(result)
	

if __name__ == "__main__":
	main()



