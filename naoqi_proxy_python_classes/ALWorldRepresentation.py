#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alworldrepresentationproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


class ALWorldRepresentation(object):
    def __init__(self):
        self.proxy = ALProxy("ALWorldRepresentation")

    def getGenericProxy(self):
        """Gets the underlying generic proxy

        :returns boost::shared_ptr<ALProxy>: 
        """
        return self.proxy.getGenericProxy()

    def addAttributeToCategory(self, arg1, arg2, arg3):
        """Add an attribute to a category.

        :param str arg1: arg
        :param str arg2: arg
        :param AL::ALValue arg3: arg
        :returns int: 
        """
        return self.proxy.addAttributeToCategory(arg1, arg2, arg3)

    def clearObject(self, arg1):
        """Clear an object.

        :param str arg1: arg
        :returns int: 
        """
        return self.proxy.clearObject(arg1)

    def clearOldPositions(self, arg1, arg2):
        """Clear recording of old positions.

        :param str arg1: arg
        :param int arg2: arg
        :returns int: 
        """
        return self.proxy.clearOldPositions(arg1, arg2)

    def createObjectCategory(self, arg1, arg2):
        """Create a new object category

        :param str arg1: arg
        :param bool arg2: arg
        :returns int: 
        """
        return self.proxy.createObjectCategory(arg1, arg2)

    def deleteObjectAttribute(self, arg1, arg2, arg3):
        """Delete an object attribute

        :param str arg1: arg
        :param str arg2: arg
        :param str arg3: arg
        :returns int: 
        """
        return self.proxy.deleteObjectAttribute(arg1, arg2, arg3)

    def exit(self):
        """Exits and unregisters the module.
        """
        return self.proxy.exit()

    def findObject(self, arg1):
        """Check that an object is present.

        :param str arg1: arg
        :returns bool: 
        """
        return self.proxy.findObject(arg1)

    def getAttributesFromCategory(self, arg1):
        """Get all attributes from a category if it exists.

        :param str arg1: arg
        :returns AL::ALValue: 
        """
        return self.proxy.getAttributesFromCategory(arg1)

    def getBrokerName(self):
        """Gets the name of the parent broker.

        :returns str: The name of the parent broker.
        """
        return self.proxy.getBrokerName()

    def getChildrenNames(self, arg1):
        """Get the direct children of an object.

        :param str arg1: arg
        :returns std::vector<std::string>: 
        """
        return self.proxy.getChildrenNames(arg1)

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

    def getObjectAttributeValues(self, arg1, arg2, arg3):
        """

        :param str arg1: arg
        :param str arg2: arg
        :param int arg3: arg
        :returns AL::ALValue: 
        """
        return self.proxy.getObjectAttributeValues(arg1, arg2, arg3)

    def getObjectAttributes(self, arg1):
        """

        :param str arg1: arg
        :returns AL::ALValue: 
        """
        return self.proxy.getObjectAttributes(arg1)

    def getObjectCategory(self, arg1):
        """Get the name of the database where the object is stored.

        :param str arg1: arg
        :returns str: 
        """
        return self.proxy.getObjectCategory(arg1)

    def getObjectLatestAttributes(self, arg1, arg2):
        """

        :param str arg1: arg
        :param int arg2: arg
        :returns AL::ALValue: 
        """
        return self.proxy.getObjectLatestAttributes(arg1, arg2)

    def getObjectNames(self):
        """Get the name of the objects.

        :returns std::vector<std::string>: 
        """
        return self.proxy.getObjectNames()

    def getObjectParentName(self, arg1):
        """

        :param str arg1: arg
        :returns str: 
        """
        return self.proxy.getObjectParentName(arg1)

    def getObjectsInCategory(self, arg1):
        """Get the name of the objects stored in the database.

        :param str arg1: arg
        :returns std::vector<std::string>: 
        """
        return self.proxy.getObjectsInCategory(arg1)

    def getPosition(self, arg1, arg2):
        """Get the position of an object with quaternion / translation.

        :param str arg1: arg
        :param str arg2: arg
        :returns AL::ALValue: 
        """
        return self.proxy.getPosition(arg1, arg2)

    def getPosition6D(self, arg1, arg2):
        """Get the position from one object to another.

        :param str arg1: arg
        :param str arg2: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getPosition6D(arg1, arg2)

    def getPosition6DAtTime(self, arg1, arg2, arg3, arg4):
        """Get the interpolated position of an object

        :param str arg1: arg
        :param str arg2: arg
        :param int arg3: arg
        :param int arg4: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getPosition6DAtTime(arg1, arg2, arg3, arg4)

    def getRootName(self):
        """

        :returns str: 
        """
        return self.proxy.getRootName()

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

    def load(self):
        """

        :returns int: 
        """
        return self.proxy.load()

    def objectCategoryExists(self, arg1):
        """Tells if an object category exists

        :param str arg1: arg
        :returns bool: 
        """
        return self.proxy.objectCategoryExists(arg1)

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

    def removeObjectCategory(self, arg1):
        """Remove an object category

        :param str arg1: arg
        :returns int: 
        """
        return self.proxy.removeObjectCategory(arg1)

    def save(self):
        """

        :returns int: 
        """
        return self.proxy.save()

    def select(self, arg1, arg2, arg3, arg4):
        """Select information from a database.

        :param str arg1: arg
        :param str arg2: arg
        :param str arg3: arg
        :param str arg4: arg
        :returns AL::ALValue: 
        """
        return self.proxy.select(arg1, arg2, arg3, arg4)

    def selectWithOrder(self, arg1, arg2, arg3, arg4, arg5):
        """Select ordered information from a database.

        :param str arg1: arg
        :param str arg2: arg
        :param str arg3: arg
        :param str arg4: arg
        :param str arg5: arg
        :returns AL::ALValue: 
        """
        return self.proxy.selectWithOrder(arg1, arg2, arg3, arg4, arg5)

    def stop(self, id):
        """returns true if the method is currently running

        :param int id: the ID of the method to wait for
        """
        return self.proxy.stop(id)

    def storeObject(self, arg1, arg2, arg3, arg4, arg5):
        """

        :param str arg1: arg
        :param str arg2: arg
        :param std::vector<float> arg3: arg
        :param str arg4: arg
        :param AL::ALValue arg5: arg
        :returns int: 
        """
        return self.proxy.storeObject(arg1, arg2, arg3, arg4, arg5)

    def storeObjectAttribute(self, arg1, arg2, arg3):
        """

        :param str arg1: arg
        :param str arg2: arg
        :param AL::ALValue arg3: arg
        :returns int: 
        """
        return self.proxy.storeObjectAttribute(arg1, arg2, arg3)

    def storeObjectWithReference(self, arg1, arg2, arg3, arg4, arg5, arg6):
        """

        :param str arg1: arg
        :param str arg2: arg
        :param str arg3: arg
        :param std::vector<float> arg4: arg
        :param str arg5: arg
        :param AL::ALValue arg6: arg
        :returns int: 
        """
        return self.proxy.storeObjectWithReference(arg1, arg2, arg3, arg4, arg5, arg6)

    def updateAttribute(self, arg1, arg2, arg3, arg4):
        """

        :param str arg1: arg
        :param str arg2: arg
        :param str arg3: arg
        :param AL::ALValue arg4: arg
        :returns int: 
        """
        return self.proxy.updateAttribute(arg1, arg2, arg3, arg4)

    def updatePosition(self, arg1, arg2, arg3):
        """Update the position of an object.

        :param str arg1: arg
        :param std::vector<float> arg2: arg
        :param bool arg3: arg
        :returns int: 
        """
        return self.proxy.updatePosition(arg1, arg2, arg3)

    def updatePositionWithReference(self, arg1, arg2, arg3, arg4):
        """Update the position of an object relative to another.

        :param str arg1: arg
        :param str arg2: arg
        :param std::vector<float> arg3: arg
        :param bool arg4: arg
        :returns int: 
        """
        return self.proxy.updatePositionWithReference(arg1, arg2, arg3, arg4)

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
