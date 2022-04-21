// alert("Hai welcome to your resume");
// console.log("Resume opened");
// let number1=30;
// if (number1 % 2 == 0) {
//     console.log("even number");
//   } else {
//     console.log("odd number");
//   }

// let data= "priya";
//   if (data === "Naveen") {
//     document.write("SQA");
//   } else if (data === "Kiruba") {
//     document.write("DEVELOPER");
//   } else {
//     document.write("outsider");
//     console.log("Outsider");
//   }
// let i = 0;
//   while (i <= 10) {
//     document.write(i);
//     i = i + 1;
//   }

//   function naveen(x, y) {
//     let sum = x + y;
//     return sum;
//   }
  
//   function Area(radius, pi = 3.141) {
//     let area = pi * radius * radius;
//     return area;
//   }
  
//   let radius = prompt("Radius of Circle # ");
  
//   document.write("Area of Circle = ", Area(radius));

//   let food = (radius) => {
//     perimeter = 2 * 3.41 * radius;
//     return perimeter;
//   };
  
//   document.write(food(50));
document.getElementById("phone").innerHTML ="9942733487"  ;
document.getElementById("mail").innerHTML ="naveen@esmito.com"  ;

const x = document.createElement("p");
    x.innerHTML = "Above values are created by Naveen";
        document.body.appendChild(x); // stick the paragraph elemnt into the body

        function Colorb() {
            document.getElementById("bod1").style.border = "thick solid green";
          }
 document.getElementById("btn1").addEventListener("click", function () {
            document.getElementById("para1").innerHTML = "india is great!";
          });