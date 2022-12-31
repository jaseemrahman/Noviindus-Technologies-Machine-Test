$(function () {
      var loadForm =function () {
      console.log('item-delete')
      var btn = $(this);
      $.ajax({
        
        url:btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-menu").modal("show");
        },
        success: function (data) {
          $("#modal-menu .modal-content").html(data.html_form);
        }
      });
      };

  // Delete item
  $("#menu-table").on("click", ".js-delete-item", loadForm);
});
  
