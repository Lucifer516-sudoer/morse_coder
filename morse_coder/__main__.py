import typer
from rich import print
from rich.table import Table

from morse_coder._converter import CHAR_TO_MORSE, convert_to_morse, convert_to_text

app = typer.Typer()


@app.command("encode")
def encode_to_morse(message: str):
    print(f"[bold red underline]Morse code[/]:\n{convert_to_morse(text=message)}")


@app.command("decode")
def decode_to_text(morse: str):
    print(f"[bold red underline]Decoded Text[/]:\n{convert_to_text(morse=morse)}")


@app.command("morse-keys")
def all_keys():
    table = Table(show_lines=True, title="[bold blue italic]Morse Codes[/]")
    table.add_column("[bold yellow]Character[/]", style="bold italic cyan")
    table.add_column("[bold blue]Morse[/]", style="bold")
    for key, val in CHAR_TO_MORSE.items():
        table.add_row(key, val)
    print(table)


if __name__ == "__main__":
    app()
