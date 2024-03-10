
# class Member:
#     def __init__(self) :
#         self.name = "Abdellah"

# member_one = Member()
# member_two = Member()
# member_three = Member()




class Member:
    def __init__(self,first_Name,midlle_Name,last_Name) :
        self.fname = first_Name
        self.mname = midlle_Name
        self.lname = last_Name

member_one = Member('Osama','Elzero','eng')
member_two = Member('Mohamed','eng','Elsayed')
member_three = Member('Abdellah','abdo','nsila')



print(member_one.fname,member_one.mname,member_one.lname)
print(member_two.fname,member_two.mname,member_two.lname)
print(member_three.fname,member_three.mname,member_three.lname)
