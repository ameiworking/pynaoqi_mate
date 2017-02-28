#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alanimatedspeechproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


# To not instance network connections until we actually want to
# do a proxy call
def lazy_init(fn):
    def init_if_needed(self, *args, **kwargs):
        if not self.proxy:
            self.proxy = ALProxy("ALAnimatedSpeech")
        return fn(self, *args, **kwargs)
    # Preserve method name and docs
    init_if_needed.__name__ = fn.__name__
    init_if_needed.__doc__ = fn.__doc__
    return init_if_needed


class ALAnimatedSpeech(object):
    def __init__(self):
        self.proxy = None

    @lazy_init
    def addTagsToWords(self, tagsToWords):
        """Add some new links between tags and words.

        :param AL::ALValue tagsToWords: Map of tags to words.
        """
        return self.proxy.addTagsToWords(tagsToWords)

    @lazy_init
    def declareAnimationsPackage(self, animationsPackage):
        """Add a new package that contains animations.

        :param str animationsPackage: The new package that contains animations.
        """
        return self.proxy.declareAnimationsPackage(animationsPackage)

    @lazy_init
    def declareTagForAnimations(self, tagsToAnimations):
        """Declare some tags with the associated animations.

        :param AL::ALValue tagsToAnimations: Map of Tags to Animations.
        """
        return self.proxy.declareTagForAnimations(tagsToAnimations)

    @lazy_init
    def getBodyLanguageMode(self):
        """Set the current body language mode. 3 modes exist: BODY_LANGUAGE_MODE_DISABLED,BODY_LANGUAGE_MODE_RANDOM and BODY_LANGUAGE_MODE_CONTEXTUAL (see BodyLanguageMode enum for more details)

        :returns qi::uint32_t: The current body language mode.
        """
        return self.proxy.getBodyLanguageMode()

    @lazy_init
    def getBodyLanguageModeToStr(self):
        """Set the current body language mode. 3 modes exist: "disabled", "random" and "contextual" (see BodyLanguageMode enum for more details)

        :returns str: The current body language mode.
        """
        return self.proxy.getBodyLanguageModeToStr()

    @lazy_init
    def isBodyLanguageEnabled(self):
        """DEPRECATED since 1.22: use getBodyLanguageMode instead.Indicate if the body language is enabled or not.

        :returns bool: The boolean value: true means it is enabled, false means it is disabled.
        """
        return self.proxy.isBodyLanguageEnabled()

    @lazy_init
    def isBodyTalkEnabled(self):
        """DEPRECATED since 1.18: use getBodyLanguageMode instead.Indicate if the body talk is enabled or not.

        :returns bool: The boolean value: true means it is enabled, false means it is disabled.
        """
        return self.proxy.isBodyTalkEnabled()

    @lazy_init
    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    @lazy_init
    def say(self, text):
        """Say the annotated text given in parameter and animate it with animations inserted in the text.

        :param str text: An annotated text (for example: "Hello. ^start(Hey_1) My name is NAO").
        """
        return self.proxy.say(text)

    @lazy_init
    def say2(self, text, configuration):
        """Say the annotated text given in parameter and animate it with animations inserted in the text.

        :param str text: An annotated text (for example: "Hello. ^start(Hey_1) My name is NAO").
        :param AL::ALValue configuration: The animated speech configuration.
        """
        return self.proxy.say(text, configuration)

    @lazy_init
    def setBodyLanguageEnabled(self, enable):
        """DEPRECATED since 1.22: use setBodyLanguageMode instead.Enable or disable the automatic body language on the speech.If it is enabled, anywhere you have not annotate your text with animation,the robot will fill the gap with automatically calculated gestures.If it is disabled, the robot will move only where you annotate it withanimations.

        :param bool enable: The boolean value: true to enable, false to disable.
        """
        return self.proxy.setBodyLanguageEnabled(enable)

    @lazy_init
    def setBodyLanguageMode(self, bodyLanguageMode):
        """Set the current body language mode. 3 modes exist: BODY_LANGUAGE_MODE_DISABLED,BODY_LANGUAGE_MODE_RANDOM and BODY_LANGUAGE_MODE_CONTEXTUAL (see BodyLanguageMode enum for more details)

        :param qi::uint32_t bodyLanguageMode: The choosen body language mode.
        """
        return self.proxy.setBodyLanguageMode(bodyLanguageMode)

    @lazy_init
    def setBodyLanguageModeFromStr(self, stringBodyLanguageMode):
        """Set the current body language mode. 3 modes exist: "disabled", "random" and "contextual" (see BodyLanguageMode enum for more details)

        :param str stringBodyLanguageMode: The choosen body language mode.
        """
        return self.proxy.setBodyLanguageModeFromStr(stringBodyLanguageMode)

    @lazy_init
    def setBodyTalkEnabled(self, enable):
        """DEPRECATED since 1.18: use setBodyLanguageMode instead.Enable or disable the automatic body talk on the speech.If it is enabled, anywhere you have not annotate your text with animation,the robot will fill the gap with automatically calculated gestures.If it is disabled, the robot will move only where you annotate it withanimations.

        :param bool enable: The boolean value: true to enable, false to disable.
        """
        return self.proxy.setBodyTalkEnabled(enable)

    @lazy_init
    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()
