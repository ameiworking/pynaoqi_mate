#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alpeopleperceptionproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


# To not instance network connections until we actually want to
# do a proxy call
def lazy_init(fn):
    def init_if_needed(self, *args, **kwargs):
        if not self.proxy:
            self.proxy = ALProxy("ALPeoplePerception")
        return fn(self, *args, **kwargs)
    # Preserve method name and docs
    init_if_needed.__name__ = fn.__name__
    init_if_needed.__doc__ = fn.__doc__
    return init_if_needed


class ALPeoplePerception(object):
    def __init__(self):
        self.proxy = None

    @lazy_init
    def getCurrentPeriod(self):
        """Gets the current period.

        :returns int: Refresh period (in milliseconds).
        """
        return self.proxy.getCurrentPeriod()

    @lazy_init
    def getCurrentPrecision(self):
        """Gets the current precision.

        :returns float: Precision of the extractor.
        """
        return self.proxy.getCurrentPrecision()

    @lazy_init
    def getEventList(self):
        """Get the list of events updated in ALMemory.

        :returns std::vector<std::string>: Array of events updated by this extractor in ALMemory
        """
        return self.proxy.getEventList()

    @lazy_init
    def getMaximumBodyHeight(self):
        """Gets the current maximum body height used for human detection (3D mode only).

        :returns float: Maximum height in meters.
        """
        return self.proxy.getMaximumBodyHeight()

    @lazy_init
    def getMaximumDetectionRange(self):
        """Gets the current maximum detection and tracking range.

        :returns float: Maximum range in meters.
        """
        return self.proxy.getMaximumDetectionRange()

    @lazy_init
    def getMemoryKeyList(self):
        """Get the list of events updated in ALMemory.

        :returns std::vector<std::string>: Array of events updated by this extractor in ALMemory
        """
        return self.proxy.getMemoryKeyList()

    @lazy_init
    def getMinimumBodyHeight(self):
        """Gets the current minimum body height used for human detection (3D mode only).

        :returns float: Minimum height in meters.
        """
        return self.proxy.getMinimumBodyHeight()

    @lazy_init
    def getMyPeriod(self, name):
        """Gets the period for a specific subscription.

        :param str name: Name of the module which has subscribed.
        :returns int: Refresh period (in milliseconds).
        """
        return self.proxy.getMyPeriod(name)

    @lazy_init
    def getMyPrecision(self, name):
        """Gets the precision for a specific subscription.

        :param str name: name of the module which has subscribed
        :returns float: precision of the extractor
        """
        return self.proxy.getMyPrecision(name)

    @lazy_init
    def getOutputNames(self):
        """Get the list of values updated in ALMemory.

        :returns std::vector<std::string>: Array of values updated by this extractor in ALMemory
        """
        return self.proxy.getOutputNames()

    @lazy_init
    def getSubscribersInfo(self):
        """Gets the parameters given by the module.

        :returns AL::ALValue: Array of names and parameters of all subscribers.
        """
        return self.proxy.getSubscribersInfo()

    @lazy_init
    def getTimeBeforePersonDisappears(self):
        """Gets the time after which a person, supposed not to be in the field of view of the camera disappears if it has not been detected.

        :returns float: Time in seconds.
        """
        return self.proxy.getTimeBeforePersonDisappears()

    @lazy_init
    def getTimeBeforeVisiblePersonDisappears(self):
        """Gets the time after which a person, supposed to be in the field of view of the camera disappears if it has not been detected.

        :returns float: Time in seconds.
        """
        return self.proxy.getTimeBeforeVisiblePersonDisappears()

    @lazy_init
    def isFaceDetectionEnabled(self):
        """Gets the current status of face detection.

        :returns bool: True if face detection is enabled, False otherwise.
        """
        return self.proxy.isFaceDetectionEnabled()

    @lazy_init
    def isFastModeEnabled(self):
        """Gets the current status of fast mode.

        :returns bool: True if fast mode is enabled, False otherwise.
        """
        return self.proxy.isFastModeEnabled()

    @lazy_init
    def isGraphicalDisplayEnabled(self):
        """Gets the current status of graphical display in Choregraphe.

        :returns bool: True if graphical display is enabled, False otherwise.
        """
        return self.proxy.isGraphicalDisplayEnabled()

    @lazy_init
    def isMovementDetectionEnabled(self):
        """Gets the current status of movement detection in Choregraphe.

        :returns bool: True if movement detection is enabled, False otherwise.
        """
        return self.proxy.isMovementDetectionEnabled()

    @lazy_init
    def isPaused(self):
        """Gets extractor pause status

        :returns bool: True if the extractor is paused, False if not
        """
        return self.proxy.isPaused()

    @lazy_init
    def isProcessing(self):
        """Gets extractor running status

        :returns bool: True if the extractor is currently processing images, False if not
        """
        return self.proxy.isProcessing()

    @lazy_init
    def pause(self, status):
        """Changes the pause status of the extractor

        :param bool status: New pause satus
        """
        return self.proxy.pause(status)

    @lazy_init
    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    @lazy_init
    def resetPopulation(self):
        """Empties the tracked population.
        """
        return self.proxy.resetPopulation()

    @lazy_init
    def setFaceDetectionEnabled(self, enable):
        """Turns face detection on or off.

        :param bool enable: True to turn it on, False to turn it off.
        """
        return self.proxy.setFaceDetectionEnabled(enable)

    @lazy_init
    def setFastModeEnabled(self, enable):
        """Turns fast mode on or off.

        :param bool enable: True to turn it on, False to turn it off.
        """
        return self.proxy.setFastModeEnabled(enable)

    @lazy_init
    def setGraphicalDisplayEnabled(self, enable):
        """Turns graphical display in Choregraphe on or off.

        :param bool enable: True to turn it on, False to turn it off.
        """
        return self.proxy.setGraphicalDisplayEnabled(enable)

    @lazy_init
    def setMaximumBodyHeight(self, height):
        """Sets the maximum human body height (3D mode only).

        :param float height: Maximum height in meters.
        """
        return self.proxy.setMaximumBodyHeight(height)

    @lazy_init
    def setMaximumDetectionRange(self, range):
        """Sets the maximum range for human detection and tracking.

        :param float range: Maximum range in meters.
        """
        return self.proxy.setMaximumDetectionRange(range)

    @lazy_init
    def setMinimumBodyHeight(self, height):
        """Sets the minimum human body height (3D mode only).

        :param float height: Minimum height in meters.
        """
        return self.proxy.setMinimumBodyHeight(height)

    @lazy_init
    def setMovementDetectionEnabled(self, enable):
        """Turns movement detection on or off.

        :param bool enable: True to turn it on, False to turn it off.
        """
        return self.proxy.setMovementDetectionEnabled(enable)

    @lazy_init
    def setTimeBeforePersonDisappears(self, seconds):
        """Sets the time after which a person, supposed not to be in the field of view of the camera disappears if it has not been detected.

        :param float seconds: Time in seconds.
        """
        return self.proxy.setTimeBeforePersonDisappears(seconds)

    @lazy_init
    def setTimeBeforeVisiblePersonDisappears(self, seconds):
        """Sets the time after which a person, supposed to be in the field of view of the camera disappears if it has not been detected.

        :param float seconds: Time in seconds.
        """
        return self.proxy.setTimeBeforeVisiblePersonDisappears(seconds)

    @lazy_init
    def subscribe(self, name, period, precision):
        """Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.

        :param str name: Name of the module which subscribes.
        :param int period: Refresh period (in milliseconds) if relevant.
        :param float precision: Precision of the extractor if relevant.
        """
        return self.proxy.subscribe(name, period, precision)

    @lazy_init
    def subscribe2(self, name):
        """Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.

        :param str name: Name of the module which subscribes.
        """
        return self.proxy.subscribe(name)

    @lazy_init
    def unsubscribe(self, name):
        """Unsubscribes from the extractor.

        :param str name: Name of the module which had subscribed.
        """
        return self.proxy.unsubscribe(name)

    @lazy_init
    def updatePeriod(self, name, period):
        """Updates the period if relevant.

        :param str name: Name of the module which has subscribed.
        :param int period: Refresh period (in milliseconds).
        """
        return self.proxy.updatePeriod(name, period)

    @lazy_init
    def updatePrecision(self, name, precision):
        """Updates the precision if relevant.

        :param str name: Name of the module which has subscribed.
        :param float precision: Precision of the extractor.
        """
        return self.proxy.updatePrecision(name, precision)

    @lazy_init
    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()
