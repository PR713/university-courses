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




console.log('-----------------');

let fun = function(num1, num2){
    let prod = 1;
    for ( const num of arguments) {
        prod *= num;
    }
    return prod;
}

console.log(fun(1,2,3,5));



console.log('-----------------');

const fun2 = function(...args){
    return args.reduce((acc, num) => acc * num, 1);
}


console.log(fun2(1,2,3,5));


console.log('-----------------');


const fun3 = function(multiplier, ...numbers){
    return numbers.map(num => num * multiplier);
}

console.log(fun3(3,2,3,5));



console.log('-----------------');


let funWithDefaultParams = function (name, role = 'guest', status = 'active'){
    console.log(`User: ${name}, Role: ${role}, Status: ${status}`);
}

funWithDefaultParams('Radek', 'admin', 'inactive');
funWithDefaultParams('John', 'admin');



console.log('-----------------');


const course = {
    name: 'JavaScript for Beginners',
    duration: '4 hours',
    get details(){
        return `${this.name} is ${this.duration}`;
    },
    set details(value){
        if (typeof value !== 'string') {
            throw new Error(`Value ${value} must be a string`);
        }

        const parts = value.split(' is ');
        this.name = parts[0];
        this.duration = parts[1];
    }
}

console.log(course.details); //getter, without parentheses due to it has
//get or set keyword, else we use ()
course.details = 'JavaScript Pro is 12 hours'; //setter
console.log(course.details);

try {
    course.details = 42;
} catch (e) {
    console.error(`Caught an error: ${e.message}`);
}


console.log('-----------------');

function display(){
    for (var i = 0; i < 5; i++){
        console.log(i);
    }
    console.log(i) //if we use let i, we don't have an access there
}



console.log('-----------------');

const course2 = {
    name: 'JavaScript for Beginners',
    start() {
        console.log(this.name); //this - that object
    }
}

course2.start();


//but

function startVideo(){
    console.log(this); //global object
}

startVideo(); //and browsers have a window object



//but when we use arrow function it uses the context from parent
const course3 = {
    name: 'ES6 syntax',
    start: () => {
        console.log(this.name); //undefined
    }
}


console.log('-----------------');

function introduce(language) {
    console.log(`I am ${this.name} and I program in ${language}`);
}

introduce('JavaScript'); //I am undefined and I program in JavaScript
const student = {name: 'Radek'};
const introduction = introduce.bind(student); //this -> student
introduction('JavaScript');


//or

const student2 = {name: 'Kasia'};
const newIntroduction = introduce.bind(student2); //this -> student2
newIntroduction('Python');
//I am Kasia and I program in Python


//but
const newIntro = introduction.bind(student2); //this -> student, not student2
newIntro('Java'); //I am Radek and I program in Java
//because it is already bound to student