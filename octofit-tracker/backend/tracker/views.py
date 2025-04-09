from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "url": "https://build-applications-w-copilot-agent-mode-8000.app.github.dev"
    })