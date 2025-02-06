import openai

def performance_analysis(code):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that provides performance optimization suggestions for code."},
            {"role": "user", "content": f"Analyze this code for performance improvements: {code}"}
        ]
    )
    return response['choices'][0]['message']['content']
    