# GR8-1 Homebrew CPU

The GR8-1 is the first in a series of 8-bit homebrew CPUs I'm designing from scratch with 74 series logic, aiming to push the limits of speed in an 8-bit architecture. The architecture will have a 4-stage pipeline and 2 execution units; ALU and a Register Bank. Why 8-bit? Because 16-bit might be faster, but squeezing every ounce of performance out of 8 bits is way more fun (and a bit of a laugh). 

The goal for this architecture is to get at the very least 0.6 instructions per clock. The CPU will decode variable length instructions up to 4 bytes long. To maximize performance both the Fetch Unit and Decoder are double issued [working in the rising and falling edge of the clock](https://youtube.com/shorts/t5TkMNN1aw8?feature=share).  Also, there is some special consideration on how the branching will be executed to avoid emptying the pipeline.

The next step would be to double down on the multiple execution unit idea. Building on from the GR8-1, the GR8-2 will be a massive improvement in math related tasks. This should have a similar structure to the GR8-1, keeping or increasing the size of the pipeline, while also incorporating a dual ALU design and instruction caching. The aim is to be able to crunch through as many 8-bit operations as possible. Also bringing some memory access optimizations to keep up with the added compute power.

This architecture’s goal is to get as close as possible to 1 instruction per clock. Should also add new instructions while staying compatible with the original GR8-1. These instructions will address deficiencies in the GR8-1, mainly related to hardware multiplication and division.

![Architecture Overview](Documentation/Images/Architecture_Overview.png)

## GR8-1 To Do List
- [x] General Schematic of the Architecture
- [ ] Instruction Set Architecture
- [ ] Architecture Overview Document
- [ ] Fetch Unit
  - [x] Edge Detect Circuit
  - [ ] Program Counter
  - [ ] Memory Address Register
- [ ] Decoder
  - [ ] Variable Length Instruction Circuit
  - [ ] Halt Circuit
  - [ ] Unconditional Jump Handler
  - [ ] Conditional Jump Handler
- [ ] Scheduler
  - [ ] Address Decoder
  - [ ] ALU
    - [x] Control Unit
    - [ ] 74LS181 Circuit
    - [ ] Flag Registers
    - [x] 4 x 8bit Registers
  - [ ] Register Bank
    - [ ] Write Queue  

- **Licenses**: CERN-OHL-S v2 (hardware), GPL 3.0 (software).

