import os
import random

from discord.ext import commands


def roll_die(sides: int) -> int:
    """Rolls a die with given number of sides."""
    return random.randint(1, sides)


def parse(message: str) -> tuple[int, int]:
    """
    Takes a !roll message and parses the
    dice count and dice sides.
    """
    args = message.split()
    count, sides = args[0].split("d")
    return int(count), int(sides)


def roll(message: str) -> int:
    """
    Rolls dice given a command.

    Example commands:
        2d6 - Rolls 2 six sided dice.
        1d20 - Rolls 1 twenty sided die.
    """
    count, sides = parse(message)
    return sum([roll_die(sides) for i in range(count)])


bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")


@bot.command()
async def roll(ctx, message: roll):
    await ctx.send(f"You rolled a {message}")


if __name__ == "__main__":
    key = os.getenv("DISCORD_KEY")
    bot.run(key)
