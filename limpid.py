#!/usr/bin/env python
 
try:
    import gtk
    import pango
except:
    print >> sys.stderr, "You need to install the python gtk and pango bindings"
    sys.exit(1)
 
# import vte
try:
    import vte
except:
    error = gtk.MessageDialog (None, gtk.DIALOG_MODAL, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK,
        'You need to install python bindings for libvte')
    error.run()
    sys.exit (1)
 
if __name__ == '__main__':
    v = vte.Terminal ()
    v.set_font_full(pango.FontDescription(), vte.ANTI_ALIAS_FORCE_DISABLE)
    v.connect ("child-exited", lambda term: gtk.main_quit())
    v.fork_command()
    window = gtk.Window()
    window.add(v)
    window.connect('delete-event', lambda window, event: gtk.main_quit())
    window.show_all()
    gtk.main()
