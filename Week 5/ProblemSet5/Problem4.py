# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:31:20 2016

@author: RichardG
"""

def decrypt_story():
    tmpStory = CiphertextMessage(get_story_string())
    return(tmpStory.decrypt_message())