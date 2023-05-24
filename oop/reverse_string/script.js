class Helper {

  constructor (type) {
    this.type = type;
  }

  get_type() {
    return this.type
  }

  // returns string parameter reversed
  reverse_string(string) {
    let tmp_str = ""
    while (string != "") {
      tmp_str += string.slice(-1);
      string = string.slice(0,-1);
    }
    return tmp_str;
  }

  reverse_string_recursive(string) {
    console.log(string);

    if (string == "") {
      return ""
    } else {
      return string.slice(-1) + this.reverse_string_recursive(string.slice(0,-1));
      console.log(string);
    }
  }

}

// declare elements... the assign listeners...
const inp = document.getElementById("input_text").addEventListener("input", updateButton);
const btn = document.getElementById("reverse_button");
btn.addEventListener("click", main);

// create a new instance of the Helper class
const helper = new Helper("reverse");


// checks to see if text has been entered disables button accordingly
function updateButton(e) {
  if (e.target.value != "") {
    document.getElementById("reverse_button").disabled = false;
  } else {
    document.getElementById("reverse_button").disabled = true;
  }
}


// function runs when the button is clicked (see eventListener above)
function main() {
  let inp_element = document.getElementById("input_text");
  let out_element = document.getElementById("output_text");
  
  if (inp_element.value != "") {
    // out_element.innerHTML = helper.reverse_string(inp_element.value);
    out_element.innerHTML = helper.reverse_string_recursive(inp_element.value);
  }
}
