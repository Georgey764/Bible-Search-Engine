import json, hashlib, math, os, re
from docx import Document

query = """
        In the beginning, god created homies
      """
stop_words = {"a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"}
bm25_scores = {}
total_num_files = 31102

def make_hash_name(term, max_len=4):
	max_ngram = 6
	query = term.lower()[:min(max_ngram, len(term))].encode("UTF-8")
	return "{}.txt".format(hashlib.md5(query).hexdigest()[:max_len])

def get_bm25_score(document_length, num_of_doc_containing_key, keyword_freq_in_doc):
	idf = math.log(((total_num_files - num_of_doc_containing_key + 0.5) / (num_of_doc_containing_key + 0.5)) + 1)
	k1 = 1.2
	b = 0.75
	avg_len_of_docs = 25
	second_part = (keyword_freq_in_doc * (k1 + 1)) /  ((keyword_freq_in_doc + k1) * (1 - b + (b * (document_length / avg_len_of_docs))))
	return idf * second_part	

def display_results(bm25_scores):
	keys_bm25_scores = list(bm25_scores.values())
	keys_bm25_scores.sort(reverse=True)
	sorted_bm25_scores = {}
	for sorted_value in keys_bm25_scores:
		for key, list_value in bm25_scores.items():
			if list_value == sorted_value:
				sorted_bm25_scores[key] = sorted_value
	print(sorted_bm25_scores)

def get_bm25_of_ngram(txt_json, num_of_doc_containing_key):
	for left_txt, value in txt_json.items():
		book_name = left_txt.split(",")[0]
		chapter_number = left_txt.split(",")[1]
		verse_number = int(left_txt.split(",")[2])

		document_name = f"{book_name}_ch_{chapter_number}.txt"
		keyword_freq_in_doc = len(value)

		document_length = 0
		with open(f"./verses/{book_name}/{document_name}") as file:
			all_lines = file.readlines()
			print(all_lines[verse_number - 1])

	# for document, value in txt_json.items():
	# 	keyword_freq_in_doc = len(value)
	# 	document_length = 0
	# 	with open(f"./verses/{book_name}/{document_name}") as file:
	# 		total_lines = file.readlines()
	# 		for line in total_lines:
	# 			if line.split("\t")[0] == document_name:
	# 				document_length = len(line.split("\t")[1])
	# 	if not document in bm25_scores:
	# 		bm25_scores[document] = get_bm25_score(document_length, num_of_doc_containing_key, keyword_freq_in_doc)
	# 	else:
	# 		bm25_scores[document] = bm25_scores[document] + get_bm25_score(document_length, num_of_doc_containing_key, keyword_freq_in_doc)

def main():
	for keyword in re.split(r"[ \t\n]", query):
		max_ngram = 6
		keyword = keyword.strip(" \t\n0123456789.:[(<>)].,'\"‘’?--•…")[:min(max_ngram, len(keyword))]
		if not keyword.lower() in stop_words and len(keyword) != 0:
			file_name = make_hash_name(keyword.lower())
			if os.path.exists(f"./hashed_documents/{file_name}"):
				with open(f"./hashed_documents/{file_name}") as file:
					all_lines = file.readlines()
					for line in all_lines:
						ngram = line.split("\t")[0].lower()
						if ngram == keyword.lower():
							txt_json = json.loads(line.split("\t")[1])
							num_of_doc_containing_key = len(txt_json)
							get_bm25_of_ngram(txt_json, num_of_doc_containing_key)



if __name__ == "__main__":
	main()




# import os

# print(len(os.listdir("./Books/1 Thessalonians")))


# import hashlib
# print(hashlib.md5("[rebu".encode("UTF-8")).hexdigest()[:4])