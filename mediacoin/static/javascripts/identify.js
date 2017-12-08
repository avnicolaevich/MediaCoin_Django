var UserIdentify = (function () {
	return {
		setCurUserIdentify: function (register_path) {
			var userIdentifyID = getCurUserIdentify("userIdentifyID");

		    if (userIdentifyID == "") {
		    	userIdentifyID = getUUID();
		    }
		    registerUUID(userIdentifyID);

		    var wrp_flag = false, cur_wlp = window.location.pathname, referral_link_path = '';
		    if (cur_wlp.indexOf('/u/') >= 0) {
		        referral_link_path = cur_wlp.substring(cur_wlp.length - 11, cur_wlp.length - 1);
		        wrp_flag = true;
            }

		    jQuery.ajax({
                type: "post",
                url: register_path,
                data: { uuid: userIdentifyID, wrp_flag: wrp_flag, referral_link_path: referral_link_path },
                success: function (data) {
                    if (data['status'] == 'success') {
                        console.log('Welcome to Mediacoin!');
                        var referral_path = ('https:' == document.location.protocol ? 'https://' : 'http://');
                        referral_path += window.location.host + '/u/' + data['referral_link_path'];
                        jQuery("nav .referral-link-path > a").text('Your referral link: ' + referral_path);
                        jQuery("nav .referral-link-path > a").attr('href', referral_path);
                        jQuery("nav .referral-link-path > span").text(data['referral_times']);
                    } else {
                        console.log(data['message']);
                    }
                }
            });

		    return true;
		}
	}
})();