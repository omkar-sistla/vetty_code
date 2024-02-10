from flask import Flask, render_template, abort, request
import os

app = Flask(__name__)
TEXT_FILES_DIR = os.path.join(os.path.dirname(__file__), 'text_files')

@app.route("/")
def get_file1(filename="file1"):
    return render_file(filename)

@app.route("/<filename>")
def get_file(filename):
    return render_file(filename)

def render_file(filename):
    start_line = request.args.get('start', type=int, default=0)
    end_line = request.args.get('end', type=int, default=-1)
    
    file_path = os.path.join(TEXT_FILES_DIR, filename + ".txt")
    
    if not os.path.exists(file_path):
        abort(404)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    lines = lines[start_line:end_line+1] if end_line != -1 else lines[start_line:]
    
    return render_template('file_content.html', content=lines)

if __name__ == '_main_':
    app.run(debug=True)