'use strict'

function addToCart(e, a) {
    e.preventDefault()
    let token = a.children[1].value
    let url = '/products/show/'+a.getElementsByClassName('product_id')[0].value+'/'
    $.ajax({
        type: "POST",
        url: url,
        data: {
            csrfmiddlewaretoken: token
        },
        success: function()
        {
          location.reload()
        }
    });
}