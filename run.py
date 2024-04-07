from flask import Flask, render_template, request
import io
import tokenize
import os
import sys
import platform
import ast
import random
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    code = request.form['code']
    obfuscated_code = obfuscate_code(code)
    return obfuscated_code

def obfuscate_code(code):
    def remove_docs(source):
        io_obj = io.StringIO(source)
        out = ""
        prev_toktype = tokenize.INDENT
        last_lineno = -1
        last_col = 0
        for tok in tokenize.generate_tokens(io_obj.readline):
            token_type = tok[0]
            token_string = tok[1]
            start_line, start_col = tok[2]
            end_line, end_col = tok[3]
            if start_line > last_lineno:
                last_col = 0
            if start_col > last_col:
                out += (" " * (start_col - last_col))
            if token_type == tokenize.COMMENT:
                pass
            elif token_type == tokenize.STRING:
                if prev_toktype != tokenize.INDENT:
                    if prev_toktype != tokenize.NEWLINE:
                        if start_col > 0:
                            out += token_string
            else:
                out += token_string
            prev_toktype = token_type
            last_col = end_col
            last_lineno = end_line
        out = '\n'.join(l for l in out.splitlines() if l.strip())
        return out

    def do_rename(pairs, code):
        for key in pairs:
            code = re.sub(fr"\b({key})\b", pairs[key], code, re.MULTILINE)
        return code

    def rename_code(code):
        used = set()
        pairs = {}

        parsed = ast.parse(code)
        # Lấy ra tất cả các hàm và lớp
        funcs = {
            node for node in ast.walk(parsed) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        classes = {
            node for node in ast.walk(parsed) if isinstance(node, ast.ClassDef)
        }
        args = {
            node.id for node in ast.walk(parsed) if isinstance(node, ast.Name) and not isinstance(node.ctx, ast.Load)
        }
        attrs = {
            node.attr for node in ast.walk(parsed) if isinstance(node, ast.Attribute) and not isinstance(node.ctx, ast.Load)
        }

        # Fake tên  hàm
        for func in funcs:
            if func.name == "__init__":
                continue
            newname = "__x" + "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") for i in range(20))
            while newname in used:
                newname = "__x" + "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") for i in range(20))
            used.add(newname)
            pairs[func.name] = newname

        # Fake tên lớp
        for _class in classes:
            newname = "__x" + "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") for i in range(20))
            while newname in used:
                newname = "__x" + "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") for i in range(20))
            used.add(newname)
            pairs[_class.name] = newname

        # Fake tên biến
        for arg in args:
            newname = "__x" + "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") for i in range(20))
            while newname in used:
                newname = "WsOBFx" + "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") for i in range(20))
            used.add(newname)
            pairs[arg] = newname

        # Fake thuộc tính
        for attr in attrs:
            newname = join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") for i in range(20))
            while newname in used:
                newname = "__x" + "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") for i in range(20))
            used.add(newname)
            pairs[attr] = newname

        string_regex = r'("[^"\\]*(?:\\.[^"\\]*)*"|\'[^\'\\]*(?:\\.[^\'\\]*)*\')'

        original_strings = re.finditer(string_regex, code, re.MULTILINE)
        originals = []

        for matchNum, match in enumerate(original_strings, start=1):
            originals.append(match.group())

        placeholder = os.urandom(16).hex()
        code = re.sub(string_regex, f"'{placeholder}'", code, 0, re.MULTILINE)

        for i in range(len(originals)):
            for key in pairs:
                originals[i] = re.sub(r"({.*)(" + key + r")(.*})", "\\1" + pairs[key] + "\\3", originals[i], re.MULTILINE)

        while True:
            found = False
            code = do_rename(pairs, code)
            for key in pairs:
                if re.findall(fr"\b({key})\b", code):
                    found = True
            if found == False:
                break

        replace_placeholder = r"('|\")" + placeholder + r"('|\")"
        for original in originals:
            code = re.sub(replace_placeholder, original, code, 1, re.MULTILINE)

        return code

    obfuscated_code = rename_code(remove_docs(code))
    return obfuscated_code

if __name__ == '__main__':
    app.run(debug=True)
