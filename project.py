with open("story.txt", "r") as f:
    story = f.read()

words = []

for i, char in enumerate(story):