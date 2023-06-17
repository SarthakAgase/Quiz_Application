window.onload = function () {
  fetch("GetInfo/")
    .then((response) => response.json())
    .then((Info) => {
      console.log(Info);
      document.getElementById("name").innerHTML = `${Info["FullName"]}`;
      document.getElementById("roll_no").innerHTML = `${Info["RollNumber"]}`;
      document.getElementById("marks").innerHTML = `${Info[
        "Total_Marks"
      ].toFixed(2)}`;
      document.getElementById("time").innerHTML = `${Info["Total_Time"]}`;
      document.getElementById("rank").innerHTML = `${Info["rank"]}`;
    });
};
