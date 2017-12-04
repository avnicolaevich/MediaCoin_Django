$(document).ready(function(){
	var ele_heights = [0, 0, 0];

	function getMaxHeights() {
		var max_height = 0, i = 0;
		for (i=0; i<ele_heights.length; i++) {
			if (max_height < ele_heights[i]) {
				max_height = ele_heights[i];
			}
		}
		return max_height;
	}

	$(window).on('resize', function(){
		var viewportWidth = $(window).width();
		if (viewportWidth > 767) {
			$('.section.features .each-feature').each(function (index, element) {
				var left_content = $(element).find('div.float-left').outerHeight();
				var right_content = $(element).find('div.float-right').outerHeight();

				if (left_content > right_content) {
					$(element).find('div.float-right').css('padding-top', (left_content - right_content) / 2 + 'px');
				} else {
					$(element).find('div.float-left').css('padding-top', (right_content - left_content) / 2 + 'px');
				}
			});
		} else {
			$('.section.features .each-feature').each(function (index, element) {
				$(element).find('div.float-right').css('padding-top', '10px');
				$(element).find('div.float-left').css('padding-top', '10px');
			});
		}
		if (viewportWidth > 768) {
			/* sort goal element by bottom */
			// var max_height = 0;
			// $('.ico-stretch-goals .each-goal').each(function (index, element) {
			// 	var height = $(element).outerHeight();
			// 	if (max_height < height) {
			// 		max_height = height;
			// 	}
			// 	if ((index+1) % 3 === 0) {
			// 		$(element).css('margin-top', (max_height - height) + 'px');
			// 		var prev_element = $(element).prev(); $(prev_element).css('margin-top', (max_height - $(prev_element).outerHeight()) + 'px');
			// 		prev_element = $(element).prev().prev(); $(prev_element).css('margin-top', (max_height - $(prev_element).outerHeight()) + 'px');
			// 		max_height = 0;
			// 	}
			// });
		} else {
			$('.ico-stretch-goals .each-goal').each(function (index, element) {
				$(element).css('margin-top', '0px');
			});
		}

		$('.hiring .real-content .each-hire').each(function (index, element) {
			var ele_span = $(element).find('label');
			$(ele_span).css('margin-top', ($(element).outerHeight() - $(ele_span).outerHeight()) / 2 + 'px');
		});
	}).trigger('resize');
});