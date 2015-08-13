var mouseIsInside = false;

$(document).ready(function() {
	$('.notif-field').hover(function(){ 
		mouseIsInside=true; 
	}, function(){ 
		mouseIsInside=false; 
	});

	$('.panel').slideUp(0);
	$('.pull-me').click(function() {
		$('.panel').slideToggle('slow');
	});

	$('body').click(function() {
		if (!mouseIsInside) {
			$('.panel').slideUp('slow');
		};
	});
});