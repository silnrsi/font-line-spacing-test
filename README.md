# Line Spacing Test Fonts

This file provides detailed information on the Line Spacing Test family of fonts. This information should be distributed along with the Line Spacing Test fonts and any derivative works.

## Project status [![Build Status](http://build.palaso.org/app/rest/builds/buildType:Fonts_LineSpacingTest/statusIcon)](http://build.palaso.org/viewType.html?buildTypeId=Fonts_LineSpacingTest&guest=1)


These fonts are based on Andika Mtihani (https://github.com/silnrsi/font-andika-mtihani) and are only for use in testing application line spacing and clipping. 

For copyright and licensing information - including any Reserved Font Names - see [OFL.txt](OFL.txt).

For practical information about using, modifying and redistributing this font see [OFL-FAQ.txt](OFL-FAQ.txt).

For more details about this project, including changelog and acknowledgements see [FONTLOG.txt](FONTLOG.txt) and [README.txt](README.txt).

## Background

OpenType fonts have at least three sets of internal metrics that applications and web sites can use to determine default line spacing:

- [Ascender/Descender/LineGap in `hhea` table](https://docs.microsoft.com/en-us/typography/opentype/spec/hhea) - initially intended to be single reference but in practice is Apple-only
- [usWinAscent/usWinDescent in `OS/2` table](https://docs.microsoft.com/en-us/typography/opentype/spec/os2#uswinascent) - common for older Windows apps (and still used by Notepad)
- [sTypoAscender/sTypoDescender/sTypoLineGap in `OS/2` table](https://docs.microsoft.com/en-us/typography/opentype/spec/os2#stypoascender) - recommended on all platforms (since 2008)

These metrics also have an influence on clipping, where parts of glyphs that extend very high or very low can get chopped off on screen in some Windows apps. Clipping only affects screen rendering, not printing.

Traditionally SIL has set all of these metrics to be equal, so that a wide variety of applications on multiple platforms have similar default line spacing. Our [Font Development Best Practices site](http://silnrsi.github.io/FDBP/en-US/Line_Metrics.html) provides more details on this technique.

The problem with this practice is that it has forced us to give many of our fonts wider-than-normal default line spacing. Any reduction in the default line spacing would cause the tops or bottoms of some glyphs - and in some cases whole diacritics - to get cut off or disappear altogether on screen. 

We are being encouraged to switch our practice to use a different technique that in many cases will enable us to eliminate most clipping and reduce default line spacing. However this can cause older apps that still use *usWinAsc/Desc* to miss out on these benefits and see line spacing *increase* in some cases. This also will affect apps using OS APIs or frameworks that rely on *usWinAsc/Desc*.

**Apps are strongly recommended to set default line spacing using the sTypo metrics, and we're now setting a flag in our fonts ([fsSelection bit 7](https://docs.microsoft.com/en-us/typography/opentype/spec/os2#fsselection)) that explicitly tells apps to use the sTypo metrics.**

## Using these fonts to test line spacing

You may not know what line metrics your app is using. These fonts enable you to test if changes to our fonts may affect you.

1) *Install:* Download the Github release package and install the two included fonts (Line Spacing Test Old and Line Spacing Test New).

2) *Test line spacing:* Use the fonts to display text in your app. If the line spacing for both fonts is equal then you are not using *usWinAsc/Desc* - good news! Be aware, however, that this does not mean that you are correctly using *sTypo* metrics. Some text frameworks may set default line spacing as a percentage of the type size (but really should be using *sTypo*).

3) *Test for clipping:* Add the character Ǻ (U+01FA - Latin Capital A with ring and acute) to your text. Look carefully at the text using each of the fonts. If both the ring and acute appear over the A then no clipping is happening with that font. If the acute (above the ring) is missing then the glyphs are being clipped.

    - If clipping is happening with *Old* but not *New* then the new technique will benefit your app.
    - If clipping is happening with *both* fonts then see if explicitly increasing line spacing in your app will reduce the clipping. If that does not work then your app or framework may be using other metrics (possibly *sTypo* or *hhea*, or percentages) to define clipping regions. That's a bad idea. See below for a better option for determining clipping on Windows.  

4) *Tell us what is happening:* In order to make good decisions regarding our font practices we need to know what apps may be affected by these changes. **Please let us know if your app displays different line spacing with the two fonts, or if you're seeing any clipping.** Write to us using the [font support contact form](https://software.sil.org/fonts/support/) with a subject of "Line spacing tests".

## Using usWinAscent/usWinDescent for clipping

Although it's no longer recommended to use *usWinAsc/Desc* for line spacing, it is appropriate to use it for determinine clipping regions. The [OpenType specification](https://docs.microsoft.com/en-us/typography/opentype/spec/os2#uswinascent) notes that: 

*Applications that use the sTypo fields for default line spacing can use the usWin values to determine the size of a clipping region. Some applications use a clipping region for editing scenarios to determine what portion of the display surface to re-draw when text is edited, or how large a selection rectangle to draw when text is selected. This is an appropriate use for the usWin values."

