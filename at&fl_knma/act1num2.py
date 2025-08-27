#ACTIVITY 1 NUMBER 2

from base_class import Authentication

transition_table= {
    "q0":{"a": "q1", "b": "q2"},
    "q1":{"a": "q0", "b": "q3"},
    "q2":{"a": "q3", "b": "q0"},
    "q3":{"a": "q2", "b": "q1"}
}

dfa = Authentication(start_state= "q0", accept_state={"q3"}, transition_table=transition_table)

user_input = input("Enter a string (a's and b's): ")

result = dfa.check_string(user_input)
print(result)

#EXAMPLES:
#Accepted: {ab}, {abbb}, {ba}
#Rejected: {a}, {aba}, {bba}