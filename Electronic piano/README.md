# Electronic piano (Arduino)

A small experiment where I wanted to take a keyboard project from my Arduino Projects Book as far as possible. I chose the resistance values for each of the 8 key buttons from C4 to C5 so that each key would have a different resistance, as would the equivalent resistance of two adjacent key buttons in parallel, so that pressing two adjacent keys would generate the sharp note. I connect the buttons to a 4.7 kOhm resistor, so that when a key (or pair of adjacent keys) is pressed, it creates a voltage divider with a different resistor ratio. I can then read the unique voltage across the second resistor with an analog pin to know which key (or pair) was pressed, and play the corresponding note on a speaker.

I play La Marseillaise here: https://youtu.be/jV4Ms26uF1I
