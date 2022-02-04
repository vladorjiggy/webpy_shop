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

function deleteProduct(e, a){
    e.preventDefault()
    let token = a.children[1].value
    let url = '/products/show/'+a.getElementsByClassName('product_id')[0].value+'/'
    $.ajax({
        type: "DELETE",
        url: url,
        headers: {'X-CSRFToken': token},
        success: function()
        {
          location.href = '/products/show'
        }
    });
    
}

function deleteReview(e, a){
    e.preventDefault()
    let token = a.children[1].value
    let url = '/products/reviews/detail/'+a.getElementsByClassName('review_id')[0].value+'/'
    $.ajax({
        type: "DELETE",
        url: url,
        headers: {'X-CSRFToken': token},
        success: function()
        {
          location.href = '/products/reviews/show/' + a.getElementsByClassName('review_id')[0].value + '/'
        }
    });
    
}