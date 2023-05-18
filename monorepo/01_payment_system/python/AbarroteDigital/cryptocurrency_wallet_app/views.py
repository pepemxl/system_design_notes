from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Wallet, Transaction

# Create your views here.

@login_required
def wallet(request):
    user = request.user
    wallet = Wallet.objects.get(user=user)
    transactions = Transaction.objects.filter(wallet=wallet).order_by('-timestamp')
    context = {
        'wallet': wallet,
        'transactions': transactions,
    }
    return render(request, 'wallet.html', context)

@login_required
def send(request):
    if request.method == 'POST':
        user = request.user
        wallet = Wallet.objects.get(user=user)
        amount = request.POST.get('amount')
        recipient = request.POST.get('recipient')
        # Process the transaction and update the wallet balance
        transaction = Transaction.objects.create(wallet=wallet, amount=-amount)
        recipient_wallet = Wallet.objects.get(user__username=recipient)
        recipient_transaction = Transaction.objects.create(wallet=recipient_wallet, amount=amount)
        wallet.balance -= amount
        wallet.save()
        recipient_wallet.balance += amount
        recipient_wallet.save()
        return HttpResponse('Transaction successful')
    else:
        return render(request, 'send.html')

@login_required
def receive(request):
    user = request.user
    wallet = Wallet.objects.get(user=user)
    context = {
        'wallet': wallet,
    }
    return render(request, 'receive.html', context)