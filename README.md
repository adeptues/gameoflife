#Game of Life

This is an implementation of conways game of life in python
basic implementation at the moment but it works, still rough around the edges

## Dependancies 

needs numpy installed and pygame 

pip install -r requirements.txt

the above should work 90% of the time however pygame is an enigma and if it fails to install it will fail
hard, to fix do the following

install dependancies

sudo apt-get install mercurial python-dev python-numpy ffmpeg \
    libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
    libsdl1.2-dev  libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev

then install video4l-dev

sudo apt-get install libv4l-dev

and becuase apt-get installs it but doesnt put the header files in the right place we need to create a symlink
so pygame can find it.

cd /usr/include/linux

sudo ln -s ../libv4l1-videodev.h videodev.h

then install py game via this method becuase pip will try to download 1.6 instead of 1.9 and it puts out all sorts
of jibberish 400 bad request etc ...

pip install http://www.pygame.org/ftp/pygame-1.9.1release.tar.gz

fucking package managers ...