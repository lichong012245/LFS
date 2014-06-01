$(document).ready(function() {
    var mainCarousel = $('#main-carousel');

    if (mainCarousel.length) {
        var animationInProgress = false;
        var carouselWrapper = $('.carousel-wrapper', mainCarousel);
        var slides = $('.inner-box', carouselWrapper);
        var currentSlide = slides.filter('.active');
        var hiddenCSS = {
            opacity: 0,
            height: 0,
            top: '100%'
        };
        var visibleCSS = {
            height: '100%',
            opacity: 1
        };
        var timer;

        if(!currentSlide.length) {
            currentSlide = slides.first();
        }

        var hideElements = function(elementsToHide) {
            elementsToHide.animate(hiddenCSS, 500);
            elementsToHide.removeClass('active');
            elementsToHide.each(function(index, element) {
                $('a[href=#'+$(element).attr('id')+']').removeClass('active');
            });
        };
        var showElement = function(elementToShow) {
            if (animationInProgress) {
                return;
            }
            animationInProgress = true;
            elementToShow.queue(function() {
                $(this).css('top', '0%').animate(visibleCSS, 500);

                elementToShow.addClass('active');
                $('a[href=#'+elementToShow.attr('id')+']').addClass('active');
                hideElements(elementToShow.siblings());
                animationInProgress = false;
                $(this).dequeue();
            });
        };
        var showNextElement = function() {
            var current_slide = slides.filter('.active');
            if(!current_slide.length) {
                curren_slide = slides.last();
            }
            var next_slide = current_slide.next('.inner-box');
            if(!next_slide.length) {
                next_slide = slides.first();
            }
            return showElement(next_slide);
        };
        var clearCarouselTimer = function() {
            if (timer) {
                clearInterval(timer);
            }
        };
        var createCarouselTimer = function() {
            clearCarouselTimer();
            timer = setInterval(showNextElement, 5000);
        };

        carouselWrapper.mouseenter(function(e) {
            clearCarouselTimer();
        }).mouseleave(function(e) {
            createCarouselTimer();
        });

        $('.carousel-menu, .carousel-navigation').on('click', 'a', function(e) {
            clearCarouselTimer();
            e.preventDefault();
            e.stopPropagation();
            var $elementToShow = $($.find($(this).attr('href'))[0]);
            showElement($elementToShow);
            createCarouselTimer();
        });

        slides.css('position', 'absolute').css(hiddenCSS);
        currentSlide.css('top', '0%').css(visibleCSS);
        createCarouselTimer();
    }
});
