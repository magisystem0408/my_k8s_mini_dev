class Person {
  static final Person _singleton = new Person._internal();
  static final String _name = "MAMUSHI";

  static String get name => _name;

  factory Person(){
    return _singleton;
  }

  Person._internal();
}


void main() {
  Person person1 = Person();
  Person person2 = Person();
  if (person1 == person2) {
    print("same person");
  }
}

