from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("test-video.mp4", 5000, 5300, targetname="cut2.mp4")