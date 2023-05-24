# coding=utf-8
"""
Main class for addon launch
"""
import sys
import xbmcaddon

# Script constants
__addon__ = xbmcaddon.Addon(id='script.mldonkey')
__title__ = __addon__.getAddonInfo('name')
__version__ = __addon__.getAddonInfo('version')
__language__ = __addon__.getLocalizedString
__cwd__ = __addon__.getAddonInfo('path')

if __name__ == '__main__':

    import resources.lib.view_files as view_files
    import resources.lib.mytools as mytools
    mytools.log("[SCRIPT] '%s: version %s' initialized!" % (__addon__, __version__, ))
    window = view_files.GUI(__title__)
    window.doModal()
    # Destroy the instance explicitly because
    # underlying xbmcgui classes are not garbage-collected on exit.
    del window

sys.modules.clear()
