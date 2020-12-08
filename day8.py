from helpers import *

class BootCodeInstruction:
    def __init__(self, id: int, code: str, value: int) -> None:
        if (code not in ["acc", "jmp", "nop"]):
            raise ValueError("Invalid code provided: {0}".format(code))
        self.id = id
        self.code = code
        self.value = value

class BootCodeProgram:
    def __init__(self, instructions: list[BootCodeInstruction]) -> None:
        self.instructions = instructions

    def execute(self, handleDuplicates = True) -> int:
        self.reset()
        numberOfInstructions = len(self.instructions)
        while self.currentIndex not in self.visitedInstructions:
            if self.currentIndex < numberOfInstructions:
                nextInstruction = self.instructions[self.currentIndex]
                self.executeInstruction(nextInstruction)
            else:
                return self.accumulator

        if handleDuplicates:
            return self.accumulator
        else:
            raise OverflowError("Infinite loop")

    def executeInstruction(self, instruction: BootCodeInstruction) -> None:
        self.visitedInstructions.append(self.currentIndex)

        if instruction.code == "nop":
            self.currentIndex += 1
        elif instruction.code == "acc":
            self.currentIndex += 1
            self.accumulator += instruction.value
        elif instruction.code == "jmp":
            self.currentIndex += instruction.value
        else:
            raise ValueError("Invalid instruction code {0}".format(instruction.code))

    def reset(self):
        # these properties are undefined until here which seems a bit cursed
        self.currentIndex = 0
        self.accumulator = 0
        self.visitedInstructions = []

def initialiseProgramFromData() -> BootCodeProgram:
    data = getFileLines(8)

    instructions: list[BootCodeInstruction] = []
    for (counter, line) in enumerate(data):
        [code, value] = line.split(" ")
        instructions.append(BootCodeInstruction(counter, code, int(value)))

    return BootCodeProgram(instructions)

def main():
    program = initialiseProgramFromData()

    # Part 1

    timer = ExecutionTimer()
    result = program.execute()
    print(f"Day 8 part 1 solution: {result}")
    timer.stop()

    # Part 2

    timer = ExecutionTimer()
    part2Result: int or None = None
    for i in range(len(program.instructions)):
        if program.instructions[i].code == "jmp":
            program.instructions[i].code = "nop"
            try:
                part2Result = program.execute(False)
                break
            except OverflowError:
                pass
                program.instructions[i].code = "jmp"
        elif program.instructions[i].code == "nop":
            program.instructions[i].code = "jmp"
            try:
                part2Result = program.execute(False)
                break
            except OverflowError:
                pass
                program.instructions[i].code = "nop"

    if part2Result is not None:
        print(f"Day 8 part 2 solution: {part2Result}")
    timer.stop()

if __name__ == "__main__":
    main()
