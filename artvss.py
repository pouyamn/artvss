#!/usr/bin/env python3

#Version 1.0.0
#Author PMN

import os
import sys
import re

VID_EXT = ['.mp4', '.mkv', '.avi']
SUB_EXT = ['.srt', '.sub']


def printHelp():
    print(f'''
        
        Auto rename subtitles for TV Series to mtch the video files

        Usage: {sys.argv[0][sys.argv[0].rindex("/")+1:]} [subtitle folder] [video folder]
               {sys.argv[0][sys.argv[0].rindex("/")+1:]} [target folder]
        
        It requires that season number and episod number exist if file name of videos and subtitles, 
        no specific format is important it should just be the first two numbers in the file names and
        they should be separated with any non-digit charecter.

        For example: 
        It renames 'the.sopranos.6-12.hdtv-lol.srt' to 'The Sopranos Season 6 Episode 12 - Kaisha.srt' automatically 
        to match 'The Sopranos Season 6 Episode 12 - Kaisha.avi' 
        And "Sopranos [4x02] - No-Show - Sweetmate -.srt" to "The Sopranos Season 4 Episode 02 - No Show.srt" to match "The Sopranos Season 4 Episode 02 - No Show.mkv"

        If no parameters given it will use current folder for both subs and videos. If only one argument is given,
        it will be used for both, the program looks into the provided path and put the result into it. If both paths give, first one 
        will be used for looking up subtitles and the second one for looking up for video files, any match result in renaming the 
        subtitle and moving it to the videos folder.

        Warning!: It will overwrite files with no prior notice.
        ''')
    exit()


def main():
    if len(sys.argv) == 1:
        src = dest = '.'
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            printHelp()
        else:
            src = dest = sys.argv[1]
    elif len(sys.argv) == 3:
        src, dest = sys.argv[1:]
    else:
        printHelp()

    src_files = os.listdir(src)
    dest_files = os.listdir(dest)

    src_files = [
        file for file in src_files
        if re.match(f'.*(?<={"|".join(SUB_EXT)})$', file)
    ]
    dest_files = [
        file for file in dest_files
        if re.match(f'.*(?<={"|".join(VID_EXT)})$', file)
    ]

    # print("\n".join(src_files))
    # print("\n".join(dest_files))

    src_dict = {}
    for sf in src_files:
        src_dict[tuple([
            int(g) for g in re.match(
                r'^\D*(?P<season>\d+)\D*(?P<episode>\d+).*$', sf).groups()
        ])] = sf

    dest_dict = {}
    for df in dest_files:
        dest_dict[tuple([
            int(g) for g in re.match(
                r'^\D*(?P<season>\d+)\D*(?P<episode>\d+).*$', df).groups()
        ])] = df

    commands = []

    for key in dest_dict.keys():
        if src_dict.get(key):
            commands.append(
                (src_dict[key], dest_dict[key][:dest_dict[key].rindex('.')] +
                 src_dict[key][src_dict[key].rindex('.'):]))
            print(
                f'Renaming "{commands[-1][0]}" to "{commands[-1][1]}" to match "{dest_dict[key]}"'
            )
            os.rename(
                os.path.join(src, commands[-1][0]),
                os.path.join(dest, commands[-1][1]))


if __name__ == '__main__':
    main()
