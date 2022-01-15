# Setup

Setup the hardware according to the connectivity chart, add a tube to the pump an put the other end to the plant.

## Adafruit
It's up to you if you use adafruit, since it's not too hard to change to direct the data to be sent elsewhere, but you would need to set up an account on adafruit for free if you go our exact route. When you've done that, you need to create a feed and then record username, the key at the "My Key" page device id, and feed name.

## Code
In order for this to work for you, there are a few inputs you need to change in the code.

First you need to change the adafruit inputs in the internet class, so that you send the data to your feed and have it accessible to you.
Secondly, change the internet name and password in the main function to be connecting to your internet.
Third, determine what moisture level your plant should have and how often it should be watered. Right now the code so that the plant will be watered for five seconds if the moisture level is below a certain value every two hours when it takes it's measurement. However a cactus for example, should not be watered even every day, thus the time waiting after last measurement can be increased from two hours. Thus, the three variables timeCycle, moistureLevel and pumpTime in the main file.
