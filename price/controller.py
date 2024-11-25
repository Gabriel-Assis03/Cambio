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
    

def caculate_value(value, coinNow, coinNew):
    try:
        if value is '':
            return 'coloque um valor valido'
        response = requests.get(f'https://economia.awesomeapi.com.br/last/{coinNow}-{coinNew}')
        response.raise_for_status()
        data = response.json()
        q = list(data.values())
        value = float(value)
        ret = round(value*float(q[0]['bid']), 2)
        return ret
    
    except requests.exceptions.HTTPError as http_err:
        return JsonResponse({"error": str(http_err)}, status=response.status_code)
    except Exception as err:
        return JsonResponse({"error": str(err)}, status=500)
