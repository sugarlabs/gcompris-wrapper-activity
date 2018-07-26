# Copyright (C) 2012-2018 One Laptop per Child

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

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
