/**
 * Created by monterola on 30/06/2017.
 */
$('.btn-delete').click(function(){
    $('<div></div>').appendTo('body')
      .html('<div><h6>Yes or No?</h6></div>')
      .dialog({
          modal: true, title: 'message', zIndex: 10000, autoOpen: true,
          width: 'auto', resizable: false,
          buttons: {
              Yes: function () {
                  doFunctionForYes();
                  $(this).dialog("close");
              },
              No: function () {
                  doFunctionForNo();
                  $(this).dialog("close");
              }
          },
          close: function (event, ui) {
              $(this).remove();
          }
    });
});