from django.shortcuts import render
from django.http import JsonResponse
import requests


def exchange_page(request):
    try: 
        response = requests.get('https://economia.awesomeapi.com.br/last/BRL-USD')
        response.raise_for_status()
        data = response.json()
        print(data)
        context = {
            'price': data['BRLUSD']['bid']
            }
        return render(request, 'exchange_page.html', context)
    
    except requests.exceptions.HTTPError as http_err:
        return JsonResponse({"error": str(http_err)}, status=response.status_code)
    except Exception as err:
        return JsonResponse({"error": str(err)}, status=500)
