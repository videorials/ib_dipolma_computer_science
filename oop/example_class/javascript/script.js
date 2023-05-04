/* https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript */

class Person {
  
  constructor(name) {
    this.name = name;
  }
  
  introduceSelf() {
    const elem = document.querySelector('#debug')
    elem.innerText += `Hi! I'm ${this.name}`
    console.log(`Hi! I'm ${this.name}`);
  }

}

class Teacher extends Person {

  constructor(name, teaches) {
    super(name);
    this.teaches = teaches;
  }

  introduceSelf() {

    const elem = document.querySelector('#debug')
    elem.innerText += `\nMy name is ${this.name}, and I will be your ${this.teaches} teacher.`
    console.log(`My name is ${this.name}, and I will be your ${this.teaches} teacher.`);

  }
  
}

class Student extends Person {

  #year;

  constructor(name, year) {
    super(name);
    this.#year = year;
  }

  introduceSelf() {
    const elem = document.querySelector('#debug')
    elem.innerText += `\nHi! I'm ${this.name}, and I'm in year ${this.#year}.`
    console.log(`Hi! I'm ${this.name}, and I'm in year ${this.#year}.`);
  }
  
}


function main() {
  const aPerson = new Person("Andy");
  aPerson.introduceSelf();
  const aTeacher = new Teacher("Mr Bramwell", "Computer Science");
  aTeacher.introduceSelf();
  const aStudent = new Student("Noud", 12);
  aStudent.introduceSelf();
}