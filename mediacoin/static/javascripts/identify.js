var UserIdentify = (function () {
	return {
		setCurUserIdentify: function () {
			var userIdentifyID = getCurUserIdentify("userIdentifyID");
		    if (userIdentifyID != "") {
		        console.log('Welcome to MediaCoin!');
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