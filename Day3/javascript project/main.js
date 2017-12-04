window.onload = function() {

  document.getElementById("fname").onblur = function(){
    if(this.value == ""){
      document.getElementById("efname").innerHTML = "This field cannot be empty";
      this.style.borderColor = "red";
    }else{
      document.getElementById("efname").innerHTML = "";
      this.style.borderColor = "#ccc";
    }
  };

  document.getElementById("lname").onblur = function(){
    if(this.value == ""){
      document.getElementById("elname").innerHTML = "This field cannot be empty";
      this.style.borderColor = "red";
    }else{
      document.getElementById("elname").innerHTML = "";
      this.style.borderColor = "#ccc";
    }
  };

  document.getElementById("uname").onblur = function(){
    if(this.value == ""){
      document.getElementById("euname").innerHTML = "This field cannot be empty";
      this.style.borderColor = "red";
    }else{
      document.getElementById("euname").innerHTML = "";
      this.style.borderColor = "#ccc";
    }
  };

  document.getElementById("password").onblur = function(){
    if(this.value == ""){
      document.getElementById("epassword").innerHTML = "This field cannot be empty";
      this.style.borderColor = "red";
    }else{
      document.getElementById("epassword").innerHTML = "";
      this.style.borderColor = "#ccc";
    }
  };

  document.getElementById("cpassword").onblur = function(){
    if(this.value == ""){
      document.getElementById("ecpassword").innerHTML = "This field cannot be empty";
      this.style.borderColor = "red";
    }else{
      document.getElementById("ecpassword").innerHTML = "";
      this.style.borderColor = "#ccc";
    }
  };

  document.getElementById("month").onblur = function(){
    if(this.value == ""){
      document.getElementById("emonth").innerHTML = "This field cannot be empty";
      this.style.borderColor = "red";
    }else{
      document.getElementById("emonth").innerHTML = "";
      this.style.borderColor = "#ccc";
    }
  };

  document.getElementById("day").onblur = function(){
    if(this.value == ""){
      document.getElementById("eday").innerHTML = "This field cannot be empty";
      this.style.borderColor = "red";
    }else{
      document.getElementById("eday").innerHTML = "";
      this.style.borderColor = "#ccc";
    }
  };

  document.getElementById("year").onblur = function(){
    if(this.value == ""){
      document.getElementById("eyear").innerHTML = "This field cannot be empty";
      this.style.borderColor = "red";
    }else{
      document.getElementById("eyear").innerHTML = "";
      this.style.borderColor = "#ccc";
    }
  };

  document.getElementById("gender").onblur = function(){
    if(this.value == ""){
      document.getElementById("egender").innerHTML = "This field cannot be empty";
      this.style.borderColor = "red";
    }else{
      document.getElementById("egender").innerHTML = "";
      this.style.borderColor = "#ccc";
    }
  };

  document.getElementById("phone").onblur = function(){
    if(this.value == ""){
      document.getElementById("ephone").innerHTML = "This field cannot be empty";
      this.style.borderColor = "red";
    }else{
      document.getElementById("ephone").innerHTML = "";
      this.style.borderColor = "#ccc";
    }
  };

  document.getElementById("terms").onclick = function(){
    if(this.checked == false){
      document.getElementById("eterms").innerHTML = "You need to agree to our terms to use our services";
      this.style.borderColor = "red";
    }else{
      document.getElementById("eterms").innerHTML = "";
      this.style.borderColor = "#ccc";
    }
  };

  document.getElementById("password").onkeyup = function(){
    var strength = document.getElementById("strength");
    if(this.value.match("((?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).{8,20})")){
      strength.className = "passwordStrength";
      strength.className += " strong";
    }
    else if(this.value.match("(?=.*[a-zA-Z])(?=.*\\d).{8,}")){
      strength.className = "passwordStrength";
      strength.className += " good";
    }else if(this.value.length<8 || this.value.match("(?=.*[0-9])") || this.value.match("(?=.*[a-z])")){
      strength.className = "passwordStrength";
      strength.className += " weak";
    }
    if(this.value.length > 0){
      document.getElementById("epassword").innerHTML = "";
      this.style.borderColor = "#ccc";
    }
  };

  document.getElementById("cpassword").onkeyup = function(){
    password = document.getElementById("password").value;
    if(this.value != password){
      if(document.getElementById("ecpassword").className == "success"){
        document.getElementById("ecpassword").className = "error";
      }
      document.getElementById("ecpassword").innerHTML = "Passwords do no match";
      this.style.borderColor = "red";
    }else{
      document.getElementById("ecpassword").innerHTML = "Password matches";
      this.style.borderColor = "#ccc";
      if(document.getElementById("ecpassword").className == "error"){
        document.getElementById("ecpassword").className = "success";
      }
    }
  };

document.getElementById("signupForm").onsubmit = function(){
    var flag = 0;
    if(document.getElementById("password").value != document.getElementById("cpassword").value){
      document.getElementById("ecpassword").innerHTML = "Passwords do no match";
      document.getElementById("ecpassword").style.borderColor = "red";
      flag = 1;
    }else{
      document.getElementById("ecpassword").innerHTML = "";
      document.getElementById("ecpassword").style.borderColor = "#ccc";
    }

    var day = document.getElementById("day").value;
    var month = document.getElementById("month").value;
    var year = document.getElementById("year").value;

    if (year.length > 4) {
        document.getElementById("eyear").innerHTML = "Enter a valid year";
        document.getElementById("eyear").style.borderColor = "red";
        return false;
    }else{
        document.getElementById("eyear").innerHTML = "";
        document.getElementById("eyear").style.borderColor = "#ccc";
    }

    if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12){
      if(day<=0 || day >31){
        document.getElementById("eday").innerHTML = "Enter a valid day of month";
        document.getElementById("eday").style.borderColor = "red";
        return false;
      }else{
        document.getElementById("eday").innerHTML = "";
        document.getElementById("eday").style.borderColor = "#ccc";
      }
    }else if(month == 4 || month == 6 || month == 9 || month == 11){
      if(day<=0 || day >30){
        document.getElementById("eday").innerHTML = "Enter a valid day of month";
        document.getElementById("eday").style.borderColor = "red";
        return false;
      }else{
        document.getElementById("eday").innerHTML = "";
        document.getElementById("eday").style.borderColor = "#ccc";
      }
    }else if(month == 2){
      if(parseInt(year)%400==0 || (parseInt(year)%100!=0 && parseInt(year)%4==0)){
        if(day<=0 || day >29){
          document.getElementById("eday").innerHTML = "Enter a valid day of month";
          document.getElementById("eday").style.borderColor = "red";
          return false;
        }else{
          document.getElementById("eday").innerHTML = "";
          document.getElementById("eday").style.borderColor = "#ccc";
        }
      }else{
        if(day<=0 || day >28){
          document.getElementById("eday").innerHTML = "Enter a valid day of month";
          document.getElementById("eday").style.borderColor = "red";
          return false;
        }else{
          document.getElementById("eday").innerHTML = "";
          document.getElementById("eday").style.borderColor = "#ccc";
       }
      }
    }

    var date = new Date(year, month-1, day).getTime();

    var today = new Date().getTime();
    if(today<date){
      document.getElementById("emonth").innerHTML = "Birthday cannot be a future date";
      flag = 1;
    }else{
      document.getElementById("emonth").innerHTML = "";
    }

    if(document.getElementById("terms").checked == false){
      document.getElementById("eterms").innerHTML = "You need to agree to our terms to use our services";
      document.getElementById("terms").style.borderColor = "red";
      flag = 1;
    }else{
      document.getElementById("eterms").innerHTML = "";
      document.getElementById("terms").style.borderColor = "#ccc";
    }

    if(flag == 1){
      return false;
    }else{
      newWindow = window.open("", "_blank");
      newWindow.document.write("<h2>You have been successfully signed up</h2>");
      return true;
    }
  };
};
