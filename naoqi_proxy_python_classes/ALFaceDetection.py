#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alfacedetectionproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


class ALFaceDetection(object):
    def __init__(self):
        self.proxy = ALProxy("ALFaceDetection")

    def getGenericProxy(self):
        """Gets the underlying generic proxy

        :returns boost::shared_ptr<ALProxy>: 
        """
        return self.proxy.getGenericProxy()

    def clearDatabase(self):
        """Remove all faces from the database.

        :returns bool: true if the operation succeeds
        """
        return self.proxy.clearDatabase()

    def enableRecognition(self, arg1):
        """deprecated

        :param bool arg1: arg
        """
        return self.proxy.enableRecognition(arg1)

    def enableTracking(self, arg1):
        """deprecated

        :param bool arg1: arg
        """
        return self.proxy.enableTracking(arg1)

    def exit(self):
        """Exits and unregisters the module.
        """
        return self.proxy.exit()

    def forgetPerson(self, pId):
        """Delete from the database all faces instances of a person.

        :param str pId: The name of the person to forget
        :returns bool: true if the operation succeeds
        """
        return self.proxy.forgetPerson(pId)

    def getActiveCamera(self):
        """Gets extractor active camera

        :returns int: Id of the current active camera of the extractor
        """
        return self.proxy.getActiveCamera()

    def getBrokerName(self):
        """Gets the name of the parent broker.

        :returns str: The name of the parent broker.
        """
        return self.proxy.getBrokerName()

    def getCurrentPeriod(self):
        """Gets the current period.

        :returns int: Refresh period (in milliseconds).
        """
        return self.proxy.getCurrentPeriod()

    def getCurrentPrecision(self):
        """Gets the current precision.

        :returns float: Precision of the extractor.
        """
        return self.proxy.getCurrentPrecision()

    def getEventList(self):
        """Get the list of events updated in ALMemory.

        :returns std::vector<std::string>: Array of events updated by this extractor in ALMemory
        """
        return self.proxy.getEventList()

    def getFrameRate(self):
        """Gets extractor framerate

        :returns int: Current value of the framerate of the extractor
        """
        return self.proxy.getFrameRate()

    def getLearnedFacesList(self):
        """Returns the list of learned faces.

        :returns AL::ALValue: List of names
        """
        return self.proxy.getLearnedFacesList()

    def getMemoryKeyList(self):
        """Get the list of events updated in ALMemory.

        :returns std::vector<std::string>: Array of events updated by this extractor in ALMemory
        """
        return self.proxy.getMemoryKeyList()

    def getMethodHelp(self, methodName):
        """Retrieves a method's description.

        :param str methodName: The name of the method.
        :returns AL::ALValue: A structure containing the method's description.
        """
        return self.proxy.getMethodHelp(methodName)

    def getMethodList(self):
        """Retrieves the module's method list.

        :returns std::vector<std::string>: An array of method names.
        """
        return self.proxy.getMethodList()

    def getModuleHelp(self):
        """Retrieves the module's description.

        :returns AL::ALValue: A structure describing the module.
        """
        return self.proxy.getModuleHelp()

    def getMyPeriod(self, name):
        """Gets the period for a specific subscription.

        :param str name: Name of the module which has subscribed.
        :returns int: Refresh period (in milliseconds).
        """
        return self.proxy.getMyPeriod(name)

    def getMyPrecision(self, name):
        """Gets the precision for a specific subscription.

        :param str name: name of the module which has subscribed
        :returns float: precision of the extractor
        """
        return self.proxy.getMyPrecision(name)

    def getOutputNames(self):
        """Get the list of values updated in ALMemory.

        :returns std::vector<std::string>: Array of values updated by this extractor in ALMemory
        """
        return self.proxy.getOutputNames()

    def getResolution(self):
        """Gets extractor resolution

        :returns int: Current value of the resolution of the extractor
        """
        return self.proxy.getResolution()

    def getSubscribersInfo(self):
        """Gets the parameters given by the module.

        :returns AL::ALValue: Array of names and parameters of all subscribers.
        """
        return self.proxy.getSubscribersInfo()

    def getUsage(self, name):
        """Gets the method usage string. This summarises how to use the method.

        :param str name: The name of the method.
        :returns str: A string that summarises the usage of the method.
        """
        return self.proxy.getUsage(name)

    def importOldDatabase(self, policy):
        """Imports the content of an old face reco DB

        :param str policy: Merging policy if an imported entry has the same name as an existing one. It can be either: "overwrite" to replace the existing entry by the imported one, "merge" to merge data from both entries (if they don't relate to the same person, face recognition may fail), "keep" to keep the existing entry and skip the imported one.
        :returns bool: True if the import succeeded, false otherwise.
        """
        return self.proxy.importOldDatabase(policy)

    def isPaused(self):
        """Gets extractor pause status

        :returns bool: True if the extractor is paused, False if not
        """
        return self.proxy.isPaused()

    def isProcessing(self):
        """Gets extractor running status

        :returns bool: True if the extractor is currently processing images, False if not
        """
        return self.proxy.isProcessing()

    def isRecognitionEnabled(self):
        """Returns if recognition is enabled.

        :returns bool: True/False
        """
        return self.proxy.isRecognitionEnabled()

    def isRunning(self, id):
        """Returns true if the method is currently running.

        :param int id: The ID of the method that was returned when calling the method using 'post'
        :returns bool: True if the method is currently running
        """
        return self.proxy.isRunning(id)

    def isTrackingEnabled(self):
        """(BETA) Returns if tracking is enabled.

        :returns bool: True/False
        """
        return self.proxy.isTrackingEnabled()

    def learnFace(self, pId):
        """Add a new face in the database.

        :param str pId: The name of the person to save
        :returns bool: true if the operation succeeds
        """
        return self.proxy.learnFace(pId)

    def pCall(self):
        """NAOqi1 pCall method.

        :returns AL::ALValue: 
        """
        return self.proxy.pCall()

    def pause(self, paused):
        """Changes the pause status of the extractor

        :param bool paused: New pause satus
        """
        return self.proxy.pause(paused)

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    def reLearnFace(self, pId):
        """use in a new learning process the latest images where a face has been wrongly recognized

        :param str pId: The name of the person to save
        :returns bool: true if the operation succeeds
        """
        return self.proxy.reLearnFace(pId)

    def setActiveCamera(self, cameraId):
        """Sets extractor active camera

        :param int cameraId: Id of the camera that will become the active camera
        :returns bool: True if the update succeeded, False if not
        """
        return self.proxy.setActiveCamera(cameraId)

    def setFrameRate(self, subscriberName, framerate):
        """Sets the extractor framerate for a chosen subscriber

        :param str subscriberName: Name of the subcriber
        :param int framerate: New framerate
        :returns bool: True if the update succeeded, False if not
        """
        return self.proxy.setFrameRate(subscriberName, framerate)

    def setFrameRate2(self, framerate):
        """Sets the extractor framerate for all the subscribers

        :param int framerate: New framerate
        :returns bool: True if the update succeeded, False if not
        """
        return self.proxy.setFrameRate(framerate)

    def setParameter(self, paramName, value):
        """DEPRECATED: Sets pause and resolution

        :param str paramName: Name of the parameter to set
        :param AL::ALValue value: New value
        """
        return self.proxy.setParameter(paramName, value)

    def setRecognitionEnabled(self, enable):
        """enable/disable the recognition stageProcess will be faster when disabled when you don't need to recognize people

        :param bool enable: True/False
        """
        return self.proxy.setRecognitionEnabled(enable)

    def setResolution(self, resolution):
        """Sets extractor resolution

        :param int resolution: New resolution
        :returns bool: True if the update succeeded, False if not
        """
        return self.proxy.setResolution(resolution)

    def setTrackingEnabled(self, enable):
        """(BETA) Choose to enable or disable tracking. Enabling tracking usually allows you to follow a face for a longer period of time. However, it can lead to more false detections.

        :param bool enable: True/False
        """
        return self.proxy.setTrackingEnabled(enable)

    def stop(self, id):
        """returns true if the method is currently running

        :param int id: the ID of the method to wait for
        """
        return self.proxy.stop(id)

    def subscribe(self, name, period, precision):
        """Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.

        :param str name: Name of the module which subscribes.
        :param int period: Refresh period (in milliseconds) if relevant.
        :param float precision: Precision of the extractor if relevant.
        """
        return self.proxy.subscribe(name, period, precision)

    def subscribe2(self, name):
        """Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.

        :param str name: Name of the module which subscribes.
        """
        return self.proxy.subscribe(name)

    def unsubscribe(self, name):
        """Unsubscribes from the extractor.

        :param str name: Name of the module which had subscribed.
        """
        return self.proxy.unsubscribe(name)

    def updatePeriod(self, name, period):
        """Updates the period if relevant.

        :param str name: Name of the module which has subscribed.
        :param int period: Refresh period (in milliseconds).
        """
        return self.proxy.updatePeriod(name, period)

    def updatePrecision(self, name, precision):
        """Updates the precision if relevant.

        :param str name: Name of the module which has subscribed.
        :param float precision: Precision of the extractor.
        """
        return self.proxy.updatePrecision(name, precision)

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()

    def wait(self, id, timeoutPeriod):
        """Wait for the end of a long running method that was called using 'post'

        :param int id: The ID of the method that was returned when calling the method using 'post'
        :param int timeoutPeriod: The timeout period in ms. To wait indefinately, use a timeoutPeriod of zero.
        :returns bool: True if the timeout period terminated. False if the method returned.
        """
        return self.proxy.wait(id, timeoutPeriod)
