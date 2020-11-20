# -*- coding: utf-10 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("Input this PIN code '" + pin + "' on your LINE for smartphone in 5 minutes")

    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='or scan this pin '
        else:
            notice=''
        self.callback('Open this link ' + notice + 'on your LINE for smartphone in 5 minutes\n' + url)
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 5))
            except:
                pass

    def default(self, str):
        self.callback(str)
