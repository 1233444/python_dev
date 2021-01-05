# http://coreyms.com/

from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html=HTML(html=source)


match = html.finjd('title', first=True)
print(match.text)
# print(html.text)
