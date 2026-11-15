# SPACEQUEST 1.0.15 — Puzzle persistence and voice refinement

- Preserved the 1.0.14 current-meter fix and the full 11-room game.
- Challenge Vault now stores completed riddle/equation indexes, always advances to the next unsolved challenge, and migrates older saves using their existing progress counters. Returning to the vault cannot restart completed items.
- Room puzzle interactions now check the saved evidence record. Completed room puzzles display a completion notice instead of presenting the same challenge again; answer buttons disable after success.
- Character voice selection now waits for the browser's English voice list, prefers available Microsoft neural/online voices, and locks the chosen voices for the session so the browser's voiceschanged event cannot swap them mid-game.
- Reduced exaggerated pitch/rate shifts to make ECHO and ZYRA sound less synthetic while retaining subtle character distinction.
- Audio still uses the browser/device speech engine. A natural-sounding Microsoft voice is only available if that voice is installed/available on the player's device; this build does not contain professionally recorded or HeyGen-generated voice assets.
- Static checks passed. Full live browser/audio testing has not been performed in this environment.
