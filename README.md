# Holiday

Choose the best days to be off work in the calendar following some rule in order to maximize satisfaction


# Usage

Edit the file `feste.py` adding the day off work in your country, file is now set with italian configuration.

Edit the `holidays.py` and set the `daysn = 24;` to the number of days you have for holidays in a year!

run command

```
python holidays.py
```

The result is the best day you can pick in your calendar in order to maximize your satisfaction during your holiday!


# How Does this work?

## Genetic approach

The system create a number of dna made as a list of 0 o 1 where 0 is working day and 1 is holidays.
He try to maximize a function of fitness where block of long holidays are preferred.
He select the top of the dna and delete the other and make them reproduce using crossing over and random mutation.
