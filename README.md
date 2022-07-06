Agamdeep Singh 2021306
Ankit Singh 2021450
Siddharth Gupta 2021355

We have implemented a simple assembler in python which takes input from a text file containing instructions according to the given ISA and generates the corresponding binary.

We made a lists for storing the instructions as well as their line numbers which were required to identify which instruction had produced an error in case of any errors.
We also removed the blank spaces from the instructions using the strip() function and stored their indexes as required for the memory addresses for labels and variables.

We then iterated over the instructions and checked for the various errors mentioned in the guidelines as well as some other errors and printed an error message along with the line number for the encountered errors.
In case no error is encountered, the assembler code generates binary codes for each instruction using the dictionaries which contain the key:value pairs as instruction:opcode pairs.

Thus, our assembler performs the function expected and generates the binary codes for the given instructions.
