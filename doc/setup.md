# Setup

Setup the hardware according to the connectivity chart, add a tube to the pump an put the other end to the plant.

## Adafruit
It's up to you if you use adafruit, since it's not too hard to change to direct the data to be sent elsewhere, but you would need to set up an account on adafruit for free if you go our exact route. When you've done that, you need to create a feed and then record username, **password** device id, and feed name.

## Code
In order for this to work for you, there are a few inputs you need to change in the code.

First you need to change the adafruit inputs in the internet class, so that you send the data to your feed and have it accessible to you.
Secondly, change the internet name and password in the main function to be connecting to your internet.

