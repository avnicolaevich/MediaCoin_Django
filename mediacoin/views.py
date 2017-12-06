import datetime
import braintree

from decimal import Decimal

from mediacoin.models import Transaction, Referral, GiftCode, GiftPrice, GiftRecipient

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail

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

            if gift_type == 'buy-for-me':
                gift_code = GiftCode(referral_id=referral.id, type=True, amount=Decimal(gift_price))
                gift_code.updated_at = datetime.datetime.now()
                gift_code.save()

                return JsonResponse({'status': 'success', 'message': 'Purchased Gift Promo Code successfully!'})
            else: # gift for friend
                gift_code = GiftCode(referral_id=referral.id, type=False, amount=Decimal(gift_price))
                gift_code.updated_at = datetime.datetime.now()
                gift_code.save()

                recipient_email = request.POST.get('recipient_email')
                recipient_name = request.POST.get('recipient_name')
                recipient_message = request.POST.get('recipient_message')
                your_name = request.POST.get('your_name')

                message = 'Hi, <b>' + recipient_name + '</b>!' + '<br/>Just received Gift Code is purchased over <b>$' + gift_price + '</b> from ' + your_name + '.<br/>' + '*** Gift Promo Code ***<br/>' + gift_code.get_code()
                if recipient_email != '':
                    message += '<br/><br/>' + your_name + '`s message: ' + recipient_message
                message += '<br/><br/><br/>MediaCoin Security Team'

                send_mail(
                    'MediaCoin Gift Code from ' + your_name,
                    message,
                    'security@mediacoin.com',
                    [recipient_email],
                    fail_silently=False
                )

                gift_recipient = GiftRecipient(gift_code_id=gift_code.id, email=recipient_email, name=recipient_name)

                return JsonResponse({'status': 'success', 'message': 'Sent Gift Promo Code to ' + recipient_name + ' successfully!'})
        else:
            return JsonResponse({'status': 'failed', 'message': 'Connection error with Braintree System! Please try again!'})


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