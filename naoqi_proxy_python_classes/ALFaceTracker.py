#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alfacetrackerproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


class ALFaceTracker(object):
    def __init__(self):
        self.proxy = ALProxy("ALFaceTracker")

    def getGenericProxy(self):
        """Gets the underlying generic proxy

        :returns boost::shared_ptr<ALProxy>: 
        """
        return self.proxy.getGenericProxy()

    def exit(self):
        """Exits and unregisters the module.
        """
        return self.proxy.exit()

    def getBrokerName(self):
        """Gets the name of the parent broker.

        :returns str: The name of the parent broker.
        """
        return self.proxy.getBrokerName()

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

    def getPosition(self):
        """Return the [x, y, z] position of the face in FRAME_TORSO. This is done assuming an average face size, so it might not be very accurate.  This invalidates the isNewData field of the tracker. See isNewData()) for more details.

        :returns std::vector<float>: An Array containing the face position [x, y, z].
        """
        return self.proxy.getPosition()

    def getUsage(self, name):
        """Gets the method usage string. This summarises how to use the method.

        :param str name: The name of the method.
        :returns str: A string that summarises the usage of the method.
        """
        return self.proxy.getUsage(name)

    def isActive(self):
        """Return true if the face Tracker is running.

        :returns bool: true if the face Tracker is running.
        """
        return self.proxy.isActive()

    def isNewData(self):
        """Return true if a new face was detected since the last getPosition().

        :returns bool: true if a new face was detected since the last getPosition().
        """
        return self.proxy.isNewData()

    def isRunning(self, id):
        """Returns true if the method is currently running.

        :param int id: The ID of the method that was returned when calling the method using 'post'
        :returns bool: True if the method is currently running
        """
        return self.proxy.isRunning(id)

    def pCall(self):
        """NAOqi1 pCall method.

        :returns AL::ALValue: 
        """
        return self.proxy.pCall()

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    def setWholeBodyOn(self, pWholeBodyOn):
        """if true, the tracking will be through a Whole Body Process.

        :param bool pWholeBodyOn: The whole Body state
        """
        return self.proxy.setWholeBodyOn(pWholeBodyOn)

    def startTracker(self):
        """Start the tracker by Subscribing to Event FaceDetected from ALFaceDetection module. Then Wait Event FaceDetected from ALFaceDetection module. And finally send information to motion for head tracking. NOTE: Stiffness of Head must be set to 1.0 to move!
        """
        return self.proxy.startTracker()

    def stop(self, id):
        """returns true if the method is currently running

        :param int id: the ID of the method to wait for
        """
        return self.proxy.stop(id)

    def stopTracker(self):
        """Stop the tracker by Unsubscribing to Event FaceDetected from ALFaceDetection module.
        """
        return self.proxy.stopTracker()

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
