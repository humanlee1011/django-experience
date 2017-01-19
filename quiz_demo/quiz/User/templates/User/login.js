(function($) {
  $(document).ready(function() {
    $('#error').hide();
    $('#form').submit(function(event) {
      $ajax({
        method: "POST",
        data: $('form').serialize(),
        success: function(responseText) {
          if (responseText == "login error")
            $('#error').show();
        }
      });
      event.preventDefault();
    });
  });
})(jQuery);
