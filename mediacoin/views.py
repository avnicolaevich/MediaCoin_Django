import datetime

from mediacoin.models import Transaction, Referral, GiftCode, GiftPrice

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

# index view page
def index(request):
	return render(request, 'mediacoin/index.html')

# demo view page
def demo(request):
	return render(request, 'mediacoin/demo.html')

# purchase gift promo code page
def purchaseGiftCard(request):
    gift_prices = GiftPrice.objects.all()

    return render(request, 'mediacoin/purchase-gift.html', {'gift_prices': gift_prices})


# register Referral ID if not exists
def registerUUID(request):
	if request.method == 'POST':
		uuid = request.POST.get('uuid', '')

		if uuid == '':
			return JsonResponse({'status': 'failed', 'message': 'UUID is empty!'})

		if Referral.objects.filter(referral_id=uuid).exists():
			referral = Referral.objects.get(referral_id=uuid)
			referral.updated_at = datetime.datetime.now()
		else:
			referral = Referral(referral_id=uuid)
		referral.save()

		return JsonResponse({'status': 'success'})