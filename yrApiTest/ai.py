import requests

def generate_response(personality, prompt):
    url = "http://localhost:1234/v1/chat/completions"
    
    payload = {
        "model": "deepseek-r1-distill-llama-8b",
        "messages": [
            {"role": "system", "content": f"You are {personality}."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }
    
    response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
    
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response received.")
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    personality = input("Enter personality: ")
    prompt = input("Enter your prompt: ")
    
    response = generate_response(personality, prompt)
    print("\nResponse:")
    print(response)
