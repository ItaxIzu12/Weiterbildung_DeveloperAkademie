import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Chatbot

# Create your views here.


@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        review = Chatbot.objects.create(
            firstName=data.get("firstName"),
            lastName=data.get("lastName"),
            message=data.get("message"),
        )
        return JsonResponse({
            "id": review.id,
            "firstName": review.firstName,
            "lastName": review.lastName,
            "message": review.message,
        }, status=201)

    if request.method == "GET":
        reviews = list(Chatbot.objects.values("id", "firstName", "lastName", "message", "created_at"))
        return JsonResponse(reviews, safe=False)

    return JsonResponse({"error": "Methode nicht erlaubt"}, status=405)
