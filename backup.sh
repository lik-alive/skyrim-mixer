title=skyrim-mixer

echo $title backup started
ROOT=$1/$title
mkdir $ROOT

# Backup web files
WEBPATH=$ROOT/web
mkdir $WEBPATH
#rsync -a --info=progress2 . $WEBPATH --exclude .git
tar cf - --exclude ".git" . | pv -s $(du -sb . | awk '{print $1}') | gzip > $WEBPATH/$title.tar.gz

echo $title backup finished
