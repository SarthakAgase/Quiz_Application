var StartTime = 5;
var time = StartTime * 60;
var ques_no = 1;
var form_check_inputs = document.querySelectorAll(".form-check-input");
var prev_time = 0;

window.onload = GetQues();

setInterval(updateTime, 1000);
function updateTime() {
  var minutes = Math.floor(time / 60);
  var seconds = time % 60;
  seconds = seconds < 10 ? "0" + seconds : seconds;
  document.getElementById("countdown").innerHTML = `${minutes} : ${seconds}`;
  time--;
}

function SubmitButton() {
  let checked_option;
  form_check_inputs.forEach((form_check_input) => {
    if (form_check_input.checked) {
      checked_option = form_check_input.id;
    }
  });
  let Ques_time = StartTime * 60 - time - prev_time;
  prev_time = StartTime * 60 - time;
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  const requestOptions = {
    method: "POST",
    body: JSON.stringify({
      checked_option: checked_option,
      Ques_time: Ques_time,
      ques_no: ques_no,
    }),
    headers: {
      "X-CSRFToken": csrftoken,
      "Content-type": "application/json",
    },
  };
  fetch("SaveQues/", requestOptions)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    });

  location.href = "/result/";
}

function PreviousButton() {
  if (ques_no < 2) {
    alert("This is First Question of the test. Please Start the test !!!");
  } else {
    ques_no--;
    GetQues();
    form_check_inputs.forEach((form_check_input) => {
      form_check_input.checked = false;
    });
  }
}

function NextButton() {
  if (ques_no > 4) {
    alert("This is Last Question of the test. Please Submit the test !!!");
  } else {
    ques_no++;
    GetQues();
    form_check_inputs.forEach((form_check_input) => {
      form_check_input.checked = false;
    });
  }
}

function SaveButton() {
  let checked_option;
  form_check_inputs.forEach((form_check_input) => {
    if (form_check_input.checked) {
      checked_option = form_check_input.id;
    }
  });
  let Ques_time = StartTime * 60 - time - prev_time;
  prev_time = StartTime * 60 - time;
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  const requestOptions = {
    method: "POST",
    body: JSON.stringify({
      checked_option: checked_option,
      Ques_time: Ques_time,
      ques_no: ques_no,
    }),
    headers: {
      "X-CSRFToken": csrftoken,
      "Content-type": "application/json",
    },
  };
  fetch("SaveQues/", requestOptions)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    });
  NextButton();
}

function GetQues() {
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  const requestOptions = {
    method: "POST",
    body: JSON.stringify({
      Ques_no: ques_no,
    }),
    headers: {
      "X-CSRFToken": csrftoken,
      "Content-type": "application/json",
    },
  };
  fetch("GetQues/", requestOptions)
    .then((response) => response.json())
    .then((QuesAns) => {
      print_ques(QuesAns);
    });
}

function print_ques(QuesAns) {
  document.getElementById("ques_no").innerHTML = `Question ${ques_no} out of 5`;
  document.getElementById("ExamProgress").innerHTML = `${ques_no * 20} %`;
  document.getElementById("ExamProgress").style = `width: ${ques_no * 20}%`;
  document.getElementById("question").innerHTML = QuesAns["question"];
  document.getElementById("optionA-content").innerHTML = QuesAns["optionA"];
  document.getElementById("optionB-content").innerHTML = QuesAns["optionB"];
  document.getElementById("optionC-content").innerHTML = QuesAns["optionC"];
  document.getElementById("optionD-content").innerHTML = QuesAns["optionD"];
}
