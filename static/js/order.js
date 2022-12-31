$(function () {
    var loadForm =function () {
    console.log('item-order')
    var btn = $(this);
    $.ajax({
      
      url:btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-cart").modal("show");
        console.log("hello")
      },
      success: function (data) {
        $("#modal-cart .modal-content").html(data.html_form);
      }
    });
    };


// order product
$("#placeorder").on("click", ".js-order-item", loadForm);
});