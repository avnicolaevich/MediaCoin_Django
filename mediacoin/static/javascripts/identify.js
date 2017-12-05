var UserIdentify = (function () {
	return {
		setCurUserIdentify: function () {
			var userIdentifyID = getCurUserIdentify("userIdentifyID");

		    if (userIdentifyID != "") {
		    	jQuery.ajax({
					type: "post",
					url: "/register-uuid",
					data: { uuid: userIdentifyID },
					success: function (data) {
						if (data['status'] == 'success') {
							console.log('Welcome to Mediacoin!');
						} else {
							console.log(data['message']);
						}
					}
				});
		    } else {
		        var d = new Date();
			    d.setTime(d.getTime() + (365*24*60*60*1000));
			    var expires = "expires="+ d.toUTCString();
		    	document.cookie = 'userIdentifyID' + "=" + getUUID()  + ";" + expires + ";path=/";
		    }

		    return true;
		}
	}
})();