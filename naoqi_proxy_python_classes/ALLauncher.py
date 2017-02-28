#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/allauncherproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


# To not instance network connections until we actually want to
# do a proxy call
def lazy_init(fn):
    def init_if_needed(self, *args, **kwargs):
        if not self.proxy:
            self.proxy = ALProxy("ALLauncher")
        return fn(self, *args, **kwargs)
    # Preserve method name and docs
    init_if_needed.__name__ = fn.__name__
    init_if_needed.__doc__ = fn.__doc__
    return init_if_needed


class ALLauncher(object):
    def __init__(self):
        self.proxy = None

    @lazy_init
    def getGlobalModuleList(self):
        """get the list of modules loaded on the robot and connected on the robot

        :returns std::vector<std::string>: array of present modules
        """
        return self.proxy.getGlobalModuleList()

    @lazy_init
    def isModulePresent(self, strPartOfModuleName):
        """Tests the existence of an active module in the global system (in same executable or in another executable of the distributed system)

        :param str strPartOfModuleName: a part of the name of the module to test existence
        :returns bool: the returned value is true if this module is present
        """
        return self.proxy.isModulePresent(strPartOfModuleName)

    @lazy_init
    def launchExecutable(self, moduleName):
        """runs an executable and connect it to current broker (executable)

        :param str moduleName: the name of the module to launch or the name of the script file to execute
        :returns bool: true if ok
        """
        return self.proxy.launchExecutable(moduleName)

    @lazy_init
    def launchLocal(self, moduleName):
        """Loads dynamicaly a module

        :param str moduleName: the name of the module to launch or the name of the python script to evaluate
        :returns std::vector<std::string>: list of modules loaded
        """
        return self.proxy.launchLocal(moduleName)

    @lazy_init
    def launchPythonModule(self, moduleName):
        """Import a python module

        :param str moduleName: the name of the module to launch
        :returns bool: true if ok
        """
        return self.proxy.launchPythonModule(moduleName)

    @lazy_init
    def launchScript(self, moduleName):
        """runs a script connected the current broker

        :param str moduleName: the name of the script to launch (python)
        :returns bool: true if ok
        """
        return self.proxy.launchScript(moduleName)

    @lazy_init
    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    @lazy_init
    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()
