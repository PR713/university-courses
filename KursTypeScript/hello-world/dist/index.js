"use strict";
let age = 20;
if (age < 50)
    age += 10;
console.log(age);
let sales = 123456879;
let course = 'TypeScript';
let is_published = true;
let student = 'Radek';
let level;
level = 1;
level = 'a';
function render(document) {
    console.log(document);
}
let numbers = [1, 2, '3'];
let numbers1 = [1, 2, 3];
let user = [1, 'Radek'];
const small = 1;
const medium = 2;
const large = 3;
var Size;
(function (Size) {
    Size[Size["Small"] = 1] = "Small";
    Size[Size["Medium"] = 2] = "Medium";
    Size[Size["Large"] = 3] = "Large";
})(Size || (Size = {}));
;
let mySize = Size.Small;
console.log(mySize);
function calculateTax(income, taxYear = 2024) {
    if (taxYear < 2022) {
        return income * 1.05;
    }
    return income * 1.1;
}
let employee = {
    id: 1,
    name: 'Radek',
    retire: (date) => {
        console.log(date);
    }
};
function kgToLbs(weight) {
    if (typeof weight === 'number') {
        return weight * 2.2;
    }
    else {
        return parseInt(weight) * 2.2;
    }
}
kgToLbs(10);
kgToLbs('10');
//# sourceMappingURL=index.js.map