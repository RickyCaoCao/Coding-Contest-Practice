#-------------------------------------------------------------------------------
# Name:        ACSL 2
# Purpose:
#
# Author:      Richard Cao
#
# Created:     06-02-2015
# Copyright:   (c) Richard Cao 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
##test_line = "(ADD (EXP -3 2) (SQR 5) (SUB 6 2) (MULT 6 7 -2 3) (DIV 15 5))"
##another_test_line ="(MULT (ADD 1 4 3) (EXP 2 -3) (MULT 1 3 5) (DIV 15 3) (SUB 9 2) (ADD 5 7 -9) (SUB 2 1))"

expression = input("Input the LISP Function.")
##expression = another_test_line
expression_list = expression.split("(")
##print (expression_list)
expression_beginning = expression_list[1]
expression_list = expression_list[2:]
##print (expression_list)
##print (expression_beginning)
new_expression_list = []
for i in expression_list:
    i = "(" + i[:-2] + ")"
    new_expression_list.append(i)
##print (new_expression_list)

input_times = 0
while input_times < 5:
    input_times += 1
    input_command = input("Enter command.")
    if input_command == "COUNT":
        print (len(new_expression_list))
    elif input_command == "MAXIMUM":
        max_length = 0
        for i in new_expression_list:
            sublist = i.split()
            list_length = len(sublist)
            if list_length > max_length:
                max_length = list_length
                some_string = i
        some_string = some_string
        print(some_string)
    else:
        type_of_command = input_command[:-4]
        first_value = int(input_command[-3])
        second_value = int(input_command[-1])
        ##print (type_of_command)
        ##print (first_value)
        ##print (second_value)
        if type_of_command == "REMOVE":
            removed_list = new_expression_list[:first_value-1]
            removed_list.extend(new_expression_list[second_value:])
            removed_list = " ".join(removed_list)
            print ("(" + expression_beginning + removed_list + ")")
        elif type_of_command == "REVERSE":
            old_reversed_part = new_expression_list[first_value-1 :second_value]
            new_reversed_part = []
            for i in old_reversed_part:
                new_reversed_part.append(old_reversed_part[-1])
                old_reversed_part = old_reversed_part[:-1]
            reversed_list = new_expression_list[:first_value-1]
            reversed_list.extend(new_reversed_part)
            reversed_list.extend(new_expression_list[second_value:])
            reversed_list = " ".join(reversed_list)
            print ("(" + expression_beginning + reversed_list + ")")
        elif type_of_command == "SORT":
            sorted_part = new_expression_list[first_value-1 :second_value]
            sorted_part.sort()
            sorted_list = new_expression_list[:first_value-1]
            sorted_list.extend(sorted_part)
            sorted_list.extend(new_expression_list[second_value:])
            sorted_list = " ".join(sorted_list)
            print ("(" + expression_beginning + sorted_list + ")")
        else:
            print ("ERROR")

