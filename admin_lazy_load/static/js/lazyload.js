function load_data(elem) {

  elem.children("#" + elem.attr("id") + "-spinner").show()
  elem.children("#" + elem.attr("id") + "-click").hide()

  django.jQuery.ajax({
    url: elem.attr('url_to_load'),
  }).done(function(data) {
    elem.children("#" + elem.attr("id") + "-spinner").hide()
    elem.children("#" + elem.attr("id") + "-content").html(data)
  });
}



window.onload = function () {
  
  console.log('Lazyload.js is laoded!!!');

  django.jQuery( document ).ready(function() {
      console.log( "doc ready!" );

      django.jQuery( "div[lazyload_placeholder='yes']" ).each(function( index ) {

        var elem = django.jQuery( this );

        if (elem.attr('loading_type') == 'on_click') { // assign on-lick event
          elem.children("#" + elem.attr("id") + "-click").click(function() {  
            console.log('Clicked: ' + elem);
            load_data(elem);
          })
        } else {  // load immediately
          load_data(elem);
        }
      });


});
}