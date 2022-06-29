window.onload = function () {
  

console.log('Lazyload.js is laoded!!!');

django.jQuery( document ).ready(function() {
    console.log( "doc ready!" );


    function load_data(elem) {
      django.jQuery.ajax({
        url: elem.attr('url_to_load'),
      //   context: document.body
      }).done(function(data) {
        // console.log(data)

        elem.html(data)

      });
    }

    django.jQuery( "div[lazyload_placeholder='yes']" ).each(function( index ) {
      var elem = django.jQuery( this );
      // console.log( index  + ": " + elem.attr("id") );
      //
      // console.log('Loading ur: ' + elem.attr('url_to_load'));

      load_data(elem);
    });



    django.jQuery( "div[lazyload_click='yes']" ).each(function( index ) {
      var elem = django.jQuery( this );
      console.log('Clickable lazyload ' + index  + ": " + elem.attr("id") );

      console.log('Loading ur: ' + elem.attr('url_to_load'));

      elem.click(function() {
        console.log('Clicked: ' + elem);
        load_data(elem);

      });

    });

});
}