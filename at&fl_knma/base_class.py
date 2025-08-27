#BASE CLASS

class Accepted:
    def __init__(self,string):
        self.string = string

    def __str__(self):
        return f"Accepted: {self.string}"
    
class Rejected:
    def __init__(self,string):
        self.string = string

    def __str__(self):
        return f"Rejected: {self.string}"

class Authentication:
    def __init__(self, start_state, accept_state, transition_table):
        self.start_state = start_state
        self.accept_state = accept_state
        self.transition_table = transition_table

    def check_string(self, string):
        state = self.start_state
        for char in string:
            if char not in self.transition_table[state]:
                return Rejected(string) #INVALID SYMBOL
            
        if state in self.accept_state:
            return Accepted(string)
        else:
            return Rejected(string)