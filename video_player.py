"""A video player class."""

from .video_library import VideoLibrary
import random
        
class VideoPlayer:
    """A class used to represent a Video Player."""
        
    def __init__(self):
        self._video_library = VideoLibrary()
        
    def default_values(self):
        global video_playing
        global video_paused
        global current_video
        global Playlists
        global Playlists_with_vids
        
        video_playing = False
        video_paused = False
        current_video = 0
        Playlists = []
        Playlists_with_vids = []
        
    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        alphalist = sorted(self._video_library.video_id_list())
        
        for i in range(0,len(alphalist)):
            for j in range(0, len(alphalist)):
                if alphalist[i] == self._video_library.get_all_videos()[j][1].strip():
                    video_info = self._video_library.get_all_videos()[j]
                    video_info_2 = video_info[0].strip() + " ("+video_info[1].strip()+") "+"["+(video_info[2].strip()).replace(' ,', '')+"]"
            print(video_info_2)

    def play_video(self, video_id):
        global video_playing
        global current_video
        global video_paused
        
        video_name = 0
        """Plays the respective video.
        Args: video_id: The video_id to be played."""
        for i in range(len(self._video_library.video_id_list())):
            if video_id == self._video_library.video_id_list()[i]:
                video_name = self._video_library.get_all_videos()[i][0].strip()
        
        if video_name == 0:
            print("Cannot play video: Video does not exist")
        elif video_playing == True:
            print("Stopping video: " + str(current_video))
            current_video = video_name
            video_playing = True
            video_paused = False
            print("Playing video: " + str(video_name))
        else:
            current_video = video_name
            video_playing = True
            video_paused = False
            print("Playing video: " + str(video_name))
        

    def stop_video(self):
        global video_playing
        global current_video
        
        if video_playing == False:
            print("Cannot stop video: No video is currently playing")
        else:
            video_playing = False
            print("Stopping video: " + str(current_video))


    def play_random_video(self):
        """Plays a random video from the video library."""
        global video_playing
        global current_video
        global video_paused
        
        r = random.randrange(0, len(self._video_library.video_id_list()))
        video_name = self._video_library.get_all_videos()[r][0].strip()
        
        if video_playing == True:
            print("Stopping video: " + str(current_video))
        current_video = video_name
        video_playing = True
        video_paused = False
        print("Playing video: " + str(video_name))

    def pause_video(self):
        """Pauses the current video."""
        global video_playing
        global current_video
        global video_paused
        
        if video_playing == False:
            print("Cannot pause video: No video is currently playing")
        
        elif video_paused == True:
            print("Video already paused: " + str(current_video))
        else:
            video_paused = True
            print("Pausing video: " + str(current_video))

    def continue_video(self):
        """Resumes playing the current video."""
        global video_playing
        global current_video
        global video_paused
        
        if video_playing == False:
            print("Cannot continue video: No video is currently playing")
        
        elif video_paused == False:
            print("Cannot continue video: Video is not paused")
        else:
            video_paused = False
            print("Continuing video: " + str(current_video))

    def show_playing(self):
        """Displays video currently playing."""
        global video_playing
        global current_video
        global video_paused
        
        index = 0
        
        if video_playing == False:
            print("No video is currently playing")
        else:
            for i in range(0, len(self._video_library.video_id_list())):
                if current_video == (self._video_library.get_all_videos()[i][0]).strip():
                    index = i
            video_info = current_video
            video_info +=" ("+str(self._video_library.video_id_list()[index])+") " 
            video_info +="["+str((self._video_library.get_all_videos()[index][2]).strip()).replace(' ,', '')+"]"
            if video_paused == True:
                print("Currently playing: " + video_info + " - PAUSED")
            else:
                print("Currently playing: " + video_info)
            
    def create_playlist(self, playlist_name):
        global Playlists
        similarity = 0
        
        for i in range(len(Playlists)):
            if (str(playlist_name.casefold())) == str(Playlists[i].casefold()):
                similarity = 1
        if similarity == 1:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            print("Successfully created new playlist: " + str(playlist_name))
            Playlists.append(playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        global Playlists
        global Playlists_with_vids
        
        Playlists_stand = []
        playlistname = str(playlist_name)
        already_added = 0
        video_name = 0
           
        for i in range(len(Playlists)):
            Playlists_stand.append(Playlists[i].lower())
            
        if playlistname.lower() in Playlists_stand:
            for i in range(0,len(Playlists)):
                if isinstance(playlist_name,str):
                    playlist_name = playlist_name.lower()
                    playlist_name = []
            for j in range(len(self._video_library.video_id_list())):
                if video_id == self._video_library.video_id_list()[j]:
                    video_name = self._video_library.get_all_videos()[j][0].strip()
            for k in range(0, len(Playlists_with_vids)):
                if video_name in Playlists_with_vids[0]:
                    already_added = 1
            if video_name == 0:
                print("Cannot add video to "+playlistname +": Video does not exist")
            elif already_added != 0:
                print("Cannot add video to "+playlistname +": Video already added")
            else:
                playlist_name.append(video_name)
                Playlists_with_vids.append(playlist_name)
                print("Added video to "+playlistname + ": " + str(video_name))
            
        else:
            print("Cannot add video to "+str(playlist_name) +": Playlist does not exist")
        
       

    def show_all_playlists(self):
        """Display all playlists."""
        global Playlists
        
        if len(Playlists) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            sorting = sorted(Playlists)
            for i in range(len(Playlists)):
                print(sorting[i])

    def show_playlist(self, playlist_name):
        global Playlists_with_vids
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        global Playlists
        Playlists_stand = []
        
        for i in range(len(Playlists)):
            Playlists_stand.append(Playlists[i].lower())
            
        if playlist_name.lower() not in Playlists_stand:
            print("Cannot delete playlist "+str(playlist_name+": Playlist does not exist"))
        else:
            Playlists.remove(playlist_name)
            print("Deleted playlist: "+str(playlist_name))
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
