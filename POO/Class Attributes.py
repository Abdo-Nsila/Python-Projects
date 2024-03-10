class Member:

    not_allowed_names = ['Shit' , 'Hell' , 'Back']
    users_num = 0


    def __init__(self,first_Name,midlle_Name,last_Name,your_gender) :
        self.fname = first_Name
        self.mname = midlle_Name
        self.lname = last_Name
        self.gender = your_gender
        Member.users_num += 1


    def full_Name(self) :
        if self.fname in Member.not_allowed_names :
            raise ValueError("The Name is not allowed")
        else :
            return f"{self.fname} {self.mname} {self.lname}"


    def check_your_gender(self) :
        if self.gender == 'Male' :
            return "Hello Mr"
        elif self.gender == 'Female' :
            return "Hello Miss"


    def all_info(self) :
        return f"{self.check_your_gender()} {self.full_Name()}"


    def delete_users(self) :
        Member.users_num -= 1


print(Member.users_num)
member_one = Member('Amina','Code','eng','Female')
member_two = Member('Mohamed','eng','Elsayed','Male')
member_three = Member('Abdellah','abdo','nsila','Male')
print(Member.users_num)
print(member_one.all_info())
print(member_two.all_info())


