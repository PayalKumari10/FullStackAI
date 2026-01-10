import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
text = "Hey There! My name is Payal Kumari"

tokens = enc.encode(text)
print("Tokens:", tokens)

# Tokens: [25216, 3274, 0, 3673, 1308, 382, 11961, 280, 81689, 1683]

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 11961, 280, 81689, 1683])
print("Decoded", decoded)
