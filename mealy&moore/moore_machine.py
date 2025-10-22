class MooreMachine:
    def __init__(self, states, start_state, output_map, transitions):
        self.states = states
        self.start_state = start_state
        self.output_map = output_map
        self.transitions = transitions

    def process_input(self, input_string):
        current_state = self.start_state
        output = self.output_map[current_state]

        for symbol in input_string:
            next_state = self.transitions.get((current_state, symbol))
            if next_state is None:
                print(f"Invalid transition from state {current_state} on input '{symbol}'")
                return None

            current_state = next_state
            output += self.output_map[current_state]

        return output


class MooreDemo:
    def __init__(self):
        self.machine = MooreMachine(
            states={"A_b", "B_b", "B_a", "C_b"},
            start_state="A_b",
            output_map={
                "A_b": "b",
                "B_b": "b",
                "B_a": "a",
                "C_b": "b"
            },
            transitions={
                ("A_b", "0"): "B_b",
                ("A_b", "1"): "C_b",

                ("B_b", "0"): "B_b",
                ("B_b", "1"): "B_a",

                ("B_a", "0"): "B_b",
                ("B_a", "1"): "C_b",

                ("C_b", "0"): "B_b",
                ("C_b", "1"): "C_b",
            }
        )

    def test(self, test_inputs):
        print("=== Moore Machine ===\n")
        for input_str in test_inputs:
            output = self.machine.process_input(input_str)
            if output is not None:
                print(f"Input: {input_str} → Output: {output}")
            else:
                print(f"Input: {input_str} → Invalid sequence")
        print()


if __name__ == "__main__":
    test_inputs = ["10", "11", "101", "110", "110011", "011001"]
    demo = MooreDemo()
    demo.test(test_inputs)