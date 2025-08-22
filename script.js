let res = document.getElementById("result");

function append(val){ 
  res.value += val; 
}
function clr(){ 
  res.value = ""; 
}
function del(){ 
  res.value = res.value.slice(0,-1); 
}
function calculate(){ 
  try { 
    res.value = eval(res.value); 
  }
  catch { 
    res.value = "Error"; 
  }
}
