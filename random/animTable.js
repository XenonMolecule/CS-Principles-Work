
var rows = 0;

//Set variables to decide things like button disable time
//And also eases the changing of animation
var fadeTime = 700;
var delayTime = 50;

//This also won't be correct until table is set
//since it depends on rows
//Used to decide how long button needs to be disabled after clicked
var animTime = 0;

$(window).load(function()
{

  //Now we can properly set the rows and animTime variable
  rows = $("#m tr").length;
  animTime = (rows * delayTime) + fadeTime + 100;
  //+100 for margin
});

//Loop through all table rows and fade them in
var animateTable = function(i, rows)
{
  (function next(i) {
    if (i++ >= rows) return;
    setTimeout(function() {
        $("#m tr:nth-child(" + i + ")").fadeTo(fadeTime, 0.7);
        next(i);
    }, delayTime);
  })(0, rows);
}

function hideTable() {
  $("#m tr:nth-child(1n)").css("opacity", 0);
}

// make sure your desired animated table has an id of "m"
