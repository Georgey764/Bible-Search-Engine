import json, os, hashlib
from docx import Document 

# json_hi = {
# 	"hi": 1,
# 	"bye": 2
# }

# array = []

# array.append(f"hi\t{json.dumps(json_hi)}")
# array.append(f"hi\t{json.dumps(json_hi)}")

# # with open("test.txt", "w") as file:
# # 	file.write("hi")

# with open("test.txt", "a") as file:
# 	file.write("\n" + "\n".join(array))

# print(not "hi" in json_hi or 3 > 1)

print(hashlib.md5("justic".encode("UTF-8")).hexdigest()[:4])
# docx = Document(f"./Books/Genesis/Genesis_ch_1.docx")
# hi = [paragraph.text.split(" ") for paragraph in docx.paragraphs]
# print(hi)

# query = """
# 	beginning
# """




# keyword = [line.strip(" \t\n0123456789.:[(<>)].,'\"‘’?--•…") for line in (" ".join(query.split("\n"))).split(" ")]

# print(keyword)