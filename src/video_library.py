"""A video library class."""

from .video import Video
from pathlib import Path
import csv


# Helper Wrapper around CSV reader to strip whitespace from around
# each item.

class VideoLibrary:
    """A class used to represent a Video Library."""

    def __init__(self):
        """The VideoLibrary class is initialized."""
        self._videos = []
        with open(Path(__file__).parent / "videos.txt") as video_file:
            reader = csv.reader(video_file, delimiter="|")
            for v_i in reader:
                self._videos.append(v_i)
                   
    def get_all_videos(self):
        """Returns all available video information from the video library."""
        return list(self._videos)
    
    def video_id_list(self):
        video_id_list = []
        for i in range(len(self._videos)):
            video_id_list.append(self._videos[i][1].strip())
        return video_id_list
