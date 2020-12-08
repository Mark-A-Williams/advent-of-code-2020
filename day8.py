from helpers import *

class BootCodeInstruction:
    def __init__(self, id: int, code: str, value: int) -> None:
        if (code not in ["acc", "jmp", "nop"]):
            raise ValueError("Invalid code provided: {0}".format(code))
        self.id = id
        self.code = code
        self.value = value

class BootCodeProgram:
    currentIndex = 0
    accumulator = 0
    visitedInstructions: list[int] = []

    def __init__(self, instructions: list[BootCodeInstruction]) -> None:
        self.instructions = instructions

    def execute(self) -> int:
        numberOfInstructions = len(self.instructions)
        while self.currentIndex not in self.visitedInstructions:
            if self.currentIndex < numberOfInstructions:
                nextInstruction = self.instructions[self.currentIndex]
                self.executeInstruction(nextInstruction)
            else:
                print(f"Program terminated at instruction {self.currentIndex}")
                break
        
        return self.accumulator

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

def main():
    instructions: list[BootCodeInstruction] = []
    for (counter, line) in enumerate(getFileLines(8)):
        [code, value] = line.split(" ")
        instructions.append(BootCodeInstruction(counter, code, int(value)))

    program = BootCodeProgram(instructions)

    # Part 1

    timer = ExecutionTimer()
    result = program.execute()
    print("Day 8 part 1 solution: {0}".format(result))
    timer.stop()

if __name__ == "__main__":
    main()