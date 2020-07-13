a simple but fully functional command line script for fixing persian 
subtitles encoding and other problems based on an old project from [aliva](https://github.com/aliva).


## Important

This is a simple script for fixing Persian subtitles.
If you don't want to watch videos with Persian subtitles this script won't be useful for you...


### project will be updated soon...

## installing:

you need git and python3 installed on your system!

`cd /tmp && git clone https://github.com/sinaebrahimi1/sufix.git && cd sufix`

`pip install -r requirements.txt`

`chmod +x install.sh` and
`./install.sh` to install the script

Done!

## How it works?
fixing a subtitle in working directory:

`sufix fix -i filename.srt`

fixing a subtitle using its full path:

`sufix fix -fp fullpath` example: /home/sina/subtitles/How.i.met.your.mother.S05E05.srt

or you can set your subtitle folder in `subtitles_path` variable in the beginning 
of the file and script will use that path as subtitle folder:

`sufix fix -i filename.srt -cp`



##### contact me:
* email: ebrahimisina78@gmail.com
* telegram: [@Thunderstrack](https://t.me/Thunderstrack)
