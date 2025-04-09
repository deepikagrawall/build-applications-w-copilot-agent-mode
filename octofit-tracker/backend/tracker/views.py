from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "url": "https://ideal-waddle-vjrvwrqgj9vhw4jw-8000.app.github.dev"
    })