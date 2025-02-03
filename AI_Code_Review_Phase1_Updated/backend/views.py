import openai
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CodeSnippet

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def analyze_code(request):
    user = request.user
    code_content = request.data.get('code', '')

    if not code_content:
        return Response({"error": "No code provided."}, status=400)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that reviews code for best practices, security, and optimization."},
            {"role": "user", "content": f"Review this code: {code_content}"}
        ]
    )

    ai_analysis = response['choices'][0]['message']['content']
    snippet = CodeSnippet.objects.create(user=user, content=code_content, analysis=ai_analysis)

    return Response({"analysis": ai_analysis})
    