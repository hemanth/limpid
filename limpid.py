#!/bin/python
"""
@author: Hemanth.HM
@contact: hemanth.hm@gmail.com
@license: GNU GPLV3
@version: Beta

"""
import gtk
import vte 
import webkit
    
class Limpid:
    
    def resize(self,widget,data=None):
        ''' Get current allocation co-ordinates and resize back to the same '''
        x, y, w, h = widget.get_allocation()
        widget.disconnect(widget.connection_id)
        widget.unmaximize()
        widget.window.move_resize(x, y, w, h)
        
    def destroy(self,widget):
        gtk.main_quit()

    def __init__(self):
       
        ''' Using python-vte VteTerminal A terminal widget implementation '''
        
        vt = vte.Terminal ()
        vt.connect ("child-exited", lambda term: gtk.main_quit())
        vt.fork_command()
        
        ''' Create the main gtk Window, with title as Code with me '''
        window = gtk.Window()
        ''' Set request, later maximize '''
        window.set_size_request(1024,768)
        window.set_title("Limpid")
        
        ''' Webit.Webview to load the irc page
            Yes i know gtkmozembed, but that just an overhead in this case! 
            TODO : load_progress signal handler '''
            
        irc = webkit.WebView()
        ''' Change the below URI for your requirement '''
        irc.open("http://webchat.freenode.net?channels=p2pu-webcraft/scripting-101&uio=OT10cnVlJjExPTIyNge7")
    
        ''' Create a Vpanel, which will hold the VBoxes '''
        vp = gtk.VPaned()
        '''Set its initial position to be 400''' 
        vp.set_position(400)
        
   
        ''' VBox1 holds the vt, homogeneous set to false and spacing is 5 '''
        vtBox = gtk.VBox(False,5)
        vtBox.pack_start(vt)
        vtBox.show()
   
        ''' Vbox2 holds the web based irc loaded from the webkit, 
            homogeneous set to false and spacing is 5 '''
        chat = gtk.VBox(False,5)
        chat.pack_start(irc)
        chat.show()
       
        '''
        Add vt/chat to scroll window if required
        scroll = gtk.ScrolledWindow()
        scroll.add_with_viewport(chat) '''
        
        ''' Add the Vboxes to Vpanel and show them '''
        vp.add1(chat)
        vp.show()
        vp.add2(vtBox)
        vp.show()
   
        ''' Add Vpanel to the main window and show_all '''
        window.add(vp)
        
        ''' Connect window to gtk.main_quit(), a delete-event '''
        window.connect('destroy',self.destroy)
        window.show_all()
        
        ''' In case you turns to resize the window, by unmaximizing '''
        window.connection_id = window.connect('size-request', self.resize)
        window.maximize()


    def main(self):
        ''' Invoke the main loop of gtk '''
        gtk.main()

if __name__ == "__main__":
    ''' Create code instance of CodeWithMe class '''
    limp = Limpid()
    ''' Invoke the main method '''
    limp.main()
