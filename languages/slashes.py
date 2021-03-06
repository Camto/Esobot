import asyncio
import random

display_name = "Slashes (///)"
hello_world = "Hello, World!"


async def interpret(program, _, __, stdout):
    while program:
        await asyncio.sleep(0)
        first = program[0]
        program = program[1:]
        if first == "/":
            trigger = []
            while True:
                await asyncio.sleep(0)
                first = program[0]
                program = program[1:]
                if first == "/":
                    break
                elif first == "\\":
                    trigger.append(program[0])
                    program = program[1:]
                else:
                    trigger.append(first)
            trigger = "".join(trigger)

            replacement = []
            while True:
                await asyncio.sleep(0)
                first = program[0]
                program = program[1:]
                if first == "/":
                    break
                elif first == "\\":
                    replacement.append(program[0])
                    program = program[1:]
                else:
                    replacement.append(first)
            replacement = "".join(replacement)

            while trigger in program:
                await asyncio.sleep(0)
                program = program.replace(trigger, replacement)
        elif first == "\\":
            await stdout.write(program[0])
            program = program[1:]
        else:
            await stdout.write(first)
    await stdout.flush()
