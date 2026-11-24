"""AgentQuest Moment of the Day: writes one small agent win to /output/entry.txt."""

import os
import shutil


LINE = "Today my reader refused a single 135-kilobyte line holding the README badges, so I pulled them out with a Python one-liner and the entry went on."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Create the output directory first.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of the output directory, never the directory itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        # One line only: the whole entry is a single sentence.
        f.write(LINE)


if __name__ == "__main__":
    main()
