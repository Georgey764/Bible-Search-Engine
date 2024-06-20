from flask import Flask, jsonify, json, request
from flask_cors import CORS, cross_origin
import query_chapter as QS
from docx import Document

app = Flask(__name__)
CORS(app, origins=["http:localhost:3000"])

@app.get("/read/<query>")
@cross_origin()
def get_result(query):
    return jsonify(QS.return_bm25_scores(query))

@app.get("/chapter")
@cross_origin()
def get_chapter():
    book = request.args.get('book')
    chapter = request.args.get('chapter')
    text = QS.get_chapter(book, chapter)
    return text

@app.get("/text-preview")
@cross_origin()
def get_preview_text():
    book = request.args.get('book')
    query = request.args.get('query')
    chapter = request.args.get('chapter')
    result = QS.return_preview_text(query, book, chapter)
    return result

@app.get("/keyword-indices")
@cross_origin()
def get_keyword_indices():
    book = request.args.get('book')
    query = request.args.get('query')
    chapter = request.args.get('chapter')
    result = QS.return_keyword_indices(query, book, chapter)
    return jsonify(result)

@app.get("/preview-indices")
@cross_origin()
def get_preview_indices():
    book = request.args.get('book')
    query = request.args.get('query')
    chapter = request.args.get('chapter')
    result = QS.return_preview_indices(query, book, chapter)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
