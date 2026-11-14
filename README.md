# Perfect Hashing

> **Course:** COSC 607 Algorithm Design Techniques · MSc, Khalifa University

![Python](https://img.shields.io/badge/python-3-blue.svg) ![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)

Perfect hashing in Python. The script builds a two-level hash table for a static set of integer keys so that every key ends up in its own slot with no collisions, which makes every lookup take constant time.

## What it does

- Reads `n` keys from `test-in.txt`.
- **First level**: hashes the keys into a table of size `8n` with a universal hash function `h(k) = ((a·k + b) mod p) mod m`, where `p` is a random prime between 10,000 and 20,000, `a` is in `[1, p-1]` and `b` is in `[0, p-1]`.
- **Second level**: a slot that receives `n_j` keys gets its own table of size `n_j²`. New random parameters are drawn until each key lands in an empty second-level slot.
- Writes the hash parameters and the final position of every key to `test-out.txt`.

## Input and output format

`test-in.txt`: the number of keys on the first line, then one key per line. The included example:

```
5
65
12
2
87
875
```

`test-out.txt` is written in three parts:

1. One line `m a b`: the first-level table size (`8n`) and hash parameters.
2. `8n` lines `m_j a_j b_j`: the size and parameters of each second-level table (`0 0 0` for empty slots).
3. `n` lines `key i j`: each key with its first-level slot `i` and second-level slot `j`.

For the example input, the included output starts with `40 5566 4860` (a 40-slot first-level table) and places the keys as follows:

| Key | First-level slot | Second-level slot |
| --- | --- | --- |
| 65 | 23 | 0 |
| 12 | 0 | 0 |
| 2 | 14 | 0 |
| 87 | 25 | 0 |
| 875 | 28 | 0 |

Parameters are random, so each run produces different values.

## Project structure

| File | Contents |
| --- | --- |
| `perfect-hash.py` | Two-level perfect hashing script |
| `test-in.txt` | Example input (5 keys) |
| `test-out.txt` | Output from a run on the example input |

## Getting started

Requirements: Python 3 (standard library only).

```bash
python perfect-hash.py
```

Run it from the repository folder. It reads `test-in.txt` and overwrites `test-out.txt`.

## Tech

Python 3 (standard library).

## License

Licensed under the Apache License 2.0; see [LICENSE](LICENSE).
