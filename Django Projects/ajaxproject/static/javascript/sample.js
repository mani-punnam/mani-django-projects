/*function call(){
  var xhttp=new  XMLHttpRequest();
  xhttp.onreadystatechange=function() {
    if(this.readyState==4 && this.status==200) {
      document.getElementById('demo').innerHTML=this.responseText
    }
  }
  xhttp.open("GET","sample.txt",true)
  xhttp.send()
}
$('input#id_name').keyup(
  function(event) {
    if((event.which>=48 && event.which<=57) || (event.which>=65 && event.which<=90) || (event.which>=97 && event.which<=122)) {
      alert('hello')
    var name=$(this).val()
    $.ajax(
      {
        url:'/test',
        data:{
          'name':name
        },
        dataType:'json',
        success:function(data){
          if(data.is_taken){
            alert('name already exists')
          }
        }
      }
    )
  }
  }
)*/

//By using GET method in javascript
/*function get() {
  var xhr=new XMLHttpRequest()
  xhr.onreadystatechange=function() {
    if(this.readyState==4 && this.status==200) {
      obj=JSON.parse(this.responseText)
      document.getElementById('demo').innerHTML=obj['is_taken']
    }
  }
  name=$('input#id_name').val()
  console.log(name)
  xhr.open('GET','/test?name='+name,true)
  xhr.send()
}
var obj=document.querySelector('input#id_name')
obj.addEventListener('keyup',get)
*/
//By using POST method in jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});
/*$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        *///if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        /*    // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});*/
function get() {
  var name=$('input#id_name').val()
  $.ajax({
    url:'/test/',
    dataType:'json',
    type:'POST',
    data:{
      'name':name
    },
    success:function(data){
      $('input#id_name').val('')
      $('#demo').text(data.is_taken)
    }
  })
}

//By using POST method in JavaScript
/*function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function get(){
  var xhr=new XMLHttpRequest()
  xhr.onreadystatechange=function() {
    if(this.readyState==4 && this.status==200){
      $('#demo').text(this.responseText)
      console.log(this.getAllResponseHeaders())
    }
  }
  var name=$('input#id_name').val()
  xhr.open('POST','/test/',true)
  xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'))
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
  xhr.send('name='+name)
}
var obj=document.querySelector('input#id_name')
obj.addEventListener('keyup',get)
*/
