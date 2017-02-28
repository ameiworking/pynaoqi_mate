#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alworldrepresentationproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


# To not instance network connections until we actually want to
# do a proxy call
def lazy_init(fn):
    def init_if_needed(self, *args, **kwargs):
        if not self.proxy:
            self.proxy = ALProxy("ALWorldRepresentation")
        return fn(self, *args, **kwargs)
    # Preserve method name and docs
    init_if_needed.__name__ = fn.__name__
    init_if_needed.__doc__ = fn.__doc__
    return init_if_needed


class ALWorldRepresentation(object):
    def __init__(self):
        self.proxy = None

    @lazy_init
    def addAttributeToCategory(self, arg1, arg2, arg3):
        """Add an attribute to a category.

        :param str arg1: arg
        :param str arg2: arg
        :param AL::ALValue arg3: arg
        :returns int: 
        """
        return self.proxy.addAttributeToCategory(arg1, arg2, arg3)

    @lazy_init
    def clearObject(self, arg1):
        """Clear an object.

        :param str arg1: arg
        :returns int: 
        """
        return self.proxy.clearObject(arg1)

    @lazy_init
    def clearOldPositions(self, arg1, arg2):
        """Clear recording of old positions.

        :param str arg1: arg
        :param int arg2: arg
        :returns int: 
        """
        return self.proxy.clearOldPositions(arg1, arg2)

    @lazy_init
    def createObjectCategory(self, arg1, arg2):
        """Create a new object category

        :param str arg1: arg
        :param bool arg2: arg
        :returns int: 
        """
        return self.proxy.createObjectCategory(arg1, arg2)

    @lazy_init
    def deleteObjectAttribute(self, arg1, arg2, arg3):
        """Delete an object attribute

        :param str arg1: arg
        :param str arg2: arg
        :param str arg3: arg
        :returns int: 
        """
        return self.proxy.deleteObjectAttribute(arg1, arg2, arg3)

    @lazy_init
    def findObject(self, arg1):
        """Check that an object is present.

        :param str arg1: arg
        :returns bool: 
        """
        return self.proxy.findObject(arg1)

    @lazy_init
    def getAttributesFromCategory(self, arg1):
        """Get all attributes from a category if it exists.

        :param str arg1: arg
        :returns AL::ALValue: 
        """
        return self.proxy.getAttributesFromCategory(arg1)

    @lazy_init
    def getChildrenNames(self, arg1):
        """Get the direct children of an object.

        :param str arg1: arg
        :returns std::vector<std::string>: 
        """
        return self.proxy.getChildrenNames(arg1)

    @lazy_init
    def getObjectAttributeValues(self, arg1, arg2, arg3):
        """

        :param str arg1: arg
        :param str arg2: arg
        :param int arg3: arg
        :returns AL::ALValue: 
        """
        return self.proxy.getObjectAttributeValues(arg1, arg2, arg3)

    @lazy_init
    def getObjectAttributes(self, arg1):
        """

        :param str arg1: arg
        :returns AL::ALValue: 
        """
        return self.proxy.getObjectAttributes(arg1)

    @lazy_init
    def getObjectCategory(self, arg1):
        """Get the name of the database where the object is stored.

        :param str arg1: arg
        :returns str: 
        """
        return self.proxy.getObjectCategory(arg1)

    @lazy_init
    def getObjectLatestAttributes(self, arg1, arg2):
        """

        :param str arg1: arg
        :param int arg2: arg
        :returns AL::ALValue: 
        """
        return self.proxy.getObjectLatestAttributes(arg1, arg2)

    @lazy_init
    def getObjectNames(self):
        """Get the name of the objects.

        :returns std::vector<std::string>: 
        """
        return self.proxy.getObjectNames()

    @lazy_init
    def getObjectParentName(self, arg1):
        """

        :param str arg1: arg
        :returns str: 
        """
        return self.proxy.getObjectParentName(arg1)

    @lazy_init
    def getObjectsInCategory(self, arg1):
        """Get the name of the objects stored in the database.

        :param str arg1: arg
        :returns std::vector<std::string>: 
        """
        return self.proxy.getObjectsInCategory(arg1)

    @lazy_init
    def getPosition(self, arg1, arg2):
        """Get the position of an object with quaternion / translation.

        :param str arg1: arg
        :param str arg2: arg
        :returns AL::ALValue: 
        """
        return self.proxy.getPosition(arg1, arg2)

    @lazy_init
    def getPosition6D(self, arg1, arg2):
        """Get the position from one object to another.

        :param str arg1: arg
        :param str arg2: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getPosition6D(arg1, arg2)

    @lazy_init
    def getPosition6DAtTime(self, arg1, arg2, arg3, arg4):
        """Get the interpolated position of an object

        :param str arg1: arg
        :param str arg2: arg
        :param int arg3: arg
        :param int arg4: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getPosition6DAtTime(arg1, arg2, arg3, arg4)

    @lazy_init
    def getRootName(self):
        """

        :returns str: 
        """
        return self.proxy.getRootName()

    @lazy_init
    def load(self):
        """

        :returns int: 
        """
        return self.proxy.load()

    @lazy_init
    def objectCategoryExists(self, arg1):
        """Tells if an object category exists

        :param str arg1: arg
        :returns bool: 
        """
        return self.proxy.objectCategoryExists(arg1)

    @lazy_init
    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    @lazy_init
    def removeObjectCategory(self, arg1):
        """Remove an object category

        :param str arg1: arg
        :returns int: 
        """
        return self.proxy.removeObjectCategory(arg1)

    @lazy_init
    def save(self):
        """

        :returns int: 
        """
        return self.proxy.save()

    @lazy_init
    def select(self, arg1, arg2, arg3, arg4):
        """Select information from a database.

        :param str arg1: arg
        :param str arg2: arg
        :param str arg3: arg
        :param str arg4: arg
        :returns AL::ALValue: 
        """
        return self.proxy.select(arg1, arg2, arg3, arg4)

    @lazy_init
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

    @lazy_init
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

    @lazy_init
    def storeObjectAttribute(self, arg1, arg2, arg3):
        """

        :param str arg1: arg
        :param str arg2: arg
        :param AL::ALValue arg3: arg
        :returns int: 
        """
        return self.proxy.storeObjectAttribute(arg1, arg2, arg3)

    @lazy_init
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

    @lazy_init
    def updateAttribute(self, arg1, arg2, arg3, arg4):
        """

        :param str arg1: arg
        :param str arg2: arg
        :param str arg3: arg
        :param AL::ALValue arg4: arg
        :returns int: 
        """
        return self.proxy.updateAttribute(arg1, arg2, arg3, arg4)

    @lazy_init
    def updatePosition(self, arg1, arg2, arg3):
        """Update the position of an object.

        :param str arg1: arg
        :param std::vector<float> arg2: arg
        :param bool arg3: arg
        :returns int: 
        """
        return self.proxy.updatePosition(arg1, arg2, arg3)

    @lazy_init
    def updatePositionWithReference(self, arg1, arg2, arg3, arg4):
        """Update the position of an object relative to another.

        :param str arg1: arg
        :param str arg2: arg
        :param std::vector<float> arg3: arg
        :param bool arg4: arg
        :returns int: 
        """
        return self.proxy.updatePositionWithReference(arg1, arg2, arg3, arg4)

    @lazy_init
    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()
