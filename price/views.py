from django.shortcuts import render
from .controller import coins_options, caculate_value


def exchange_page(request):
    data = coins_options()
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
    return render(request, 'home_page.html')

