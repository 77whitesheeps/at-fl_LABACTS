#ACTIVITY 1 NUMBER 1

from base_class import Authentication

transition_table = {
    "a":{"0": "a", "1": "b"},
    "b":{"0": "c", "1": "a"},
    "c":{"0": "b", "1": "c"}
}

dfa = Authentication(start_state= "a", accept_state= {"c"}, transition_table=transition_table)

user_input = input("Enter a binary string (0s and 1s): ")

result = dfa.check_string(user_input)

print(result)

#EXAMPLES:
#Accepted: {10}, {1000}, {1110}
#Rejected: {1}, {01}, {011}