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

        public virtual void introduceMyself()
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

        public override void introduceMyself()
        {
            base.introduceMyself();
            Console.WriteLine("... and I am a teacher of " + this.subject);
        }
    }

    class Student : Person
    {
        private int year;

        public Student(string aName, int yearGroup) : base(aName)
        {
            year = yearGroup;
        }

        public override void introduceMyself()
        {
            base.introduceMyself();
            Console.Write("... and I am a student in year " + Convert.ToString(this.year));            
        }

    }

    class Program
    {
        static void Main(string[] args)
        {
            Person aPerson = new Person("Andrew");
            aPerson.introduceMyself();
            Teacher aTeacher = new Teacher("Mr Bramwell", "Computer Science");
            aTeacher.introduceMyself();
            Student aStudent = new Student("Noud", 12);
            aStudent.introduceMyself();
        }
    }
}