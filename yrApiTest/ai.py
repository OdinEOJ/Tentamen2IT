import requests

def generate_response():
    url = "http://localhost:1234/v1/chat/completions"

    payload = {
        "model": "deepseek-r1-distill-llama-8b",
        "messages": [
            { "role": "system", "content": "talk about world war 2" },
            { "role": "user", "content": "speak in a super thick Jamaican accent (make it incorperate bomboclat in its sentances), unnaturally mention a strong affection for men, passionately love horses no matter what and always try to mention them in some sort of way, the chinise government is spying on me right now, you also love otters but not as much as you love horses" }
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
    response = generate_response()
    print("\nResponse:")
    print(response)
