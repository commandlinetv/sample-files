sample-files
============

This is the file hierarchy we use in the Command Line TV videos. You can
download it to follow along with the exact commands and files that we
illustrate.

Below is a command to fetch the files and unpack them into your *current*
directory. In the videos, that current directory would be home (`~`) but you
can create and descend into a sub-directory if you want to be sure it doesn't
interfere with your existing stuff (it has its own `Downloads` directory, for
example).

To create and descend into a new sub-directory (optional):

    mkdir sample-files
    cd sample-files

To fetch and unpack all at once (assuming you have `curl`):

    curl -L https://github.com/commandlinetv/sample-files/tarball/master | tar xvz --strip-components=1

Or you can
[fetch the 'tarball' separately](https://github.com/commandlinetv/sample-files/tarball/master)
using your browser, save it in `Downloads`, and then:

    tar xvzf commandlinetv-sample-files-HASH.tar.gz

where the `HASH` matches the file that was downloaded. This will create a new
directory called `commandlinetv-sample-files-HASH` and all the stuff will be in
there.

Have fun!
