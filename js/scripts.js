$(document).ready(function(){
	$('a[href^="#"]').bind('click.smoothscroll',function (e) {
	    e.preventDefault();
	 
	    var target = this.hash,
	    $target = $(target);
	 
	    $('html, body').stop().animate({
	        'scrollTop': $target.offset().top
	    }, 500, 'swing', function () {
	        window.location.hash = target;
	    });
	});
});

$(function(){
  $("#introduction h1").typed({
    strings: ["Hello, my name is Lisa Huang"],
    typeSpeed: 30
  });
});