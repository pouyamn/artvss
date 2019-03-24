# artvss
Auto Renames TV Series Subtitles


 Auto rename subtitles for TV Series to mtch the video files

**Usage**:
```
artvss [subtitle folder] [video folder]
artvss [target folder]
```
        
It requires that season number and episod number exist if file name of videos and subtitles, 
no specific format is important it should just be the first two numbers in the file names and
they should be separated with any non-digit charecter.

For example: 
- It renames 'the.sopranos.6-12.hdtv-lol.srt' to 'The Sopranos Season 6 Episode 12 - Kaisha.srt' automatically 
to match 'The Sopranos Season 6 Episode 12 - Kaisha.avi' 
- And "Sopranos [4x02] - No-Show - Sweetmate -.srt" to "The Sopranos Season 4 Episode 02 - No Show.srt" to match "The Sopranos Season 4 Episode 02 - No Show.mkv"

If no parameters given it will use current folder for both subs and videos. If only one argument is given,
it will be used for both, the program looks into the provided path and put the result into it. If both paths give, first one 
will be used for looking up subtitles and the second one for looking up for video files, any match result in renaming the 
subtitle and moving it to the videos folder.

**Warning!: It will overwrite files with no prior notice.**
