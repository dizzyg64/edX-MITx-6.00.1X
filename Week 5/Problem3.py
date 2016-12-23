# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:29:43 2016

@author: RichardG
"""

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.Message = Message(text)
        self.valid_words = self.Message.get_valid_words()

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        shiftVal = None
        shiftValDict = {}
        for i in range(26):
            validCount = 0
            temText = self.Message.apply_shift(i).split(' ')
            for word in temText:
                if is_word(self.valid_words, word):
                    validCount += 1
            shiftValDict[validCount] = i
        shiftVal = shiftValDict[max(shiftValDict.keys())]
        return (shiftVal, self.Message.apply_shift(shiftVal))