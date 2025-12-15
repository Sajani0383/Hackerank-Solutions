import re

n = int(input())
html = ""

for _ in range(n):
    html += input() + "\n"

# Remove comments
html = re.sub(r'<!--[\s\S]*?-->', '', html)

# Match tags (normal + self-closing)
tag_pattern = re.compile(r'<\s*(\w+)(.*?)\s*/?>', re.DOTALL)

# Match attributes (allow hyphens, single/double quotes)
attr_pattern = re.compile(r'([\w-]+)\s*=\s*(?:"([^"]*)"|\'([^\']*)\')')

for tag, attrs in tag_pattern.findall(html):
    print(tag)
    for attr, v1, v2 in attr_pattern.findall(attrs):
        print("->", attr, ">", v1 if v1 else v2)