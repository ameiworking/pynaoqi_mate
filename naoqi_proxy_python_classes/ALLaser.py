#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/allaserproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


class ALLaser(object):
    def __init__(self):
        self.proxy = ALProxy("ALLaser")

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

    def getUsage(self, name):
        """Gets the method usage string. This summarises how to use the method.

        :param str name: The name of the method.
        :returns str: A string that summarises the usage of the method.
        """
        return self.proxy.getUsage(name)

    def isRunning(self, id):
        """Returns true if the method is currently running.

        :param int id: The ID of the method that was returned when calling the method using 'post'
        :returns bool: True if the method is currently running
        """
        return self.proxy.isRunning(id)

    def laserOFF(self):
        """Disable laser light
        """
        return self.proxy.laserOFF()

    def laserON(self):
        """Enable laser light and sampling
        """
        return self.proxy.laserON()

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

    def setDetectingLength(self, length_min_l, length_max_l):
        """Set detection threshold of the laser

        :param int length_min_l: int containing the min length that the laser will detect(mm), this value must be upper than 20 mm
        :param int length_max_l: int containing the max length that the laser will detect(mm), this value must be lower than 5600 mm
        """
        return self.proxy.setDetectingLength(length_min_l, length_max_l)

    def setOpeningAngle(self, angle_min_f, angle_max_f):
        """Set openning angle of the laser

        :param float angle_min_f: float containing the min value in rad, this value must be upper than -2.35619449
        :param float angle_max_f: float containing the max value in rad, this value must be lower than 2.092349795
        """
        return self.proxy.setOpeningAngle(angle_min_f, angle_max_f)

    def stop(self, id):
        """returns true if the method is currently running

        :param int id: the ID of the method to wait for
        """
        return self.proxy.stop(id)

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
