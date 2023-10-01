import uuid

# input stage
name = input("What is your name : ")
fname = input("What is your father's name : ")
mname = input("What is your mother's name : ")
mobilenumber = input("What is your mobile number: ")
email = input("what is your email: ")
aadhaarnumber = input("what is your aadhaar number: ")
h_edu = input("what is your higher education: ")
h_edu_school = input("what is your higher education school: ")
year_of_h_edu = input("what is your passing year for higher education: ") 

# processing and output stage
# Registration Number generate 
registration_id = uuid.uuid4()
print()
print()
print('⸻' * 125)
print("Hi ", name, "Your Registration Number is : " , registration_id)
print('⸻' * 125)
print("Father's Name: ", fname)
print("Mother's Name: ", mname)
print('⸻' * 125)
print("Mobile : ", mobilenumber, "| email : ", email)