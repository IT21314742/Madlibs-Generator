# Read the story from the file
with open("story.txt", "r") as f:
    story = f.read()

# Initialize a set to store unique words
words = set()
start_of_word = -1 

# Define target characters for start and end of the word
target_start = "<"
target_end = ">"

# Iterate over the story to find words between < and >
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

# Initialize a dictionary to store answers
answers = {}

# Prompt the user for input for each unique word
for word in words:
    answer = input("Enter a word for " + word + ":")
    answers[word] = answer

for words in words:
    story.replace(word, )
