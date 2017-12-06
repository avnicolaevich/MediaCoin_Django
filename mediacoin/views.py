import datetime
import braintree

from decimal import Decimal

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


# purchase gift promo code
def purchaseGiftPromoCode(request):
    if request.method == 'POST':
        uuid = request.POST.get('uuid', '')
        gift_type = request.POST.get('gift_type', '')
        gift_price = request.POST.get('gift_price', '')
        payment_nonce = request.POST.get('payment_method_nonce')

        if uuid == '' or gift_type == '' or gift_price == '':
            return JsonResponse({'status': 'failed', 'message': 'Error in ajax call!'})

        if gift_type == 'buy-for-me':
            result = braintree.Transaction.sale({
                "amount": gift_price,
                "payment_method_nonce": payment_nonce,
                "options": {
                    "submit_for_settlement": True
                },
                # "custom_fields": {
                #     "Referral_ID": uuid,
                #     "Amount": gift_price,
                #     "Type": "Buy For Me"
                # }
            })

            if result.is_success:
                referral = Referral.objects.get(referral_id=uuid)
                gift_code = GiftCode(referral_id=referral.id, type=True, amount=Decimal(gift_price))
                gift_code.updated_at = datetime.datetime.now()
                gift_code.save()

                return JsonResponse({'status': 'success', 'message': 'Purchased Gift Promo Code successfully!'})
            else:
                return JsonResponse({'status': 'failed', 'message': 'Connection error with Braintree System! Please try again!'})
        else:
            return JsonResponse({'status': 'failed', 'message': 'Error in ajax call!'})


def getClientToken(request):
    if request.method == 'POST':
        return JsonResponse({'client_token': braintree.ClientToken.generate()})

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