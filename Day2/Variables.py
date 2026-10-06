# Day 2: 30 Days of python programming
import math

first_name = "Ashish"
last_name = "Singh"
full_name = "Ashish Singh"
country = "India"
city = "Noida"
age = 26
year = 2000
is_married = False
is_light = False
num_one = 5;
num_two = 4;
total = num_one + num_two;
diff = num_two - num_one;
product = num_one * num_two;
division = num_one / num_two;
remainder = num_two % num_one;
exp = num_one ** num_two;
radius = 30;
area_of_circle =  math.pi * (radius ** 2);
circum_of_circle = 2 * math.pi * radius;
user_radius = input("Enter radius of circle - ");
area = math.pi * (int(user_radius) ** 2);

school, college, company = "OPS", "GU" , "NO"
print(school,college,company);

print(type(first_name));
print(type(last_name));
print(type(full_name));
print(type(country));
print(type(city));
print(type(age));
print(type(year));
print(type(is_married));
print(type(is_light));
print("Length of FirstName : ", len(first_name));
print(first_name == last_name);
print("Total of num_one and num_two : ", total);
print("Difference : ", diff);
print("exp : ", exp);
print("area_of_circle", area_of_circle);
print("circum_of_circle", circum_of_circle);
print("area : ", area);

