function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }

const insertPost = async function(data, url_request) {
    let response = await fetch(url_request, {
      method: 'POST',
      headers : {
        'Content-Type': 'application/json',
        'X-CSRFToken' : getCookie('csrftoken'),
        'credentials' : 'same-origin',
      },
      body: JSON.stringify(data)
    })
    let responsedata = await response.json()
    if (response.ok) {
      return responsedata
    } else {
      console.log(response.status)
    }
  }

const request = async function (url_request) {
  const headers = { 
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  }
  try {
      let response = await fetch(url_request, headers)
      if (response.ok) {
        let data = await response.json()

        return data
      } else {
        console.error('retour du serveur : ', response.status)
      }
    } catch (e) {
      console.log(e)

    }
}