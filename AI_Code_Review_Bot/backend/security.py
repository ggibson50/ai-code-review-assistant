import openai

def security_scan(code):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that scans code for security vulnerabilities."},
            {"role": "user", "content": f"Scan this code for security issues: {code}"}
        ]
    )
    return response['choices'][0]['message']['content']
    