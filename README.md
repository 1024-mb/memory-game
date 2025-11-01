# Simon Says Game (Raspberry Pi - Explorer HAT)

A fun Simon Says-style memory game built using Python and the [Explorer HAT](https://shop.pimoroni.com/products/explorer-hat) on a Raspberry Pi. 
The game lights up LEDs in a sequence, and the player must replicate the sequence by pressing the corresponding buttons.
The sequence gets longer with each successful round.

## Features

- The game flashes a sequence of lights.
- The player must replicate the light sequence by pressing the correct buttons.
- The game increases in difficulty by adding an additional light in the sequence after each correct round.
- The game has a time limit for input, and if the player doesn't respond in time, the game moves to the next round.
- The game continues until the user chooses to exit.


## Requirements

- Raspberry Pi (any model with GPIO pins)
- [Explorer HAT](https://shop.pimoroni.com/products/explorer-hat) (or any similar GPIO device with at least 4 LEDs and 4 buttons)
- Python 3.x installed
- The `explorerhat` library (for interacting with the Explorer HAT)

To install the `explorerhat` library, run:

```bash
pip install explorerhat

##Hardware Setup

- Explorer HAT: Ensure that your Explorer HAT is properly connected to the Raspberry Pi.
- Wiring: The game uses the four buttons and four lights on the Explorer HAT. Each button corresponds to a light.
- GPIO Pins: The Explorer HAT's touch pads are used to receive input, while the lights are used to display the pattern.
