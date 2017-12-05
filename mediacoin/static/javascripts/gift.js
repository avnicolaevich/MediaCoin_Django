$(document).ready(function () {
    $('.gift-payments .payments-inputs').on('click', function () {
        $('.gift-payments .payments-inputs .gift-price').focus();
    });
    $('.gift-payments .payments .each-gift').on('click', function () {
        $(this).parent().find('.each-gift').removeClass('activated');
        $(this).addClass('activated');
        $('.payments-inputs .gift-price').val($(this).data('price'));
        $('.payments-inputs').addClass('focused');
        gift_price = $(this).data('price');
    });
    $('.gift-payments .payments-types .each-gift').on('click', function () {
        $(this).parent().find('.each-gift').removeClass('activated');
        $(this).addClass('activated');
        gift_type = $(this).data('type');
    });
    $('.gift-payments .gift-price').focus(function () {
        $('.payments-inputs').addClass('focused');
    }).blur(function () {
        var tp_val = $(this).val();
        if (tp_val == '') {
            $('.payments-inputs').removeClass('focused');
        }
        gift_price = $(this).val();
    });
});