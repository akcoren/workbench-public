#! /bin/python3

# STRINGS
print("Hello, world!")
print("""This string runs 
multiple lines!""")
print("This is " + "concatination")
print("\n")  # new line
print("Next line")


quote = "All is fair in love and war."

print(quote.upper())
print(quote.lower())
print(quote.title())
print(len(quote))

name = "Zurnaci"
age = 31
gpa = 3.1

print(int(age))
print(int(30.1))
print(int(gpa))

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1

print(age)

# SIMPLE FUNCTION


def who_am_i():  # no input parameter
    name = "Zurnaci"  # all variables are local
    age = 30
    print("My name is " + name + " and I am " + str(age) + " years old.")


who_am_i()
print(age)


def add_one_hundred(num):
    print(num+100)


add_one_hundred(100)


def add(x, y):
    print(x+y)


add(31, 7)


def multiply(x, y):
    return x*y


multi = multiply(7, 8)
print(multi)


def square_root(x):
    print(x ** 0.5)


square_root(64)


def nl():
    print("\n")


nl()

# BOOLEANS
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)

print(type(bool1))

# LOGICALS
greater_than = 7 > 3
less_than = 5 < 7
greater_than_or_equal_to = 7 >= 7
less_than_or_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7)  # True
test_and2 = (7 > 5) and (5 > 7)  # False
test_or = (7 > 5) or (5 < 7)  # True
test_or2 = (7 > 5) or (5 > 7)  # True

test_not = not True  # False

nl()

# CONDITIONALS


def drink(money):
    if money >= 2:
        return "You've got yourself a drink!"
    else:
        return "No drink for you!"


print(drink(3))
print(drink(1))


def alcohol(age, money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money."
    elif (age < 21) and (money >= 5):
        return "Nice try, kid!"
    else:
        return "You're too toung and too poor."


nl()
print(alcohol(21, 5))
print(alcohol(21, 4))
print(alcohol(20, 5))
print(alcohol(20, 4))

nl()

# LISTS - [] changable
movies = ["When Harry Met Sally", "The Hangover",
          "The Perks of Being a Wallflower", "The Exorcist"]
print(movies[0])
print(movies[1])
print(movies[2])
print(movies[3])

nl()

print(movies[1:3])  # 2. and 3. item, not including the last number
print(movies[1:])
print(movies[:1])
print(movies[-1])  # last item
print(movies[-2])  # the item before last item

print(len(movies))
movies.append("JAWS")  # appends to the end
print(movies)

movies.insert(2, "Hustle")  # inserts into the position 2 - 3rd item
print(movies)


movies.pop()  # removes the last item
print(movies)

movies.pop(0)  # removes the first item
print(movies)

amber_movies = ["Just Go With It", "50 First Date"]
our_favorite_movies = movies + amber_movies
print(our_favorite_movies)

# 2D list
grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
print(grades)

bobs_grade = grades[0][1]
print(bobs_grade)

grades[0][1] = 85
print(grades[0][1])

# TUPLES - () Do nat change
grades = ("a", "b", "c", "d", "f")
print(grades[1])


nl()
# LOOPING
# For loops
vegetables = ["cucumber", "spinach", "cabbage", "carrot"]
for x in vegetables:
    print(x)


# While loops
i = 1
while i < 10:
    print(i)
    i += 1


nl()

# ADVANCED STRINGS
my_name = "Berkay"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence."
print(sentence[:4])
print(sentence.split())  # default delimeter is space

sentence_split = sentence.split()
sentence_join = " ".join(sentence_split)
print(sentence_join)

quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                      hello                 "
print(too_much_space.strip())

print("A" in "Apple")  # True
print("a" in "Apple")  # False

letter = "A"
word = "Apple"
print(letter.lower() in word.lower())

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))
print("My favorite movie is %s." % movie)
print(f"My favorite movie is {movie}.")

# DICTIONARIES - {} key/value pairs
drinks = {"White Russion": 7, "Old Fashioned": 10, "Lemon Drop": 8} # Drink is key, price is value
print(drinks)

employees = { "Finance": ["Bob" , "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jummy Jr.", "Mort"]}
print(employees)

employees["Legal"] = ["Mr. Frond"] # new pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]})
print(employees)


drinks["White Russian"] = 8
print(drinks)
print(drinks.get("White Russian"))

