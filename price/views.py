from django.shortcuts import render
from .controller import coins_options, caculate_value, value_fluctuation


def exchange_page(request):
    data = coins_options()
    final_value = None
    error = None
    if request.method == "POST":
        coin_now = request.POST.get('coin-now', 'USD')
        coin_new = request.POST.get('coin-new', 'BRL')
        if coin_now == 'OTHER':
            coin_now = request.POST.get('other-now', '')
        if coin_new == 'OTHER':
            coin_new = request.POST.get('other-new', '')
        if not coin_now or not coin_new:
            error = 'Selecione a moeda inicial e a final.'
        else:
            final_value, error = caculate_value(
                request.POST.get('quant-value', ''), coin_now, coin_new)
    context = {
        'keys': data['keys'],
        'finalValue': final_value,
        'error': error,
        'quantValue': request.POST.get('quant-value', '1'),
    }
    return render(request, 'exchange_page.html', context)


def home_page(request):
    coins = []
    for code, name, icon in (('USD', 'Dólar', 'dollar-symbol.png'),
                             ('EUR', 'Euro', 'euro-symbol.png'),
                             ('BTC', 'Bitcoin', 'bitcoin-symbol.png')):
        value, _ = caculate_value(1, code, 'BRL')
        coins.append({
            'code': code,
            'name': name,
            'icon': icon,
            'value': value,
            'up': value_fluctuation(code, 'BRL'),
        })
    return render(request, 'home_page.html', {'coins': coins})
