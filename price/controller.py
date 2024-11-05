from django.http import JsonResponse
import requests

def coins_options():
    try: 
        response = requests.get('https://economia.awesomeapi.com.br/json/available/uniq')
        response.raise_for_status()
        data = response.json()
        key = list(data.keys())
        value = list(data.values())
        return {'keys': key, 'values': value}
    
    except requests.exceptions.HTTPError as http_err:
        return JsonResponse({"error": str(http_err)}, status=response.status_code)
    except Exception as err:
        return JsonResponse({"error": str(err)}, status=500)