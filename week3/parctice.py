import re

texts = ["Hello    World"
         , "Python    is great", "No extra   spaces please"]

# Normalize spaces
normalized = list(map(lambda t: re.sub(r'\s+', ' ', t), texts))
print(normalized)  # ['Hello World', 'Python is great', 'No extra spaces please']