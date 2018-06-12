#!/bin/sh

set -e

exists() { which "$1" &> /dev/null ; }

if ! [ -d /home/django/.fonts ] ; then
	exec 2>&1
	echo 'There is no .fonts directory in your home.'
	echo 'Is fontconfig set up for privately installed fonts?'
	exit 1
fi

# split up to keep the download command short
# DL_HOST=download.microsoft.com
# DL_PATH=download/f/5/a/f5a3df76-d856-4a61-a6bd-722f52a5be26
# ARCHIVE=PowerPointViewer.exe
# URL="http://$DL_HOST/$DL_PATH/$ARCHIVE"
#
# if ! [ -e "$ARCHIVE" ] ; then
# 	if   exists curl  ; then curl -O "$URL"
# 	elif exists wget  ; then wget    "$URL"
# 	elif exists fetch ; then fetch   "$URL"
# 	fi
# fi
#
# TMPDIR=`mktemp -d`
# trap 'rm -rf "$TMPDIR"' EXIT INT QUIT TERM
#
# cabextract -L -F ppviewer.cab -d "$TMPDIR" "$ARCHIVE"
#
# cabextract -L -F '*.TT[FC]' -d /home/django/.fonts "$TMPDIR/ppviewer.cab"
#
# mv /home/django/.fonts/cambria.ttc /home/django/.fonts/cambria.ttf

chmod 600 /home/django/.fonts/*.ttf
chown django /home/django/.fonts/*.ttf
fc-cache -fv /home/django/.fonts
