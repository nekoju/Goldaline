#!/usr/bin/env python3

import re
import sys


def transpose(semitones, sign):
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    notes_map = {note: "" for note in notes}
    tail = []
    for _ in range(semitones):
        tail.append(notes.pop(len(notes) - 1 if sign == "-" else 0))
    notes_map = dict(
        zip(
            list(notes_map.keys()),
            tail + notes if sign == "-" else notes + tail,
        )
    )
    return notes_map

def multi_replace(pattern_map, base_regex, line):
    for pattern_in, replacement in pattern_map.items():
        pattern = rf" ({pattern_in + base_regex}) "
        print(pattern_in, pattern)
        # https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s15.html
        if re.match(pattern, line):
            print(pattern)
            print(f"Replacing {re.match(pattern, line).group(0)} with {replacement}")
            print("in " + line.strip())
            line = re.sub(pattern, "<><>" + replacement + r"\2 ", line)
            print("out " + line.strip())
    return re.sub(r'<><>(.*) ', r"\1", line)

def process_text(file, *args, **kwargs):
    notes_map = transpose(3, "+")
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    # figure out regex dict
    base_regex = r'(m)??(.+?)??'
    with open(file, "r") as file:
        for line in file:
            print(line + multi_replace(notes_map, base_regex, line))


def main():
    # out = transpose(3, "+")
    # for k, v in out.items():
    #     print(k + "->" + v)
    process_text("test.txt")


if __name__ == "__main__":
    main()
