# parent class Organizations on campus
class Organization:
    def __init__(self, name, number_of_members, president, mode_of_leadership_selection, Unique_ID): 
        self.name = name
        self.number_of_members = number_of_members
        self.president = president
        self.mode_of_leadership_selection = mode_of_leadership_selection
        self.Unique_ID = Unique_ID

# Student subclass inheriting features of organization
class Denomination (Organization):
    def __init__(self, name, number_of_members, president, mode_of_leadership_selection, Unique_ID, meeting_day, venue, mother_association): 
        super().__init__(name, number_of_members, president, mode_of_leadership_selection, Unique_ID)
        self.meeting_day = meeting_day
        self.venue = venue
        self.mother_association = mother_association
        
# displaying details of denomination
    def denominations(self):
        print("------DENOMINATION DETAILS-----")
        print("Name :", self.name)
        print("Number of Members :", self.number_of_members)
        print("President :", self.president)
        print("Mode of leadership selection :", self.mode_of_leadership_selection)
        print("Unique ID :", self.Unique_ID)
        print("Meeting day :", self.meeting_day)
        print("Venue :", self.venue)
        print("Mother Association :", self.mother_association)
        print()

class UTAG (Organization):
    def __init__(self, name, number_of_members, president, mode_of_leadership_selection, Unique_ID, meeting_day, venue, campus): 
        super().__init__(name, number_of_members, president, mode_of_leadership_selection, Unique_ID)
        self.meeting_day = meeting_day
        self.venue = venue
        self.campus = campus
        
        
# displaying details of UTAG
    def utag(self):
        print("------UTAG DETAILS------")
        print("Name :", self.name)
        print("Number of Members :", self.number_of_members)
        print("President :", self.president)
        print("Mode of leadership selection :", self.mode_of_leadership_selection)
        print("Unique ID :", self.Unique_ID)
        print("Meeting day :", self.meeting_day)
        print("Venue :", self.venue)
        print("Mother Association :", self.campus)
        print()
class TEWU (Organization):
    def __init__(self, name, number_of_members, president, mode_of_leadership_selection, Unique_ID, meeting_day, venue, campus): 
        super().__init__(name, number_of_members, president, mode_of_leadership_selection, Unique_ID)
        self.meeting_day = meeting_day
        self.venue = venue
        self.campus = campus
        
        
# displaying details of TEWU
    def tewu(self):
        print("------TEWU DETAILS------")
        print("Name :", self.name)
        print("Number of Members :", self.number_of_members)
        print("President :", self.president)
        print("Mode of leadership selection :", self.mode_of_leadership_selection)
        print("Unique ID :", self.Unique_ID)
        print("Meeting day :", self.meeting_day)
        print("Venue :", self.venue)
        print("Mother Association :", self.campus)
        

Denomination1 = Denomination("PENSA", 76, "Anim Addo","Appointment", "UENR 222", "Sundays", "Getfund Basement", "Fiapre Church of Pentecost") 
UTAG1 = UTAG("UENR UTAG", 54, "Dr. Banahene", "Elections", "UTAG UENR 31", "Fridays","LTS 2", "UENR")
TEWU1 = TEWU("UENR TEWU", 91, "Dr. Afriyie Akoto", "Elections", "TEWU UENR 31", "Fridays","SH 5", "UENR")


print(Denomination1.denominations()) 
print(UTAG1.utag()) 
print(TEWU1.tewu())
