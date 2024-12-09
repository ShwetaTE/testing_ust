from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .openai_service import ask_openai


@csrf_exempt
def bot_handler(request):
    if request.method == 'POST':
        
        try:
            # Log the incoming request body
            print(f"Request body: {request.body.decode('utf-8')}")

            # Parse the incoming Teams message
            data = json.loads(request.body)
            user_message = data.get('text')
            print(f"Received user message: {user_message}")

            # Get response from OpenAI
            openai_response = ask_openai(user_message)
            print(f"OpenAI response: {openai_response}")

            # Craft a simple text response for Web Chat
            response_message = {
                "type": "message",
                "text": openai_response
            }
            print(f"Sending response: {response_message}")

            return JsonResponse(response_message)
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)

# def create_adaptive_card_response(content):
#     print("content",content)
#     return {
#         "type": "message",
#         "attachments": [
#             {
#                 "contentType": "application/vnd.microsoft.card.adaptive",
#                 "content": {
#                     "type": "AdaptiveCard",
#                     "version": "1.3",
#                     "body": [
#                         {"type": "TextBlock", "text": content}
#                     ]
#                 }
#             }
#         ]
#     }

