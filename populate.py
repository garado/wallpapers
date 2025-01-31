
# █▀█ █▀▀ ▄▀█ █▀▄ █▀▄▀█ █▀▀    █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█ 
# █▀▄ ██▄ █▀█ █▄▀ █░▀░█ ██▄    █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄ 

from email.mime import image
import os
from glob import glob

pre = """
# Welcome to my personal collection of wallpapers

Scavenged from all corners of the Internet and vetted for perfection.

Check out [mountain, my personal favorite collection](#mountain)

# Previews
Previews are formatted for viewing on desktop.

<hr>
<p align="center">
"""

post = """
</p>
"""

ext = [".jpg", ".jpeg", ".png", ".gif", ".webp", ".webm", ".avif"]

imagecount = 0

with open("./readme.md", "w") as f:
    f.write(pre)

def wall_embed(title,path):
    return f"""| <img src="{path}" title="{title}" width="300" height="160"> """

def palette_embed(title, path):
    return f"""<img src="{path}" title="{title}">"""

def get_palette(title):
    return "palette/" + title + ".png"

def new_table_section():
    return "\n\n| | | |\n|:---------:|:---------:|:----------:|\n"

with open("./readme.md", "a") as readme:
    # get top level directories
    rootdir = '.'
    directory_list = list()
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d) and d != "./.git" and d != "./palette" and d != "./unvetted":
            directory_list.append(d)

    # sort directories in alphabetical order
    directory_list.sort()

    for d in directory_list:
        themename = d.lstrip(d[0:2])
        readme.write("\n\n## " + themename)
        
        # embed palette preview images
        palette_preview = get_palette(themename)
        if os.path.exists(palette_preview):
            readme.write("\n")
            readme.write(palette_embed(themename, palette_preview))

        # to show/hide table
        readme.write("\n<details><summary></summary>")
       
        # add images to table
        readme.write(new_table_section())
        gridcount = 0
        for file in glob(d + "/**", recursive = True):
            imagecount += 1
            if file.endswith(tuple(ext)):
                readme.write(
                    wall_embed(file[:-4], file)
                )
                gridcount += 1
  
                if gridcount == 4:
                    gridcount = 0
                    readme.write("|\n")
  
        # end show/hide table
        readme.write("\n</details>")
  
    readme.write(post)

print("you have "+str(imagecount)+" images")
