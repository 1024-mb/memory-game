# Simon Says Game (Raspberry Pi - Explorer HAT)

This is a fun memory game based on Simon Says. It’s built using Python and the [Explorer HAT](https://shop.pimoroni.com/products/explorer-hat) on a Raspberry Pi. The game lights up LEDs in a specific order, and the player must repeat the order by pressing the right buttons. The sequence becomes longer with each successful round.

## Features

- The game shows a sequence of lights.
- The player must repeat the light sequence by pressing the right buttons.
- The game becomes more challenging by adding an extra light in the sequence after each correct round.
- There is a time limit for input, and if the player doesn’t respond in time, the game moves to the next round.
- The game keeps going until the user decides to exit.

## Requirements

- Raspberry Pi (any model with GPIO pins)
- [Explorer HAT](https://shop.pimoroni.com/products/explorer-hat) (or any similar GPIO device with at least 4 LEDs and 4 buttons)
- Python 3.x installed
- The `explorerhat` library (for interacting with the Explorer HAT)

To install the `explorerhat` library, run:

```bash
pip install explorerhat
```

## Game Flow

- The game starts by showing a short light pattern on the Explorer HAT’s LEDs.
- The player must replicate the pattern by pressing the corresponding buttons.
- If the player successfully replicates the pattern, the game increases the length of the sequence by one light, making the game harder.
- If the player fails to match the pattern or doesn't input in time, the game moves to the next round.

The player can exit the game at any time by pressing "Q".
