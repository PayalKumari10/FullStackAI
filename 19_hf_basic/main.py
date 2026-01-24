from transformers import pipeline

pipe = pipeline(
    "image-text-to-text",
    model="google/gemma-3-4b-it"
    #  model="llava-hf/llava-1.5-7b-hf"
)

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png"},
            {"type": "text", "text": "Describe the image in detail."}
        ]
    }
]

output = pipe(messages)
print(output)





# from transformers import pipeline

# pipe = pipeline(
#     "text-generation",
#     model="google/gemma-3-4b-it"
# )

# prompt = "Describe a colorful image of parrots sitting on a tree branch."

# output = pipe(prompt, max_new_tokens=150)
# print(output[0]["generated_text"])
