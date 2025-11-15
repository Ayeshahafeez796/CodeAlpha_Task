import openai
openai.api_key = "YOUR_API_KEY_HERE"
def chat_with_gpt(prompt):
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]


        
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            
            break
        gpt_response = chat_with_gpt(user_input)
        print("chatbot: ", gpt_response)



