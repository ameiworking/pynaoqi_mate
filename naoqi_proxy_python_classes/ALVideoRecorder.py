#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alvideorecorderproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


# To not instance network connections until we actually want to
# do a proxy call
def lazy_init(fn):
    def init_if_needed(self, *args, **kwargs):
        if not self.proxy:
            self.proxy = ALProxy("ALVideoRecorder")
        return fn(self, *args, **kwargs)
    # Preserve method name and docs
    init_if_needed.__name__ = fn.__name__
    init_if_needed.__doc__ = fn.__doc__
    return init_if_needed


class ALVideoRecorder(object):
    def __init__(self):
        self.proxy = None

    @lazy_init
    def getCameraID(self):
        """Returns current camera ID.

        :returns int: Current camera ID.
        """
        return self.proxy.getCameraID()

    @lazy_init
    def getColorSpace(self):
        """Returns current color space.

        :returns int: Current color space.
        """
        return self.proxy.getColorSpace()

    @lazy_init
    def getFrameRate(self):
        """Returns current frame rate.

        :returns int: Current frame rate.
        """
        return self.proxy.getFrameRate()

    @lazy_init
    def getResolution(self):
        """Returns current resolution.

        :returns int: Current resolution.
        """
        return self.proxy.getResolution()

    @lazy_init
    def getVideoFormat(self):
        """Returns current video format.

        :returns str: Current video format.
        """
        return self.proxy.getVideoFormat()

    @lazy_init
    def isRecording(self):
        """Are we currently recording a video

        :returns bool: True/False
        """
        return self.proxy.isRecording()

    @lazy_init
    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    @lazy_init
    def setCameraID(self, cameraID):
        """Sets camera ID.

        :param int cameraID: ID of the camera to use.
        """
        return self.proxy.setCameraID(cameraID)

    @lazy_init
    def setColorSpace(self, colorSpace):
        """Sets color space.

        :param int colorSpace: New color space.
        """
        return self.proxy.setColorSpace(colorSpace)

    @lazy_init
    def setFrameRate(self, frameRate):
        """Sets frame rate.

        :param float frameRate: New frame rate.
        """
        return self.proxy.setFrameRate(frameRate)

    @lazy_init
    def setResolution(self, resolution):
        """Sets resolution.

        :param int resolution: New frame resolution.
        """
        return self.proxy.setResolution(resolution)

    @lazy_init
    def setVideoFormat(self, videoFormat):
        """Sets video format.

        :param str videoFormat: New video format.
        """
        return self.proxy.setVideoFormat(videoFormat)

    @lazy_init
    def startRecording(self, folderPath, fileName):
        """Starts recording a video. Please note that only one record at a time can be made.

        :param str folderPath: Folder where the video is saved.
        :param str fileName: Filename used to save the video.
        """
        return self.proxy.startRecording(folderPath, fileName)

    @lazy_init
    def startRecording2(self, folderPath, fileName, overwrite):
        """Starts recording a video. Please note that only one record at a time can be made.

        :param str folderPath: Folder where the video is saved.
        :param str fileName: Filename used to save the video.
        :param bool overwrite: If false and the filename already exists, an exception is thrown.
        """
        return self.proxy.startRecording(folderPath, fileName, overwrite)

    @lazy_init
    def stopRecording(self):
        """Stops a video record that was launched with startRecording(). The function returns the number of frames that were recorded, as well as the video absolute file name.

        :returns AL::ALValue: Array of two elements [numRecordedFrames, recordAbsolutePath]
        """
        return self.proxy.stopRecording()

    @lazy_init
    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()
