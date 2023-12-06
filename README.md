# 🎰 State Machine-Based Vending Machine Project

This project involves the creation of a state machine to simulate the operation of a vending machine, which will have three products:

| Product | Price |
|---------|-------|
| A       | €0.50 |
| B       | €1.00 |
| C       | €2.00 |

Only coins of €0.50, €1, and €2 are accepted, up to a maximum amount of €3.50. The machine has 4 buttons (A, B, C, one for each product, and D for returning the remaining balance). The machine will allow multiple transactions as long as there is sufficient balance. The remaining balance will only be returned when the return button is pressed.

## 🌟 Features

The project will include the following features:
  - Accept keyboard inputs: simulating the insertion of coins and pressing buttons through a character string.
    - Visualize the behavior of the state machine step by step, indicating the state(s) it is in at each moment.
  - The state of the state machine (AF) will always indicate the available balance. In some cases, the AF can simultaneously be in a final state indicating the product to be dispensed or the "return action".

## 🚀 Usage
**INSTRUCTIONS FOR EXECUTING THE STATE MACHINE CODE**

1. **Prepare the Environment:**
   Make sure Python is installed on your system. You can download it and find installation instructions at [https://www.python.org/](https://www.python.org/).

2. **Prepare the Automaton File:**
   
   The definition of the automaton (alphabet, set of states, transition function, initial state, and set of final states) must be read from a text file. The automaton must be passed in the following format through a `.txt` file.

   **Mandatory File Format:**

  ```
  #total number of states state1 state2 …
  #number of final states finalState1 finalState2 …
  #total number of alphabet symbols symbol1 symbol2 … symbol n
  --TRANSITION TABLE--
  AS MANY ROWS AS STATES
  AS MANY COLUMNS AS ALPHABET SYMBOLS + 1 (empty string).
  Each column ends with the symbol #
  ```

  **Example:**
  ```
  #4 q00 q10 q20 qaa
  #1 qaa
  #3 1 2 a
  --TRANSITION TABLE—
  q10 # q20 # # q10 q20 qaa #
  ```

3. **Execute the Script:**
Open a terminal or command line.
Navigate to the directory containing the script and the 'archivo.txt' file.
Run the command: `python VendingMachine.py`.

4. **Using the Program:**
Once the script is running, you will be prompted to enter an input string.
Enter the input string you want the automaton to process.
The program will run the automaton based on the provided string and display the reached final states.

## Example of Operation

For the input string “152ac22bd1c2c”, the operation of the AF will be:

| Input  |   1   |   5   |   2   |   a   |   c   |   2   |   2   |   b   |   d   |   1   |   c   |   2   |   c   |
|--------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| States | {q00} | {q10} | {q15} | {q35} | {q30, qaa} | {q10, qcc} | {q30} | {q30} | {q20, qbb} | {q00, qdd} | {q10} | {q10} | {q30} | {q10, qcc} |

5. **Interpreting the Output:**
The program will print the final states reached after processing the input string through the automaton.
If an error occurs, such as an undefined transition, the program will print a corresponding error message.

Note: This script is designed for automata specifically defined with the expected structure in 'archivo.txt'. Ensure your automaton is correctly defined as per the script's requirements.

# 👏 Credits

This project was created by Pablo Seijo as part of the Automata Theory and Formal Languages course at ETSE (University of Santiago de Compostela).
