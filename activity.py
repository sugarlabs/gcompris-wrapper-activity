import subprocess

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import GLib
from gi.repository import Gtk

from sugar3.activity.activity import Activity


class GComprisLauncher(Activity):

    def __init__(self, handle):
        # Initialize the parent
        Activity.__init__(self, handle)

        self.max_participants = 1

        hbox = Gtk.HBox()
        self.set_canvas(hbox)
        self.show_all()
        options = ['gcompris', '--fullscreen']
        proc = subprocess.Popen(options)

        # Stay alive with a blank window mapped for at least 60 seconds
        # so that the shell knows that we launched
        GLib.timeout_add_seconds(60, Gtk.main_quit)
        # but get rid of that window if the child exits beforehand
        GLib.child_watch_add(proc.pid, Gtk.main_quit)
