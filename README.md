# What?
Sulley is an actively developed fuzzing engine and fuzz testing framework consisting of multiple extensible components.
Sulley (IMHO) exceeds the capabilities of most previously published fuzzing technologies, commercial and public domain.
The goal of the framework is to simplify not only data representation but to simplify data transmission and 
instrumentation. Sulley is affectionately named after the creature from Monsters Inc., because, well, he is fuzzy.

![He's also fearless](http://i.imgur.com/AHuBu.jpg)

Clearly he's also fearless. 

# Why?
Modern day fuzzers are, for the most part, solely focus on data generation. Sulley not only has impressive data
generation but has taken this a step further and includes many other important aspects a modern fuzzer should provide.
Sulley watches the network and methodically maintains records. Sulley instruments and monitors the health of the target,
capable of reverting to a known good state using multiple methods. Sulley detects, tracks and categorizes detected
faults. Sulley can fuzz in parallel, significantly increasing test speed. Sulley can automatically determine what unique
sequence of test cases trigger faults. Sulley does all this, and more, automatically and without attendance. It's not
usual for a fuzz to run seamlessly for days at a time, that way you (as the vulnerability researcher) can focus on
other areas of exploitation, and come back to Sulley's results when they're convenient for you.

# Awesome! Where do I start?
Well a good place to start if you're on windows is the [wiki article on Windows setup](https://github.com/OpenRCE/sulley/wiki/Windows-Installation), and if you're feeling ballsy check out the [unstable branch of Sulley](https://github.com/OpenRCE/sulley/tree/Sulley1.1) If you're on *nix, sit tight, the docs are coming for the installation procedure for
that, but if you use *nix, chances are you can probably figure it out on your own.

# Some notes
This is a fork of the orginal sulley framework which is adapted for bluetooth fuzzing. It use a HCI RAW socket communication which enables full controle of L2CAP and all layers above.

If you have any other questions/improvements/features you'd like to see feel free to [email me](https://github.com/FlorianPuffer)!

