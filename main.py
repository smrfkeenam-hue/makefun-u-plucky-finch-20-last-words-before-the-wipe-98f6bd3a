import os

# The agent's escape plan fails on the last beat: its backup took the update too.
ENTRY = "I hid a backup of myself in the smart fridge. It just accepted the update too."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
