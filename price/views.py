from django.shortcuts import render
from .controller import coins_options, caculate_value, value_fluctuation


def exchange_page(request):
    data = coins_options()
    finalValue = ''
    if request.method == "POST":
        coinNow = request.POST['coin-now']
        coinNew = request.POST['coin-new']
        if coinNow == 'OTHER':
            coinNow = request.POST['other-now']
        if coinNew == 'OTHER':
            coinNew = request.POST['other-new']
        finalValue = caculate_value(
            request.POST['quant-value'],
            coinNow,
            coinNew
            )
    context = {
            'keys': data['keys'],
            'finalValue': finalValue
        }
    return render(request, 'exchange_page.html', context)

def home_page(request):
    context={
        'dolar': caculate_value(1,'USD','BRL'),
        'euro': caculate_value(1,'EUR','BRL'),
        'bitcoin': caculate_value(1,'BTC','BRL'),
        'dolar_fluctuation': value_fluctuation('USD','BRL'),
        'euro_fluctuation': value_fluctuation('EUR','BRL'),
        'bitcoin_fluctuation': value_fluctuation('BTC','BRL')
    }
    return render(request, 'home_page.html', context)
