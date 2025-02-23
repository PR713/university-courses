// == is loose equality, === is strict equality (checks also type)

//composition allows to create new functions by combining other functions
// like function eat()..., function bark()...ane then
// function createDog() {
//   return Object.assign({}, eater, barker);
// } // it creates a new empty object with properties from eater and barker
// const dog = createDog();
// dog.eat(); ... dog.bark()...


function createPerson(name) { // Factory function
    return { name }; // returns literal object, casual object { }
}

const p2 = createPerson("Radek");
console.log(p2.constructor); // [Function: Object]
//it returns a casual object, .constructor is from Object.prototype.constructor
console.log(p2 instanceof createPerson); // false
console.log(p2 instanceof Object); // true


function Person(name) { // Constructor function
    //this is a reference to the object that is created here and
    //returned by the constructor function
    this.name = name;
}

const p1 = new Person("Radek");
console.log(p1.constructor); // [Function: Person]
//it creates a new instation by using keyword 'new'
console.log(p1 instanceof Person); // true
console.log(p1 instanceof Object); // true

//--------------------------------------------


//Function as an object

// function add(x, y) {
//     return x + y;
// }
//
// const n = add;
//
// console.log(n(2, 3)); // 5
//
// console.log(add.length); // a number of arguments that function expects


// function Programmer(name) { // Constructor function
//     this.name = name;
//     this.writeCode = function () {
//         console.log("Code in JavaScript");
//     }
// }
//
// console.log(Programmer.length); // 1
// console.log(Programmer.constructor); // [Function: Function]
//

const Programmer = new Function('name', `
    this.name = name;
    this.writeCode = function (){
        console.log("Code in JavaScript");
    }
    `);

const newProgrammer = new Programmer("Radek");
newProgrammer.writeCode();
console.log(Programmer.constructor); // [Function: Function]
//all function in JS are instances of Function
console.log(newProgrammer.constructor); // [Function: anonymous]
//new Function() creates anonymous function ( function without name)

/*
const num = Number("42");
console.log(num); // 42
console.log(typeof num); // "number"

const numObj = new Number("42");
console.log(numObj); // [Number: 42]
console.log(typeof numObj); // "object"

//JavaScript automatycznie opakowuje prymitywne wartości liczbowe
w obiekty Number, gdy potrzebne są metody obiektowe (np. toFixed()).
 */



console.log('-----------------');
///---------------------

const dog = {
    name: "Rex",
    age: 5,
    eyeColor: "brown",
};

const keys = Object.keys(dog);
console.log(keys); // [ 'name', 'age', 'eyeColor' ]

const values = Object.values(dog);
console.log(values); // [ 'Rex', 5, 'brown' ]


const entries = Object.entries(dog);
console.log(entries); // [ [ 'name', 'Rex' ], [ 'age', 5 ], [ 'eyeColor', 'brown' ] ]


for (const key in dog) {
    console.log(key, dog[key]);
}
//or

for (const [key, value] of entries) {
    console.log(key, value);
}


console.log('-----------------');



let a = {value : 1};
// let b = a; //now b is a reference to a
let b = {};

Object.assign(b, a); //copy all properties from a to b
//or let b = {...a}; //spread operator
b.value = 2;
console.log(a);
console.log(b);


console.log('-----------------');

let min = 2;
let max = 10;
let random = Math.round(Math.random() * (max - min) + min);
//if 3.14 then 3, if 3.5 then 4...



console.log('-----------------');


const name = "Radek";
console.log(typeof name); // string

// const anotherName = new String("Radek");
// console.log(typeof anotherName); // object

//the difference is that name is a primitive type and anotherName is an object
//it is used really seldom

let sentence = "This is a sentence";

const doesIncludeIs = sentence.includes("is"); // true

const updatedSentence = sentence.replace("a", "A");

console.log(updatedSentence);

const sentenceArray = sentence.split(" ");

console.log(sentenceArray);

const date = new Date('December 25 2024 16:08');
console.log(date); // 2024-12-25T15:08:00.000Z

const now = new Date();
console.log(now.getTimezoneOffset());


console.log('-----------------');

const numbers = [1, 2, 3, 4, 5];
// numbers.push(6); // add to the end
// numbers.unshift(10); // add to the beginning,

numbers.splice(2, 1, 7, 8); // add to the 2nd position
console.log(numbers);
// [1, 2, 7, 8, 4, 5]
// numbers.pop(); // remove last element
// numbers.shift(); // remove first element
numbers.splice(1,1); // remove from the 2nd position
console.log(numbers);



console.log('-----------------');


let employees = [
    { name: "John", age: 30 },
    { name: "An", age: 28 },
    { name: "Radek", age: 20 },
];

employees.sort((a,b) => {
    const lowerCaseA = a.name.toLowerCase();
    const lowerCaseB = b.name.toLowerCase();
    if (lowerCaseA < lowerCaseB) return -1;
    if (lowerCaseA > lowerCaseB) return 1;
    return 0;
})

console.log(employees);

const updatedEmployees = employees.map(employee => {
    return {
        ...employee,
        name: employee.name.toUpperCase(),
        salary: 5000,
    };
});

console.log(updatedEmployees);

const sumOfAges = employees.reduce((acc, employee) => {
            return acc + employee.age;
}, 0); // 0 is the initial value of acc else it would be the first element of the array
//which IS AN OBJECT!!! (Result [object Object]3020 !!! )

console.log(sumOfAges);


