# Shell from Scratch

A minimal shell implementation built from scratch in Python as a learning exercise.

## Features

- **Interactive command prompt** with a REPL interface
- **Built-in commands** (more to be added):
  - `echo` - Print text
  - `cd` - Change working directory
  - `pwd` - Print working directory
  - `type` - Display command information
  - `exit` - Exit the shell

## Architecture

- `main.py` - Shell event loop that reads user input and dispatches to commands
- `commands/` - Command implementations with an abstract `Command` base class
- `utils.py` - Helper functions for parsing input and error handling

## Usage

```bash
python main.py
$ echo hello
$ pwd
$ exit
```

## Development

- **Python**: 3.14+
- **Package manager**: `uv`
- **Testing**: `pytest`
- **Linting**: `ruff`, `mypy`, `flake8`, `pylint`
