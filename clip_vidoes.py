
import os
import shutil
import subprocess
from moviepy.editor import VideoFileClip

VIDEO_YOUTUBE_ID = 'RDrfE9I8_hs'
RAW_VIDEO_FOLDER = os.path.join('video_data', 'raw')
CLIPPED_VIDEO_FOLDER = os.path.join('video_data', 'clipped')

TRUMP_FILENAME = 'china.mp4'
TRUMP_OUTPUT_RAW_FILEPATH = os.path.join(RAW_VIDEO_FOLDER, 'trump', TRUMP_FILENAME)
TRUMP_OUTPUT_CLIPPED_FOLDER = os.path.join(CLIPPED_VIDEO_FOLDER, 'trump')


def download_trump_video():
  if not os.path.isfile(TRUMP_OUTPUT_RAW_FILEPATH):
    command = 'youtube-dl %s -o %s' % (VIDEO_YOUTUBE_ID, TRUMP_FILENAME)
    if subprocess.call(command, shell=True) == 0:
      shutil.move(TRUMP_FILENAME, TRUMP_OUTPUT_RAW_FILEPATH)
    else:
      return False
  return True

def clip_trump_videos():
  cuts = [(3, 5), (6, 8), (9, 12)]
  video = VideoFileClip(TRUMP_OUTPUT_RAW_FILEPATH)
  subclips = [video.subclip(start, end) for (start, end) in cuts]
  for i in xrange(len(subclips)):
    clip = subclips[i]
    outfile = os.path.join(TRUMP_OUTPUT_CLIPPED_FOLDER, 'china-%02d.mp4' % i)
    clip.to_videofile(outfile, codec='libx264', audio_codec='aac', temp_audiofile='china-%02d.m4a' % i, remove_temp=True)
  return True

if __name__ == '__main__':
  clip_trump_videos()