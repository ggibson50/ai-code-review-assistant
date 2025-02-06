import openai
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .security import security_scan
from .performance import performance_analysis
from .models import CodeSnippet

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def analyze_code(request):
    user = request.user
    code_content = request.data.get('code', '')

    if not code_content:
        return Response({"error": "No code provided."}, status=400)

    # AI Code Review
    review_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that reviews code for best practices."},
            {"role": "user", "content": f"Review this code: {code_content}"}
        ]
    )
    review_analysis = review_response['choices'][0]['message']['content']

    # Security Scan
    security_analysis = security_scan(code_content)

    # Performance Optimization
    performance_feedback = performance_analysis(code_content)

    # Store in database
    snippet = CodeSnippet.objects.create(
        user=user,
        content=code_content,
        analysis=f"Review:
{review_analysis}

Security:
{security_analysis}

Performance:
{performance_feedback}"
    )

    return Response({
        "review": review_analysis,
        "security": security_analysis,
        "performance": performance_feedback
    })
    