var yourAns = new Array;

function func(questionPK) {
    $("#q"+questionPK).hide();
    $("#q"+questionPK+"-stat").hide();
    $("#q"+questionPK+"-stat").next().show();

}

function submit() {
 $('#form').submit()
}

function nextQuestion(questionPK, answerNumber, isCorrect, right, total, questionNumber) {
$(".answer-q"+questionPK+'-True').attr('disabled', 'disabled');
$(".answer-q"+questionPK+'-False').attr('disabled', 'disabled');
$(".answer-q"+questionPK+'-False').removeAttr('onClick');
$(".answer-q"+questionPK+'-True').removeAttr('onClick');

$(".answer-q"+questionPK+'-True').css({"background": "green"})
$(".answer-q"+questionPK+'-False').css({"background": "red"})
$("#q"+questionPK+"-a"+answerNumber).attr("checked", true)
width = (questionNumber)*100/$(".question").length
$("#myBar").css({'width': width + '%' }); 
percent=0
if(isCorrect=='True'){
    percent = (right+1)*100/(total+1)
} else {
    percent = right*100/(total+1)
}
$("#q"+questionPK).after("<p id='q"+questionPK+"-stat'>"+percent+" % answered right </p>");
setTimeout(func, 3000, questionPK);

}

function lastQuestion(questionPK, answerNumber, isCorrect, right, total, questionNumber) {
$(".answer-q"+questionPK+'-True').attr('disabled', 'disabled');
$(".answer-q"+questionPK+'-False').attr('disabled', 'disabled');
$(".answer-q"+questionPK+'-True').css({"background": "green"})
$(".answer-q"+questionPK+'-False').css({"background": "red"})
$("#q"+questionPK+"-a"+answerNumber).attr("checked", true)
width = (questionNumber)*100/$(".question").length
$("#myBar").css({'width': width + '%' }); 
percent=0
if(isCorrect=='True'){
    percent = (right+1)*100/(total+1)
} else {
    percent = right*100/(total+1)
}
$("#q"+questionPK).after("<p id='q"+questionPK+"-stat'>"+(percent).toFixed(2)+" % answered right </p>");
setTimeout(submit, 3000);
}
