//defining a dataset
let numbers = [];

for(let i=0;i<10;i++){
  let rnd=Math.floor(Math.random() *250);
  numbers.push(rnd);
} 

// max-min normalization
console.log(numbers);

//find maximum value
const max = (array) => {
//  return Math.max(...array);
let max=array[0];
 for(let i=1; i<array.length; i++){
 if(array[i]>max){
    max=array[i];
  }
  i++;
}
return max;
}

// find minumum value
const min = (array) => {
  //  return Math.min(...array);
  let min=array[0];
  for(let i=1; i<array.length; i++){
    if(array[i]<min){
      min=array[i];
    }
    i++;
  }
  return min;
};

// make it normaliza
const minMax = numbers.map(
  (e) => (e - min(numbers)) / (max(numbers) - min(numbers))
);