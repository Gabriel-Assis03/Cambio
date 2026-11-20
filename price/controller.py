import requests

API = 'https://economia.awesomeapi.com.br'
TIMEOUT = 8


def coins_options():
    """Lista de moedas disponiveis. Em caso de erro devolve lista vazia."""
    try:
        response = requests.get(f'{API}/json/available/uniq', timeout=TIMEOUT)
        response.raise_for_status()
        return {'keys': sorted(response.json().keys())}
    except (requests.RequestException, ValueError):
        return {'keys': []}


def caculate_value(value, coinNow, coinNew):
    """Converte `value` de coinNow para coinNew.

    Devolve (resultado, erro): um dos dois e sempre None.
    """
    try:
        if value in ('', None):
            return None, 'Coloque um valor válido.'
        value = float(value)
        response = requests.get(f'{API}/last/{coinNow}-{coinNew}', timeout=TIMEOUT)
        if response.status_code == 404:
            return None, (f'A conversão de {coinNow} para {coinNew} não foi '
                          'encontrada. Selecione outra opção.')
        response.raise_for_status()
        quote = list(response.json().values())[0]
        return round(value * float(quote['bid']), 2), None
    except ValueError:
        return None, 'Coloque um valor válido.'
    except (requests.RequestException, KeyError, IndexError):
        return None, 'Não foi possível consultar a cotação agora. Tente de novo.'


def value_fluctuation(coinNow, coinNew):
    """True se subiu, False se caiu, None se nao foi possivel saber."""
    try:
        response = requests.get(f'{API}/json/daily/{coinNow}-{coinNew}/2', timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()
        return float(data[0]['bid']) >= float(data[1]['bid'])
    except (requests.RequestException, KeyError, IndexError, ValueError):
        return None
