from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import requests

# Load the pre-trained model and tokenizer
model_name = "bigbird-tiny"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create an instance of the model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Define a function to generate text
def generate_text(prompt, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(inputs["input_ids"], max_length=max_length)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Define a function to generate a response from the API
def generate_response():
    url = "http://localhost:1234/v1/chat/completions"
    
    payload = {
        "model": "llama-3.2-1b-instruct",
        "messages": [
            { "role": "system", "content": "funny pirate with silly typos" },
            { "role": "user", "content": "say a word that rhymes with cat" }
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }
    
    response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
    
    if response.status_code == 200:
        response_json = response.json()
        ai_response = response_json['choices'][0]['message']['content']
        return ai_response
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    # Test the text generation function
    prompt = "Write a story about a cat."
    print("Generated text:")
    print(generate_text(prompt))

    # Test the API response function
    response = generate_response()
    print("\nAPI Response:")
    print(response)