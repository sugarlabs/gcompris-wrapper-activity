What is this?
=============

GCompris wrapper starts the GCompris application for the Sugar desktop.

How to use?
===========

GCompris wrapper is not part of the Sugar desktop, but can be added.  Please refer to;

* [How to Get Sugar on sugarlabs.org](https://sugarlabs.org/),
* [How to use Sugar](https://help.sugarlabs.org/),

How to upgrade?
===============

On Sugar desktop systems;
* Install GCompris using your operating system package management tools,
* Clone this repository,
* Move the clone repository to the ~/Activities directory,

For example, on Ubuntu;

```
sudo apt install --yes gcompris git
git clone --depth=1 https://github.com/sugarlabs/gcompris-wrapper-activity
rm -r ~/Activities/GCompris.activity
mv tuxpaint-wrapper-activity ~/Activities/GCompris.activity
```

How to integrate?
=================

GCompris wrapper depends on Python, [Sugar Toolkit for GTK+ 3](https://github.com/sugarlabs/sugar-toolkit-gtk3), and GCompris.
