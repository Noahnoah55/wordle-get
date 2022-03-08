import requests

# If NYT ever changes their code, these could change
# TODO: Automatically find the javascript file (even if the numbers after main change)
# TODO: Automatically find the name of the list (even if the minified name changes)
__url__ = "https://www.nytimes.com/games/wordle/main.bfba912f.js"
__listName__ = "Ma"

js = requests.get(__url__)

listStart = js.content.find(b'Ma=')
listEnd = js.content.find(b']', listStart)

print(js.content[listStart:listEnd+1])
