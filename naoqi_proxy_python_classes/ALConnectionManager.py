#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alconnectionmanagerproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


# To not instance network connections until we actually want to
# do a proxy call
def lazy_init(fn):
    def init_if_needed(self, *args, **kwargs):
        if not self.proxy:
            self.proxy = ALProxy("ALConnectionManager")
        return fn(self, *args, **kwargs)
    # Preserve method name and docs
    init_if_needed.__name__ = fn.__name__
    init_if_needed.__doc__ = fn.__doc__
    return init_if_needed


class ALConnectionManager(object):
    def __init__(self):
        self.proxy = None

    @lazy_init
    def connect(self, arg1):
        """

        :param str arg1: arg
        """
        return self.proxy.connect(arg1)

    @lazy_init
    def countries(self):
        """

        :returns std::vector<std::string>: 
        """
        return self.proxy.countries()

    @lazy_init
    def country(self):
        """

        :returns str: 
        """
        return self.proxy.country()

    @lazy_init
    def disableTethering(self, arg1):
        """

        :param str arg1: arg
        """
        return self.proxy.disableTethering(arg1)

    @lazy_init
    def disconnect(self, arg1):
        """

        :param str arg1: arg
        """
        return self.proxy.disconnect(arg1)

    @lazy_init
    def enableTethering(self, arg1, arg2, arg3):
        """

        :param str arg1: arg
        :param str arg2: arg
        :param str arg3: arg
        """
        return self.proxy.enableTethering(arg1, arg2, arg3)

    @lazy_init
    def enableTethering2(self, arg1):
        """

        :param str arg1: arg
        """
        return self.proxy.enableTethering(arg1)

    @lazy_init
    def forget(self, arg1):
        """

        :param str arg1: arg
        """
        return self.proxy.forget(arg1)

    @lazy_init
    def getTetheringEnable(self, arg1):
        """

        :param str arg1: arg
        :returns bool: 
        """
        return self.proxy.getTetheringEnable(arg1)

    @lazy_init
    def interfaces(self):
        """

        :returns AL::ALValue: 
        """
        return self.proxy.interfaces()

    @lazy_init
    def scan(self, arg1):
        """

        :param str arg1: arg
        """
        return self.proxy.scan(arg1)

    @lazy_init
    def scan2(self):
        """
        """
        return self.proxy.scan()

    @lazy_init
    def service(self, arg1):
        """

        :param str arg1: arg
        :returns AL::ALValue: 
        """
        return self.proxy.service(arg1)

    @lazy_init
    def services(self):
        """

        :returns AL::ALValue: 
        """
        return self.proxy.services()

    @lazy_init
    def setCountry(self, arg1):
        """

        :param str arg1: arg
        """
        return self.proxy.setCountry(arg1)

    @lazy_init
    def setServiceConfiguration(self, arg1):
        """

        :param AL::ALValue arg1: arg
        """
        return self.proxy.setServiceConfiguration(arg1)

    @lazy_init
    def setServiceInput(self, arg1):
        """

        :param AL::ALValue arg1: arg
        """
        return self.proxy.setServiceInput(arg1)

    @lazy_init
    def state(self):
        """

        :returns str: 
        """
        return self.proxy.state()

    @lazy_init
    def technologies(self):
        """

        :returns AL::ALValue: 
        """
        return self.proxy.technologies()

    @lazy_init
    def tetheringName(self, arg1):
        """

        :param str arg1: arg
        :returns str: 
        """
        return self.proxy.tetheringName(arg1)

    @lazy_init
    def tetheringPassphrase(self, arg1):
        """

        :param str arg1: arg
        :returns str: 
        """
        return self.proxy.tetheringPassphrase(arg1)
