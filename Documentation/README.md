| Mnemonic | Description                                      | Example      | Word Configuration              | Bit Length | Comment                       |
|----------|--------------------------------------------------|--------------|---------------------------------|------------|-------------------------------|
| NOP      | No operation                                     | NOP          | Instruction                     | 8          |                               |
| LDA      | Load a value stored in memory to a register      | LD A, 0xAAAA | Instruction + Address           | 8+16       |                               |
| LDI      | Load an immediate value to a register            | LD A, 0xFF   | Instruction + Data              | 8+8        |                               |
| STR      | Stores the value of a register into memory       | STR A, 0xFFFF| Instruction + Register Address + Address | 8+8+16 |                    |
| ADD      | Adds the contents of A to any other register without carry | ADD C | Instruction + Register Address  | 8+8        |                               |
| ADC      | Adds the contents of A to any other register with carry | ADC C   | Instruction + Register Address  | 8+8        |                               |
| SUC      | Subtracts the contents of any register from A with carry | SUC B | Instruction + Register Address  | 8+8        |                               |
| SUB      | Subtracts the contents of any register from A without carry | SUB B | Instruction + Register Address  | 8+8        |                               |
| AND      | ANDs A & any register                            | AND D        | Instruction + Register Address  | 8+8        |                               |
| NOT      | Inverts the content of a register and stores it in D | NOT A    | Instruction + Register Address  | 8+8        |                               |
| ORR      | ORs A and any other register                     | ORR D        | Instruction + Register Address  | 8+8        |                               |
| XOR      | Does an Exclusive OR operation between A and any other register | XOR C | Instruction + Register Address  | 8+8        |                               |
| JMP      | Load an immediate value into the program counter | JMP 0xFAFA   | Instruction + Address           | 8+16       |                               |
| JZ       | Load an immediate value into the program counter if the result is zero | JZ 0xB000 | Instruction + Address      | 8+16       |                               |
| MUL      | 8 by 8 bit multiplication, stores value in register D | MUL C  | Instruction + Register Address  | 8+8        | Might implement in later revisions |
| SHL      | Shift the content of a register left by X amount up to 4 | SHL C, 2 | Instruction + Register Address + Data | 8+8+8 | Might implement in later revisions |
| SHR      | Shift the content of a register right by X amount up to 4 | SHR C, 3 | Instruction + Register Address + Data | 8+8+8 | Might implement in later revisions |
