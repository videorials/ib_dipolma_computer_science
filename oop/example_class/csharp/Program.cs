using System;

namespace vscode
{

    class Person
    {
        private string name;

        // constructor
        public Person(string aName)
        {
            name = aName;
        }

        public void introduceMyself()
        {
            Console.WriteLine("Hello, my name is " + this.name);
        }

    }

    class Teacher : Person
    {
        private string subject;

        public Teacher(string aName, string teaches) : base(aName)
        {
            subject = teaches;
        }
    }

    class Student : Person
    {
        private int year;

        public Student(string aName, int yearGroup) : base(aName)
        {
            year = yearGroup;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Person aPerson = new Person("Andrew");
            aPerson.introduceMyself();
        }
    }
}