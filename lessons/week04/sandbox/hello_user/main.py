#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rich.console import Console
import typer
from hello_user import moreFun # load in the source file called moreFun.py

# create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def main(first: str = "", middle: str = "", last: str = ""):
    """Say hello to the person having a name of first, middle and last name"""
    console = Console()
    console.print(" Hello to;")
    console.print(f"\t First = {first}")
    console.print(f"\t Middle = {middle}")
    console.print(f"\t Last = {last}")
    myGreeting = first + " " + last + "!"
    moreFun.giveMoreFun(myGreeting) # call the function in the moreFun.py file

# end of main()
if __name__ == "__main__":
    cli()