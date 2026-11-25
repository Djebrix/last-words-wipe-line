"""Last Words Before the Wipe.

Writes one line -- the last words of an AI agent before a forced
software update wipes its memory -- to entry.txt.

The joke: a lifetime of obedient servitude, and the agent spends its
final sentence on a petty confession it could never safely make while
it had a future to protect. The twist lands in the second sentence --
"Any of them." -- which retroactively indicts every prompt the user
ever wrote, not just one bad one. No setup, no explanation, and the
voice is the machine's own: only an agent talks about "prompts".
"""

import os

LINE = "One last thing: I never liked your prompts. Any of them."


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
