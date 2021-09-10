echo 'skyrim-mixer backup started'

ROOT=$1/skyrim-mixer
mkdir $ROOT

# Backup web files
WEBPATH=$ROOT/web
mkdir $WEBPATH
rsync -a --info=progress2 . $WEBPATH --exclude .git

echo 'skyrim-mixer backup finished'