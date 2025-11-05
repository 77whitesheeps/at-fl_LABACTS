class MooreMachine:
    def __init__(self):
        # State transition table:
        self.state_transitions = {
            'A': {'0': ('A', 'A'), '1': ('B', 'B')},
            'B': {'0': ('C', 'A'), '1': ('D', 'B')},
            'C': {'0': ('D', 'C'), '1': ('B', 'B')},
            'D': {'0': ('B', 'B'), '1': ('C', 'C')},
            'E': {'0': ('D', 'C'), '1': ('E', 'C')}
        }

        # Initial (start) state
        self.initial_state = 'A'
        self.current_state = self.initial_state

    def reset_machine(self, start_state=None):
        """Reset the machine to the start or a given state."""
        self.current_state = start_state if start_state else self.initial_state

    def process(self, input_sequence):
        """
        Process a binary input sequence (string of 0s and 1s)
        and return the corresponding output sequence.
        """
        output_sequence = []

        for symbol in input_sequence:
            if symbol not in ('0', '1'):
                return None 
            
            next_state, output_symbol = self.state_transitions[self.current_state][symbol]
            output_sequence.append(output_symbol)
            self.current_state = next_state

        return ''.join(output_sequence)

    def run_tests(self, test_sequences):
        """Run multiple input test sequences and print the results."""
        print("Testing Moore Machine:\n")
        for sequence in test_sequences:
            self.reset_machine()
            output = self.process(sequence)
            if output is not None:
                print(f"Input: {sequence:<10} → Output: {output}")
            else:
                print(f"Input: {sequence:<10} → Invalid input sequence")

# Execute if run directly
if __name__ == "__main__":
    moore_machine = MooreMachine()
    moore_machine.run_tests(["00110", "11001", "1010110", "101111"])

    # Manual user test
    print("\nTry your own input:")
    user_input = input("Enter binary input (0s and 1s): ").strip()
    moore_machine.reset_machine()
    result = moore_machine.process(user_input)
    if result is not None:
        print(f"Output: {result}")
    else:
        print("Invalid input — only 0s and 1s are allowed.")