import subprocess

import glib
import gtk

from sugar.activity.activity import Activity


class GComprisLauncher(Activity):

    def __init__(self, handle):
        # Initialize the parent
        Activity.__init__(self, handle)
        hbox = gtk.HBox()
        self.set_canvas(hbox)
        self.show_all()
        # options = ['gcompris', '--nolockfile', '--native', '--fullscreen', '--noprint']
        options = ['gcompris', '--fullscreen']
        proc = subprocess.Popen(options)

        # Stay alive with a blank window mapped for at least 60 seconds
        # so that the shell knows that we launched
        glib.timeout_add_seconds(60, gtk.main_quit)
        # but get rid of that window if the child exits beforehand
        glib.child_watch_add(proc.pid, gtk.main_quit)

