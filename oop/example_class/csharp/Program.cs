using System;

namespace vscode
{
    class Person
    {
        protected string name;

        // constructor
        public Person(string aName)
        {
            name = aName;
        }

        public virtual string getName()
        {
            return this.name;
        }

    }

    class Teacher : Person
    {
        private string subject;

        public Teacher(string aName, string teaches) : base(aName)
        {
            subject = teaches;
        }

        public string getSubject()
        {
            return this.subject;
        }
    }

    class Student : Person
    {
        private int year;

        public Student(string aName, int yearGroup) : base(aName)
        {
            year = yearGroup;
        }

        public int getYear()
        {
            return this.year;            
        }

    }

    class Program
    {
        static void Main(string[] args)
        {
            Person aPerson = new Person("Andrew");
            Teacher aTeacher = new Teacher("Mr Bramwell", "Computer Science");
            Student aStudent = new Student("Noud", 12);

            Console.WriteLine($"My name is {aPerson.getName()}");
            Console.WriteLine($"My name is {aTeacher.getName()} and I am a teacher of {aTeacher.getSubject()}");
            Console.WriteLine($"My name is {aStudent.getName()} and I am a student in year {aStudent.getYear()}");
        }
    }
}