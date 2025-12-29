/ [Home](index.md)

## MP42GIF


#### Regular
```
ffmpeg -i one.mp4 \
  -vf "fps=12,scale=960:-1:flags=lanczos" \
  -loop 0 one.gif
```


#### Smaller Size
```
ffmpeg -i one.mp4 -vf \
"fps=12,scale=960:-1:flags=lanczos,split[s0][s1];\
[s0]palettegen[p];[s1][p]paletteuse" one.gif
```