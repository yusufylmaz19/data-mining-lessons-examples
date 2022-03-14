
// z-score normalization

//defining a dataset
let numbers = [];

for(let i=0;i<10;i++){
  let rnd=Math.floor(Math.random() *250);
  numbers.push(rnd);
} 

// find avarage value
const avg = (array) => {
    let sum = 0;
    array.forEach((e) => {
      sum += e;
    });
    return sum / array.length;
  };
  
  
  //finding standart deviation
  let sum=0;
  const myArray = numbers.map(
      (e)=>( Math.pow(e-avg(numbers),2))
  ).forEach((e)=>{
       sum+=e;
  })
  
  const stnd=Math.sqrt(sum/(numbers.length-1));
  
  const zScore=numbers.map((e)=> ((e-avg(numbers))/stnd));