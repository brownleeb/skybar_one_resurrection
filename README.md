# skybar_one_resurrection
How to resurrect a broken Skybar ONE for $5 (and a lot of time)

This is my story of resurrecting my inoperative Skybar One wine cooler system.  It is NOT intended as a tutorial on how to do this yourself!  You would need to have a full understanding of what was done, and I dont even know if I have that!  I provide it here to document the "realm of the possible" and perhaps someone will suggest an improvement that will help my project.

First, the background.  This is my second Skybar ONE (model WP0550).  The first failed after about 2 years.  The second failed after just short of one year of use.  Both failed the same way.  They were turned off, as recommended in the instruction manual, during an extended period of non-use.  When turned back on, they never started.  Nothing on the LCD display, no fans, no power consumption.  Skybar has since stopped production (just check Amazon reviews to find out why).

When the first failed, I went straight after the power supply.  It was not putting out the required voltage, but sometimes switching power supplies will not measure correctly without a load.  After trying a few things, and melting a few wires, I gave up and bought another.

When the second failed, I decided to go back to the first and figure out what everything did.  Here is what I came up with:
  - There are two IC boards.  One is relatively easy to get at, is the 'Control Board'.  The second I couldn't get at and is called the 'UI Board'
  - Obviously, there is a ThermoElectric Cooler (Peltier device)
  - There are two fans, one outside to cool the heat sink, another inside to keep constant temperatures
  - There is a air pump which also has a vacuum side
  - There are 4 solenoid controlled air valves
  - There is a temperature sensor (NTC Thermistor) inside
  - There is a vacuum sensor near the control board

That's it.  The UI board apparently runs all the buttons, allows settings, etc, and reads the vacuum sensor.  It runs off a 10v thin gauge wire from the power supply.  The Control board controls the TEC, pump, fans and air valve solenoids.  It is powered by a thicker gauge wire (labeled 10.85v) from the same power supply.  There is an 11 wire ribbon cable between the UI and Control boards.

So, how do you fix this thing for $5?  Three words, "Raspberry Pi Zero" (which for me was a 99 cent promo from MicroCenter).  Yeah, you'll need a couple other things, but I believe my solution is a bit 'clunky' and could be slimmed down if one really wanted a minimal solution vs "quick and functioning".

This repository may never get viewed, but I put it out there just to say "Hey, I did this" and if it helps anyone, or you want to help me, it will have served its purpose.
