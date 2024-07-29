// class Person {
//     constructor(name,age){
//         this._name=name;
//         this._age=age;
//     }

//     get name(){
//         return this._name
//     }

//     get age(){
//         return this._age
//     }

//     set name(newname){
//         if(newname.length >0){
//             this._name = newname
//         } else{
//             console.log("Error")
//         }
//     }

//     set age(age){
//         if(age>=0){
//             this._age = age;
//         }
//     }
// }
class Person{
    constructor(name, age){
        this.name = name;
        this.age = age;
    }
    #mymethod(){
        
    }
    
}
let person = new Person('sumedh', 35);
console.log(person.age);
console.log(person.name);
person.age =40;
console.log(person.age);