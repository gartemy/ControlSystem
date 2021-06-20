$(document).ready(function($) {
	$('.rules-open').click(function() {
		$('.rules-fade').fadeIn();
		return false;
	});

	$('.rules-close').click(function() {
		$(this).parents('.rules-fade').fadeOut();
		return false;
	});

	$(document).keydown(function(e) {
		if (e.keyCode === 27) {
			e.stopPropagation();
			$('.rules-fade').fadeOut();
		}
	});

	$('.rules-fade').click(function(e) {
		if ($(e.target).closest('.rules').length == 0) {
			$(this).fadeOut();
		}
	});
});