class MealyMachine:
    def __init__(self, states, start_state, transitions):
        self.states = states
        self.start_state = start_state
        self.transitions = transitions

    def process_input(self, input_string):
        current_state = self.start_state
        output = ""

        print("Input | Current State | Next State | Output")

        for symbol in input_string:
            transition = self.transitions.get((current_state, symbol))
            if transition is None:
                print(f"X Invalid transition from {current_state} on input '{symbol}'")
                return None

            next_state, out_symbol = transition
            print(f"  {symbol}   |       {current_state}       |     {next_state}     |   {out_symbol}")
            output += out_symbol
            current_state = next_state

        print(f"\nFinal Output: {output}")
        return output


class MealyDemo:
    def __init__(self):
        self.machine = MealyMachine(
            states={"A", "B", "C"},
            start_state="A",
            transitions={
                ("A", "0"): ("B", "b"),
                ("A", "1"): ("A", "b"),
                ("B", "0"): ("B", "b"),
                ("B", "1"): ("C", "a"), 
                ("C", "0"): ("B", "b"),
                ("C", "1"): ("A", "b"),
            }
        )

    def test(self, inputs):
        print("=== Mealy Machine ===\n")
        for input_str in inputs:
            print(f"\nProcessing input: {input_str}")
            output = self.machine.process_input(input_str)
            if output is not None:
                print(f"\nResult → Input: {input_str} | Output: {output}")
            print("-" * 40)


if __name__ == "__main__":
    test_inputs = ["10", "11", "101", "110", "110011", "011001"]
    demo = MealyDemo()
    demo.test(test_inputs)