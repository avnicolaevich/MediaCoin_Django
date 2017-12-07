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

        if (gift_type == 'gift-for-friend') {
            $('#modal-info').modal('show');
        }
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
    $('.modal-message .rem-ipt-field').focus(function () {
        $(this).removeClass('rem-ipt-require');
        $(this).addClass('focused');
    }).blur(function () {
        $(this).removeClass('focused');
    });
    $('.rem-register-but').on('click', function () {
        recipient_email = $('.rem-recipient-email').val();
        recipient_name = $('.rem-recipient-name').val();
        your_name = $('.rem-your-name').val();

        if (recipient_email == '' || recipient_name == '' || your_name == '') {
            if (recipient_email == '') {
                $('.rem-recipient-email').addClass('rem-ipt-require');
            }
            if (recipient_name == '') {
                $('.rem-recipient-name').addClass('rem-ipt-require');
            }
            if (your_name == ''){
                $('.rem-your-name').addClass('rem-ipt-require');
            }
        } else {
            recipient_message = $('.rem-recipient-message').text();
            $('.gff-descriptions').css('display', 'block');
            $('#modal-info').modal('hide');
        }
    });
});