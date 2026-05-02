import json
from django.shortcuts import render
from .models import Payment

def dashboard_view(request):
    payments = Payment.objects.select_related('payer').all()
    
    chart_data =[]
    for p in payments:
        chart_data.append({
            'date': p.pay_date.strftime("%Y-%m-%d %H:%M"),
            'amount': float(p.amount), 
            'client_name': f"{p.payer.first_name} {p.payer.last_name}"
        })
    
    context = {
        'chart_data_json': json.dumps(chart_data)
    }
    return render(request, 'payments/index.html', context)