from django.shortcuts import render

def dashboard(request):
    """Starter landing page only; live complaint metrics are not implemented."""
    return render(request, "core/dashboard.html")
