/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
  evt.preventDefault(); 

  response = await axios({
    url: '/api/get-lucky-num',
    method: 'POST',
    data: {'name': $("#name").val(),
           'year': $("#year").val(),
           'email': $("#email").val(),
           'color': $("#color").val()}
  })
  
  handleResponse(response.data);
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(res) {
  if (Object.keys(res.errors).length !== 0) {
    console.log(res.errors);
    if (res.errors.name) 
      $('#name-err').text(res.errors.name)
    if (res.errors.year)
      $('#year-err').text(res.errors.year)
    if (res.errors.email)
      $('#email-err').text(res.errors.email)
    if (res.errors.color)
      $('#color-err').text(res.errors.color)
  }
  else {
    $('#lucky-form')[0].reset();
    $('b').empty();
    let luckyResult = `Your lucky number is ${res.num.num} ${res.num.fact}<br>
                       Your birth year ${res.year.num} fact is ${res.year.fact}`;
    let $p = $('<p></p>').text(luckyResult);
    $('#lucky-results').append($p);
  }
}

$('#lucky-form').on("submit", processForm);
