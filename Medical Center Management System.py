class Person:
    def __init__(self, id_number, full_name, phone, address, specialty=None):
        self.id_number = id_number
        self.full_name = full_name
        self.phone = phone
        self.address = address
        self.specialty = specialty

    def __str__(self):
        details = f"ID: {self.id_number}, Name: {self.full_name}, Phone: {self.phone}, Address: {self.address}"
        if self.specialty:
            details += f", Specialty: {self.specialty}"
        return details

class MedicalCenter:
    def __init__(self):
        self.doctors = {}
        self.patients = {}
        self.unique_id = 1

    def add_person(self, person_type):
        full_name = input(f"Enter {person_type}'s full name: ")
        phone = input(f"Enter {person_type}'s phone number: ")
        address = input(f"Enter {person_type}'s address: ")
        specialty = input(f"Enter {person_type}'s specialty: ") if person_type == "doctor" else None
        person = Person(self.unique_id, full_name, phone, address, specialty)
        if person_type == "doctor":
            self.doctors[self.unique_id] = person
        else:
            self.patients[self.unique_id] = person
        self.unique_id += 1
        print(f"{person_type.capitalize()} added successfully!")

    def list_people(self, person_type):
        print(f"List of {person_type.capitalize()}s:")
        people = self.doctors if person_type == "doctor" else self.patients
        for person in people.values():
            print(person)

    def run(self):
        while True:
            option = input("\n1. Add Doctor\n2. Add Patient\n3. View Doctors\n4. View Patients\n5. Exit\nChoose an option: ")
            if option == '1':
                self.add_person("doctor")
            elif option == '2':
                self.add_person("patient")
            elif option == '3':
                self.list_people("doctor")
            elif option == '4':
                self.list_people("patient")
            elif option == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Running the program
medical_center = MedicalCenter()
medical_center.run()