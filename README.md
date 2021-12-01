# CHOA
This is a Choose Your Own Adventure - style game created for a philosophy project to explore sci-fi and philosophy through a game, video, podcast or another type of media.
It uses flask to render templates of static html pages containing all the possible choices which inherit from a "base" template to mitigate redundant code.
Buttons link html pages together depending on the route the player wants to take.
The names of the html pages correspond to a tree diagram containing all of the options ex. L1R2 would mean one left choice followed by two right choices.
Various paths link back to common endings.
