import cohere

# Initialize Cohere client with your API key
co = cohere.Client('opKHtxN5LG2MLT9RGj2vanYfhTq4Y7TCS2qGkjPn')  # Replace with your actual API key

# List available models
models = co.list_models()
for model in models:
    print(f"Model ID: {model.id}, Model Name: {model.name}")
