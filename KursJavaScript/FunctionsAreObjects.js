//composition allows to create new functions by combining other functions
// like function eat()..., function bark()...ane then
// function createDog() {
//   return Object.assign({}, eater, barker);
// }
// const dog = createDog();
// dog.eat(); ... dog.bark()...


function createPerson(name) { // Factory function
    return { name };
}

const p2 = createPerson("Radek");
console.log(p2.constructor); // [Function: Object]
//it returns a casual object, .constructor is from Object.prototype.constructor
console.log(p2 instanceof createPerson); // false
console.log(p2 instanceof Object); // true


function Person(name) { // Constructor function
    this.name = name;
}

const p1 = new Person("Radek");
console.log(p1.constructor); // [Function: Person]
//it creates a new instation by using keyword 'new'
console.log(p1 instanceof Person); // true
console.log(p1 instanceof Object); // true

//--------------------------------------------



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