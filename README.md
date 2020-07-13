a simple and fully functional command line script for fixing persian 
subtitles encoding and other problems based on an old project from [aliva](https://github.com/aliva).


## Important

This is a simple nautilus script for fixing Persian subtitles.
If you don't want to watch videos with Persian subtitles this script won't be usefull for you...


### project will be updated soon...

## installing:

you need git and python3 installed on your system!

`git clone git@github.com:sinaebrahimi1/sufix.git && cd sufix`

`pip install -r requirements.txt`

Done!

## How it works?
fixing a subtitle in working directory:

`./sufix.py fix -i filename.srt`

fixing a subtitle using its full path:

`./sufix.py fix -fp fullpath` example: /home/sina/subtitles/How.i.met.your.mother.S05E05.srt

or you can set your subtitle folder in `subtitles_path` variable in the beginning 
of the file and script will use that path as subtitle folder:

`./sufix.py fix -i filename.srt -cp`



##### contact me:
* email: ebrahimisina78@gmail.com
* telegram: [@Thunderstrack](https://t.me/Thunderstrack)
