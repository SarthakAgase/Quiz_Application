function Start_Test() {
  let Name = document.getElementById("floatingName").value;
  let Roll = document.getElementById("floatingRoll").value;
  let Id = document.getElementById("floatingId").value;
  let Password = document.getElementById("floatingPassword").value;
  if ((Name, Roll, Id, Password != "")) {
    eel.Start_Test(Name, Roll);
  }
}
