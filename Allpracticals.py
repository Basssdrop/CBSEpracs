def fizzbuzz():
    print("\n".join(["FizzBuzz" if num % 15 == 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else str(num) for num in range(1, 51)]))

def i_occurence():
    print([i for i in range(len("Mississippi")) if list("Mississippi")[i] == 'i'])
        
def npp_sum():
    ns = pes = pos = 0
    for n in iter(lambda: int(input("Enter the number: ")), 0):
        if n < 0: ns += n
        elif n % 2: pos += n
        else: pes += n
    print(f"Negative sum: {ns}, Positive even sum: {pes}, Positive odd sum: {pos}")
    
def twisted_pig_latin():
    print(" ".join([word[1:] + word[:1] + "ay" for word in input("Enter a word(s): ").split()]))
    
def largest_number():
    print(max([int(input("Enter a number : ")) for _ in range(3)]))
    
def common_data():
    print(bool(set(input("Enter first list: ").split()) & set(input("Enter second list: ").split())))
    
def swap_two():
    print((lambda a, b: b[:2] + a[2:] + " " + a[:2] + b[2:])(input("Enter first string: "), input("Enter second string: ")))
    
def reverse_if_4():
    print((lambda s: s[::-1] if len(s) % 4 == 0 else s)(input("Enter a string: ")))
    
def map_two_lists_into_dictionary():
    print(dict(zip(input("Enter keys: ").split(), input("Enter values: ").split())))
    
def check_if_key_exist():
    print((lambda d, k: k in d)({'1':10,'2':20,'3':30,'4':40,'5':50,'6':60}, input("Enter a key: ")))      
    
def element_list_search():
    print((lambda l, e: e in l)(list(map(float, (input("Enter a list of numbers separated by a space")).split()), int(input("Enter a number: ")))))
    
def student_dict():
    print([student['name'] for student in [{'roll': input("Enter roll number: "), 'name': input("Enter name: "), 'marks': int(input("Enter marks: "))} for _ in range(int(input("Enter the number of students: ")))] if student['marks'] > 75])
    
def smallest_larget_list():
    print((lambda l: (min(l), max(l)))(list(map(int, input("Enter a list of numbers separated by a space: ").split()))))
    
def predefined_dict():
    print((lambda d: (d, d.get(3), {k: v for k, v in d.items() if k != 2}, {k: v for k, v in d.items() if k != 1}))({1: 'prep', 2: 'For', 3:'you'}))
    
def predefined_list():
    print((lambda l: (l, len(l), [i for i in range(1, 4)], [i for i in range(1, 4)] + [2], [i for i in range(1, 4)] + [2] if 2 in [i for i in range(1, 4)] + [2] else [i for i in range(1, 4)] + [2]))([10, 20, 14]))
    
def predefined_function():
    print((lambda l: (l, l + [8, 'Geeks', 'Always']))([1, 2, 3, 4]))
    
def nested_list():
    print((lambda l: (l, l[0][0], l[0][1]))([['prep', 'School'], ['for','you']]))
    
def slicer():
    print((lambda s: (s[:3], s[1:4]))('GEETHA'))
    
def mixed_tuple():
    print((lambda t, t1: (t, t + t1))((10,20,30,40), ('P','R','E','P')))
    
def sort_tuple():
    print((lambda x, y: (sorted(x), sorted(y)))((('q', 'w', 'e', 'r', 't', 'y'), (1,2,3,10,6))))

# Dictionary with all the function references
func_references = {
    "fizzbuzz": fizzbuzz,
    "i_occurence": i_occurence,
    "npp_sum": npp_sum,
    "twisted_pig_latin": twisted_pig_latin,
    "largest_number": largest_number,
    "common_data": common_data,
    "swap_two": swap_two,
    "reverse_if_4": reverse_if_4,
    "map_two_lists_into_dictionary": map_two_lists_into_dictionary,
    "check_if_key_exist": check_if_key_exist,
    "element_list_search": element_list_search,
    "student_dict": student_dict,
    "smallest_larget_list": smallest_larget_list,
    "predefined_dict": predefined_dict,
    "predefined_list": predefined_list,
    "predefined_function": predefined_function,
    "nested_list": nested_list,
    "slicer": slicer,
    "mixed_tuple": mixed_tuple,
    "sort_tuple": sort_tuple
}

# Create a main function which asks the user to enter a key and bsed on that key, call the function in the dictionary
def main():
    while True:
        key = input("Enter a key: ")
        if key in func_references:
            func_references[key]()
        else:
            print("Invalid key")
        print("*"*64)
        print('\n'*2)
        
main()
