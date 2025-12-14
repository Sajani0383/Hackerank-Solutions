# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

parser = MyHTMLParser()

n = int(input())
html = ""
for _ in range(n):
    html += input() + "\n"

parser.feed(html)