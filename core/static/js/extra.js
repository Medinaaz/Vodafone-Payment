function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie != '') {
    let cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      let cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
let csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
$(document).ready(function () {
    let basketApiUrl = $(".main-marketplace-navigation").data("basket-api");

    $(".add-basket-item").on("click", function (e) {
        e.preventDefault();
        let me = $(this);
        me.addClass('disabled');
        $.ajax({
            url: basketApiUrl,
            type: "POST",
            data: {
                    product_slug: me.data("product-slug"),
                    quantity: me.data("quantity")
                },
            success: function (data) {
                me.text(Translations.added_to_basket)
                me.removeClass("btn-danger");
                me.addClass("btn-success");
                // window.location.reload();
            },
            error: function (xhr) {
                let data = jQuery.parseJSON(xhr.responseText);
                me.text(data.message);
                me.removeClass('disabled')
            }
        });
    })
    $(".apply-coupon-code").on("click", function (e) {
        e.preventDefault();
        let me = $(this);
        me.addClass('disabled');
        $.ajax({
            url: basketApiUrl,
            type: "PATCH",
            data: {
                coupon_code: me.data("coupon-code")
            },
            success: function (data) {
                window.location.reload();
            },
            error: function (xhr) {
                let data = jQuery.parseJSON(xhr.responseText);
                me.text(data.message);
                me.removeClass('disabled')
            }
        });
    })
    $('.quantity-input').change(function (e) {
        let me = $(this);
        $.ajax({
            url: basketApiUrl,
            type: "PATCH",
            data: {
                quantity: me.val(),
                basket_item_id: me.data("basket-item-id")
            },
            success: function (data) {
                window.location.reload();
            },
            error: function (xhr) {
                let data = jQuery.parseJSON(xhr.responseText);
                me.text(data.message);
            }
        });
    });
    $('.basket-delete').click(function (e) {
        let me = $(this);
        $.ajax({
            url: basketApiUrl,
            type: "DELETE",
            success: function (data) {
                window.location.reload();
            },
            error: function (xhr) {
                let data = jQuery.parseJSON(xhr.responseText);
                me.text(data.message);
            }
        });
    });
})
