// let count =1

// while (count <=100) {
//   console.log(count)
//   count =count +1
  
// }

// for (let i =0; i<3; i = i+1) {
//   console.log(i);
// }

// example 3
// for (let i = 1; i <= 20; ++i ) {
//   if (i%3===0 && i%5===0) {
//     console.log(`${i} frontend simplified`)
//   }
//   else if (i%3 ===0){
//     console.log('Frontend')
//   }
//   else if (i%5===0) {
//     console.log(`${i} -> simplified`)
//   }
//   else{
//     console.log(`${i} - ${i}`)
//   }}


// example 4 -my attempt worked
// x=0

// for (let i = 'frontend simplified'; x <= 19; ++x ){
//   if (x <= 19){
//     console.log(i[x])
//   }

// }

// example 4 better way

// const str = 'frontend simplified'

// for (let i=0; i < str.length; ++i){
//   console.log(str[i])
// }

//example5

// DRY- dont repeat yourself, make a funciton do it
//funtion definition, 

// function welcomePersonToFES(FirstName, LastName) {
//   console.log(`welcom to FES, ${FirstName} ${LastName}`)
//   //console.log(name)
// }
// //call the function
// welcomePersonToFES('Enrique', 'Munoz');


//these 2 funcitons are the same becaue nothing is executed after
// a return function
// function fn() {
//   return 5
//   console.log('my function')

// }

// console.log(fn()) or console.log(5)
//---------------------------------------------
// function sumOfTwoNumbers(num1, num2) {
//   return num1 +num2
  
// }
  
//  console.log(sumOfTwoNumbers(10, 10)); //a for argument goes at the bottom because it is smaller and one line,
 //p  (num1, num2) for paramitars goes on top becaue it is bigger a- when you call
 //the funciton and p when you define it
//--------------------------------------
 //create a function that converts celsius to fahrenheit

 //F= c * 1.8 +32 

//  function fahrenheit(celsius1) {
//   return celsius1* 1.8 + 32

//  }
//  console.log(fahrenheit(0));

//  //another solution

// function convertCelsiusToFahrenheit(celsius){
//   let fahrenheit = celsius * 1.8 + 32
//   return fahrenheit
// }
// console.log(convertCelsiusToFahrenheit(0))
// //...another...
// const convertCelsiusToFahrenheit = () => {
//   return celsius *1.8 + 32
// }
// console.log(convertCelsiusToFahrenheit(0))
//----------------------------------------------

// let arr = [20,30,40,50,100]

// let newArr=arr.filter((element) => {
//   console.log(element)
//   if (element<50){
//   return true;}
// })
// console.log(newArr)

//Better way:
// let arr = [20,30,40,50,100]

// let newArr=arr.filter(element => {
//   return (element<50)
// })
// console.log(newArr)
// //or best way:

// let newArr=arr.filter(element => element<50)
//----------------------------------------------

// let grades = ['A+', 'A', 'FAIL']

// let passGrades = grades.filter(element => element!= 'FAIL')

// console.log(passGrades)


// let grades = ['A+', 'A', 'FAIL']
// let goodGrades =[]

//   for (let i = 0; i < grades.length; ++i) {
//     if (grades[i] !== 'FAIL'){
//       goodGrades.push(grades[i])
 
// }
//   }
// console.log(goodGrades)
//--------------------------------------------
// let arr= [1, 4, 9, 16]

// arr.map(element => {
//   console.log(element)
// })

// let newArr = arr.map(element => 'dog')

// console.log(newArr)     -----> ['dog', 'dog', 'dog', 'dog']

// let dollars = [1, 5, 10, 3]
// let cents =[]
// // let cents = dollars.map(element => element*100)
// // console.log(cents)

// //using the for loop instead...

// for (let i =0; i < dollars.length; ++i) {
//  cents.push(dollars[i]*100)
// }
//   console.log(cents)
//------------------------------------------------------
//OBJECTS- mulitple properties in one Var

// let user= {
//   username: 'munoz',
//   email: 'sdkljf@gmail.com', 
//   lessonCompleted: [0, 1],
// }
// console.log(user.username) ------> munoz

// this is now an array...
let user= [
  {
  username: 'munoz',
  email: 'sdkljf@gmail.com', 
  password: 'test123',
  lessonCompleted: [1,2],
  },
  {
  username: 'mudnoz',
  email: 'sdkdljdf@gmail.com', 
  password: 'test321',
  lessonCompleted: [1, 2, 3],
  },
];
//this is how you log someone in...
function login(email, password) {
  for (let i = 0; i < user.length; ++i){
    console.log(user[i])
    if (user[i].email === email){
      console.log(user[i]);
      if (user[i].password === password) {
        console.log ('log user in- the details are correct')
      }
      else{
        console.log('password is incorrect')
      }
      return;
    }
  }
  console.log('could not find find an email that matches')
}

//login('sdkljf@gmail.com', 'test123')
//console.log(user[0].lessonCompleted.map((elem) => elem * 2));

//creat a register funciton

// function register(username, email, password, lessonCompleted){
//   let users = {
//     username: username,
//     email: email,
//     password: password,
//     lessonCompleted: lessonCompleted,
//   }
//    user.push(users); 
//   }

//register('ricko', 'ricko@gmail.com', 'ricko1213', [0,1,2]);

function register(users){
  user.push(users)
  }
  
//the following is better for other devs to be able to read
register({
  username:'ricko', 
  email:'ricko@gmail.com',
  password: 'ricko1213',
  lessonCompleted: [0,1,2],
});

console.log(user)
