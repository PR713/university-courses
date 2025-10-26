let age: number = 20;
if (age < 50)
    age += 10;
console.log(age);


let sales: number = 123_456_879;
let course: string = 'TypeScript';
let is_published: boolean = true;
let student = 'Radek';
let level;
level = 1;
level = 'a';

function render(document: any) {
    console.log(document);
}

let numbers = [1, 2, '3'];
let numbers1 = [1, 2, 3];

let user: [number, string] = [1, 'Radek'];

const small = 1;
const medium = 2;
const large = 3;

enum Size {Small = 1, Medium, Large};
let mySize: Size = Size.Small;
console.log(mySize);


function calculateTax(income: number, taxYear = 2024): number {

    if (taxYear < 2022) {
        return income * 1.05;
    }
    return income * 1.1;
}


// let employee: {
//     readonly id: number;
//     //name?: string;
//     name: string;
//     retire: (date: Date) => void;
// } = {
//     id: 1,
//     name: 'Radek',
//     retire: (date: Date) => {
//         console.log(date);
//     }
// };
// // employee.name = 'Radek';
// console.log(employee);
// employee.id = 0;


type Employee = {
    readonly id: number;
    name: string;
    retire: (date: Date) => void;
};

let employee: Employee = {
    id: 1,
    name: 'Radek',
    retire: (date: Date) => {
        console.log(date);
    }
};

////////////////////////////////////////


function kgToLbs(weight: number | string): number {

    if (typeof weight === 'number') {
        return weight * 2.2;
    } else {
        return parseInt(weight) * 2.2;
    }
    //why weight.valueOf * 2.2 doesn't work?
}

kgToLbs(10);
kgToLbs('10');

////////////////////////////////////////
type Draggable = {
    drag: () => void;
}

type Resizable = {
    resize: () => void;
}

type UIWidget = Draggable & Resizable;

let textBox: UIWidget = {
    drag: () => {
        console.log('dragging');
    } ,
    resize: () => {
        console.log('resizing');
    }
};

////////////////////////////////////////
//Literal (exact, specific) types
type Quantity = 50 | 100;
let quantity: Quantity = 50;

type Metric = 'cm' | 'inch';
let metric: Metric = 'cm';

////////////////////////////////////////

function greet(name: string | null | undefined) {
    if (name)
        console.log(name.toUpperCase());
    else
        console.log('Hello');
}

greet(null);

////////////////////////////////////////

type Customer = {
    birthDate?: Date;
};

function getCustomer(id: number): Customer | null {
    return id === 0 ? null : {birthDate: new Date()};
}

let customer = getCustomer(0);
//Optional property access operator
console.log(customer?.birthDate?.getFullYear());

//Optional element access operator
// if (customer !== null && customer !== undefined) {
//...... better
// customers?[0]

//optional call
let log: any = null;
console.log(log?.('a'));