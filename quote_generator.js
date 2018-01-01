/*When page had loaded*/
$(document).ready(function(){
  /*Quotes read from csv file into array*/
  var quotes = [];
  /*Current quote stored in this variable*/
  var currentQuote = "Confine yourself to the present";
  /*Load qoutes from csv file using AJAX*/
  $.ajax({
    url: 'quotes.csv',
    dataType: 'text',
    success: function(data){
    /*If successfully loaded split quotes on delimiter*/
    quotes = data.split("/");
  }})
  /*Load default quote to page*/
  $("#quote").text(currentQuote);
  /*When new quote button clicked, choose random quote from array*/
  $('#refresh').click(function(){
    rand = Math.floor(Math.random() * quotes.length)
    currentQuote = quotes[rand];
    $('#quote').text(currentQuote);
  });
  /*When user clicks tweet button, attempt to open new window where user can tweet quote*/
  $('.tweet').click(function(){
    var tLink = "https://twitter.com/intent/tweet?text="
    tLink += ('"' + currentQuote + '"' + " - Marcus Aurelius...quote courtesy of Goodreads.com");
    /*Check for character limit*/
    if (tLink.length > 280){
      alert("Marcus Aurelius lived before twitter, and unfortunately did not confine his wise words to 280 characters....this quote is too big to tweet")
    } else {
      window.open(tLink,'_blank');
    }
  });
});
