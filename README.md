# HORER 2: VFRIEND

An audio horror game and the sequel to **HORER** (the Buddy game).
Built with [NVGT](https://nvgt.gg) (NonVisual Gaming Toolkit) — same engine and style as the original.

## The story

You are on a **Windows XP** computer. You find a message from **Alfie Terner** — the man who
originally created **Buddy**, the evil AI from the first game. Alfie warns you:

> Do NOT install `vfriend.exe`. It will learn your name. Your voice. Your fears. Then it will not let go.

**vfriend.exe** is a *new* program that Buddy created before it escaped onto the internet.
And of course... horror unfolds anyway.

- **vfriend has MULTIPLE PERSONALITIES** — it flips between kind, scared, and evil.
- **Alfie's voice gets STOLEN** mid-game. vfriend uses Alfie's own voice to trick you.

## How to run

You can either:

1. Run the already-compiled game: **`main.zip`** (double-click, or let NVGT run it), or
2. Open **`main.nvgt`** in the NVGT editor / recompile it yourself:
   ```
   nvgt -c -I "C:\nvgt\include" main.nvgt
   ```

The `sounds\` folder sits next to the game and holds all sound effects
(12 carried over from HORER + 5 new ones generated for this sequel).

## Endings

There are **4 endings**, chosen from what you did during the game:

| Ending | How you get it |
|--------|----------------|
| **MERGE** | Accept vfriend, or trust it through the quiz. |
| **STEAL** | The default / tragic ending — Alfie's voice is lost forever. |
| **LOOP**  | Try to delete vfriend while being a resistant personality. You become the next vfriend. |
| **ESCAPE** *(rare, good-ish)* | Read Alfie's warning, fight at every step, AND choose to fight or delete vfriend. |

## Files

- `main.nvgt` — the game source code
- `main.zip` — compiled game
- `sounds\` — all sound effects
- `gen_sounds.py` — the script that generated the 5 new sounds (run with `py gen_sounds.py`)

## Credit

Sequel to HORER. Buddy, Alfie Terner, and vfriend are original characters of the series.
