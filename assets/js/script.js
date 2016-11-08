var yourAns = new Array;

function func(questionPK) {
    $("#q"+questionPK).hide();
    $("#next-"+questionPK).hide();
    $("#q"+questionPK).next().show();



}

function submit() {
 $('#form').submit()
}

function nextQuestion(questionPK, answerNumber, isCorrect, right, total, questionNumber) {
$(".answer-q"+questionPK+'-True').attr('disabled', 'disabled');
$(".answer-q"+questionPK+'-False').attr('disabled', 'disabled');
$(".answer-q"+questionPK+'-False').attr('onClick','event.preventDefault();');
$(".answer-q"+questionPK+'-True').attr('onClick','event.preventDefault();');

$(".answer-q"+questionPK+'-True').css({"background": "#2E8B57", 'box-shadow':'0px 0px 0px 14px rgba(50, 247, 50, 1)'})
$("#q"+questionPK+"-a"+answerNumber).attr("checked", true)
if (isCorrect == "False"){
	$("#answer-"+answerNumber+'-on-'+questionPK).css({"background": "#DCDCDC",'box-shadow':'0px 0px 0px 14px rgba(200, 50, 50, 1)'})

}

$("#next-"+questionPK).show();
}

function lastQuestion(questionPK, answerNumber, isCorrect, right, total, questionNumber) {
$(".answer-q"+questionPK+'-True').attr('disabled', 'disabled');
$(".answer-q"+questionPK+'-False').attr('disabled', 'disabled');
$(".answer-q"+questionPK+'-False').attr('onClick','event.preventDefault();');
$(".answer-q"+questionPK+'-True').attr('onClick','event.preventDefault();');

$(".answer-q"+questionPK+'-True').css({"background": "#2E8B57", 'box-shadow':'0px 0px 0px 14px rgba(50, 247, 50, 1)'})
$("#q"+questionPK+"-a"+answerNumber).attr("checked", true)
if (isCorrect == "False"){
	$("#answer-"+answerNumber+'-on-'+questionPK).css({"background": "#DCDCDC",'box-shadow':'0px 0px 0px 14px rgba(200, 50, 50, 1)'})
}
$("#next-"+questionPK).show();
}
