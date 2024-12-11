from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


@login_required
def dashboard(request):
    # template_name = 'dashboard.html'
    # return render(request, template_name)
    context = {
        "sales_this_week": {
            "amount": 45385,
            "growth": 12.5,
        },
        "latest_transactions": [
            {"transaction": "Payment from Bonnie Green", "date": "Apr 23, 2021", "amount": 2300},
            {"transaction": "Payment refund to #00910", "date": "Apr 23, 2021", "amount": -670},
            {"transaction": "Payment failed from #087651", "date": "Apr 18, 2021", "amount": 234},
        ],
        "stats": {
            "new_products": {"count": 2340, "growth": 14.6},
            "visitors": {"count": 5355, "growth": 32.9},
            "user_signups": {"count": 385, "growth": -2.7},
        },
        "latest_customers": [
            {"name": "Neil Sims", "email": "email@windster.com", "spending": 320},
            {"name": "Bonnie Green", "email": "email@windster.com", "spending": 3467},
            {"name": "Michael Gough", "email": "email@windster.com", "spending": 67},
        ],
    }
    return render(request, "dashboard.html", context)
