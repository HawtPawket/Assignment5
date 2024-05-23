# Task 1: The for Loop DJ Set
# Using the provided genres list, write a for loop that prints out 
# each genre with a custom message. Extend this task by adding a counter 
# that displays the number of the track before the genre.

# Our playlist of genres
# genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']





genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
songNumber = 1


for genre in genres:
    print("Song", songNumber,  "Playing", genre)
    songNumber +=1



# Task 2: The Remix Artist with while
# Convert the for loop from Task 1 into a while loop. Ensure it 
# performs the same function but also includes a condition to stop
# the loop if a certain genre is played for instance Hip-hop.





genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
stopPlaying = "Hip-hop"
songNumber = 0


while songNumber < len(genres) and genres[songNumber] != stopPlaying:
    print("Playing:" + genres[songNumber])
    songNumber +=1


# Task 3: Light Show Technician Loop
# Using the range() function, loop through the genres list by index. 
# For each genre, print out the track number and a message that the light show is 
# ready. Modify the loop to skip a genre if it's not suitable for the light show, 
# for instance Classical genre.


genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
noLightGenres = "Classical"


for index in range(len(genres)):
    if genres[index] == noLightGenres:
        continue
    print("Song",{index +1}, genres[index], "LIGHT SHOW IS READY!")