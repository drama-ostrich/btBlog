// tits.js
var $container = null;

function resizeMe(){
    var preferredWidth = 1650;  
    
    var displayWidth = $(window).width();
    var percentage = displayWidth / preferredWidth;
    
    // h1
    var fontsize = 50;
    var newFontSize = Math.floor(fontsize * percentage) - 1;
    if (newFontSize < 20){newFontSize = 20;} // Minimum size of 20
    $("h1.resize-font").css("font-size", newFontSize);
    
    // h2
    fontsize = 25;
    newFontSize = Math.floor(fontsize * percentage) - 1;
    if (newFontSize < 12){newFontSize = 12;} // Minimum size of 12
    $("h2.resize-font").css("font-size", newFontSize);
    
    // distance from bottom
    var initBottom = 200;
    var newBottom = Math.floor(initBottom * percentage) - 1;
    if (newBottom < 70){newBottom = 70;}
    $("#ep-slide-text").css("bottom", newBottom);
    
    
    
}

                                                    // jquery ready
$(document).ready(function(){
    // init isotope
//    $container = $('#i-container');
//    $container.isotope({
//      // options
//      itemSelector: '.i-box',
//      layoutMode: 'masonry',
//      masonry: {
//        columnWidth: 60,
//        gutter: 5
//      }
//
//    });

    
    // Make images bigger on click
//    $(".i-box img").click(function(){
//      $(this).toggleClass("entry-image-click");
//      $container.isotope('layout');
//    });
    
    // Isotope sort on top nav click
//    $('.head-filter a').click(function () { // handle sort button function actions and css changes
//            // get href attribute, minus the '#'
//            var filterType = $(this).attr('href').slice(1);
//            if (filterType == 'all'){
//              $container.isotope({ filter: '.i-box' });
//            }
//            else {
//              $container.isotope({ filter: '.' + filterType });
//            }
//            return false;
//    });

    // Do resizy stuff on resize
    $(function() {
    $(window).bind('resize', function()
    {
        resizeMe();
        }).trigger('resize');
    });
    
    // Accordians for lyric boxes
    $('.entry-lyrics .accordian-title h2').click(function(e){
        $(this).parent('.accordian-title').toggleClass('lyrics-hide');
    });

});
                                                    // end of jquery ready

    
$(window).load(function(){
    //$container.isotope('layout');
    
    $(".img-load").each(function(){
        $imgContainer = $(this);
        url = $imgContainer.data("imgsrc");
        $imgContainer.html('<img id="ep-img" src="' + url +'" alt="" >');
        //$.get(url).done(function( data ) {
        //    $imgContainer.html(data);
        //});
    });
    
});                                                 

