from media import Media, Track, Movie
from linked_list import LinkedList, Node
import json


class Player:
    """
    A media player class that manages a playlist of media.

    This class utilizes a doubly linked list (LinkedList) to store and manage media in a playlist.
    It provides methods for adding, removing, playing, and navigating through media.

    Attributes
    ----------
    playlist : LinkedList
        A doubly linked list that stores the media in the playlist.
    currentMediaNode : Node or None
        The current media being played, represented as a node in the linked list.
    """

    def __init__(self):
        """
        Initializes the Player with an empty playlist and None as currentMediaNode.
        """
        self.playlist = LinkedList()
        self.currentMediaNode = None

    def addMedia(self, media):
        """
        Adds a media to the end of the playlist.
        Set the currentMediaNode to the first node in the playlist,
        if currentMediaNode is None.

        Parameters
        ----------
        media : Media | Track | Movie
            The media to add to the playlist.
        """
        self.playlist.append(media)
        if self.currentMediaNode is None:
            self.currentMediaNode = self.playlist.dummyHead.next

    def removeMedia(self, index) -> bool:
        """
        Removes a media from the playlist based on its index.
        Set the currentMediaNode to its next, if currentMediaNode is removed,
        and remeber using _isNodeUnbound(self.currentMediaNode) to check if a link is broken.

        Parameters
        ----------
        index : int
            The index of the media to remove.

        Returns
        -------
        bool
            True if the media was successfully removed, False otherwise.
        """
        if self.playlist.deleteAtIndex(index):
            if self.playlist._isNodeUnbound(self.currentMediaNode):
                if self.currentMediaNode.next is not None:
                    self.currentMediaNode = self.currentMediaNode.next
                else:
                    self.currentMediaNode = self.currentMediaNode.prev
            return True
        return False

    def next(self) -> bool:
        """
        Moves currentMediaNode to the next media in the playlist.
        This method should not make self.currentMediaNode be self.playlist.dummyNode.

        Returns
        -------
        bool
            True if the player successfully moved to the next media, False otherwise.
        """
        if self.playlist.dummyHead.next == self.playlist.dummyTail:
            # The playlist is empty
            return False
        elif self.currentMediaNode.next == self.playlist.dummyTail:
            # The current media node is the last one in the playlist
            return False
        else:
            self.currentMediaNode = self.currentMediaNode.next
        return True

    def prev(self) -> bool:
        """
        Moves currentMediaNode to the previous media in the playlist.
        This method should not make self.currentMediaNode be self.playlist.dummyNode.

        Returns
        -------
        bool
            True if the player successfully moved to the previous media, False otherwise.
        """
        """
        Moves currentMediaNode to the previous media in the playlist.
        This method should not make self.currentMediaNode be self.playlist.dummyNode.

        Returns
        -------
        bool
            True if the player successfully moved to the previous media, False otherwise.
        """
        """
        Moves currentMediaNode to the previous media in the playlist.
        This method should not make self.currentMediaNode be self.playlist.dummyNode.

        Returns
        -------
        bool
            True if the player successfully moved to the previous media, False otherwise.
        """
        if self.playlist.dummyHead.next == self.playlist.dummyTail:
            # The playlist is empty
            return False
        elif self.currentMediaNode == self.playlist.dummyHead.next:
            # The current media node is the first one in the playlist
            return False
        else:
            self.currentMediaNode = self.currentMediaNode.prev
        return True

    def resetCurrentMediaNode(self) -> bool:
        """
        Resets the current media to the first media in the playlist,
        if the playlist contains at least one media.

        Returns
        -------
        bool
            True if the current media was successfully reset, False otherwise.
        """
        if self.playlist.dummyHead.next != self.playlist.dummyTail:
            self.currentMediaNode = self.playlist.dummyHead.next
            return True
        return False

    def play(self):
        """
        Plays the current media in the playlist.
        Call the play method of the media instance.
        Remeber currentMediaNode is a node not a media, but its data is the actual
        media. If the currentMediaNode is None or its data is None,
        print "The current media is empty.".
        """
        if self.currentMediaNode is not None and self.currentMediaNode.data is not None:
            self.currentMediaNode.data.play()
        else:
            print("The current media is empty.")

    def playForward(self):
        """
        Plays all the media in the playlist from front to the end,
        by iterating the linked list.
        Remeber each media information should take one line. (follow the same
        format in linked list)
        If the playlist is empty, print "Playlist is empty.".
        """
        if self.playlist.dummyHead.next == self.playlist.dummyTail:
            print("Playlist is empty.")
        else:
            node = self.playlist.dummyHead.next
            while node != self.playlist.dummyTail:
                self.currentMediaNode = node
                self.play()
                node = node.next

    def playBackward(self):
        """
        Plays all the media in the playlist from the back to front,
        by iterating the linked list.
        Remeber each media information should take one line. (follow the same
        format in linked list)
        If the playlist is empty, print this string "Playlist is empty.".
        """
        if self.playlist.dummyHead.next == self.playlist.dummyTail:
            print("Playlist is empty.")
        else:
            node = self.playlist.dummyTail.prev
            while node != self.playlist.dummyHead:
                self.currentMediaNode = node
                self.play()
                node = node.prev

    def loadFromJson(self, fileName):
        """
        Loads media from a JSON file and adds them to the playlist.
        The order should be the same as the provided json file.
        You could assume the filename is always valid
        Notice, for each given json object,
        you should create instance of the correct instance type, (movie,track,media).
        You need to observe the provided json and figure how to do it.
        You could assume if a json object is not track or movie,
        it has to be a media.
        Pay attention the name of the key in each json object.
        Set the currentMediaNode to the first media in the playlist,
        if there is at least one media in the playlist.
        Remeber to use the dictionary get method.

        Parameters
        ----------
        filename : str
            The name of the JSON file to load media from.
        """
        with open(fileName, "r", encoding="utf-8") as file:
            data = json.load(file)
        for media in data:
            if media.get("kind") == "song":
                self.addMedia(
                    Track(
                        media.get("trackName"),
                        media.get("artistName"),
                        media.get("releaseDate"),
                        media.get("trackViewUrl"),
                        media.get("collectionName"),
                        media.get("primaryGenreName"),
                        media.get("trackTimeMillis"),
                    )
                )
            elif media.get("kind") == "feature-movie":
                self.addMedia(
                    Movie(
                        media.get("trackName"),
                        media.get("artistName"),
                        media.get("releaseDate"),
                        media.get("trackViewUrl"),
                        media.get("contentAdvisoryRating"),
                        media.get("primaryGenreName"),
                    )
                )
            else:
                self.addMedia(
                    Media(
                        media.get("collectionName"),
                        media.get("artistName"),
                        media.get("releaseDate"),
                        media.get("collectionViewUrl"),
                    )
                )
        if self.playlist.dummyHead.next != self.playlist.dummyTail:
            self.currentMediaNode = self.playlist.dummyHead.next
