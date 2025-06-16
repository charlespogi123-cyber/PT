from django.shortcuts import render
from django.http import JsonResponse
import subprocess
import time
from datetime import datetime
from .future_integrations import NetworkAPIClient

def home(request):
    return render(request, 'dashboard/home.html', {
        'title': 'Network Dashboard',
        'current_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def ping(request):
    if request.method == 'GET':
        target = request.GET.get('target', '8.8.8.8')
        try:
            # For Windows: ['ping', '-n', '4', target]
            result = subprocess.run(['ping', '-c', '4', target], 
                                  capture_output=True, 
                                  text=True,
                                  timeout=10)
            return JsonResponse({
                'status': 'success',
                'output': result.stdout,
                'error': result.stderr
            })
        except subprocess.TimeoutExpired:
            return JsonResponse({
                'status': 'error',
                'message': 'Ping request timed out'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            })
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

