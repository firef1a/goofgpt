# goofgpt
Scans text and generates a dictionary with the relation of every word with every other word behind it, allowing it to predict the next word in a sentence with relatively correct grammar, but cannot understand context.

## reqs
With the currently included training data, it generates around ~300MB of data but this scales with O(n^2) so be wary about adding more data since you'll need exponentially more RAM to run this program.
