#!/usr/bin/python3
# this is a smith configuration file

# set the font name, version, licensing and description
APPNAME = "LineSpacingTest"
DESC_SHORT = "Fonts for testing line spacing"

getufoinfo('source/LineSpacingTestOld-Regular.ufo')

designspace('source/LineSpacingTestOld.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                woff = woff('web/${DS:FILENAME_BASE}',
                    metadata = f'../source/LineSpacingTestOld-WOFF-metadata.xml'),
    )

getufoinfo('source/LineSpacingTestNew-Regular.ufo')

designspace('source/LineSpacingTestNew.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                woff = woff('web/${DS:FILENAME_BASE}',
                    metadata = f'../source/LineSpacingTestNew-WOFF-metadata.xml'),
    )
