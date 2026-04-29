## Steps
1. Get Channel ID
    1. https://www.youtube.com/@misterwootube
    2. Inspect HTML (Developer Mode)
        1. `<link rel="alternate" href="android-app://com.google.android.youtube/http/www.youtube.com/channel/UCq0EGvLTyy-LLT1oUSO_0FQ">`
    3. Channel ID: `UCq0EGvLTyy-LLT1oUSO_0FQ`
    4. PreFix Codes
        1. `UC...` identifies a Channel.
        2. `UU...` identifies a User Uploads playlist.
        3. `PL...` identifies a User-Created playlist.
        4. `UULF.` videos only, no shorts
        5. `UULP.` videos only, no shorts + Popular Ones
    5. PlayList of All Uploaded VIdeos
        1. https://www.youtube.com/playlist?list=UUq0EGvLTyy-LLT1oUSO_0FQ

2. https://ypc.vercel.app/
    1. Paste the link above
    2. Save as HTML
    3. Ask ChatGPT to write a python script to extract all the youtube links from the HTML

3. Alternatively, use "MultiSelect for YouTube"
    1. https://chromewebstore.google.com/detail/multiselect-for-youtube/gpgbiinpmelaihndlegbgfkmnpofgfei?hl=en
    2. Load Entire Playlist
    3. Select All
    4. Save Selection to Right
    5. Don't use the "Save Playlist" option. It's kinda broken. Saves 100 videos max.

4. Alternatively, https://youtube-play-all.vercel.app/

5. Youtube Playlist from VideoIDs
    - https://ascdapps.com/youtube-playlist-from-links/