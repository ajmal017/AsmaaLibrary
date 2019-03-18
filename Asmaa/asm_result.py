# -*- coding: utf-8 -*-

##############################################################################
#a########  "قُلۡ بِفَضلِ ٱللَّهِ وَبِرَحمَتِهِۦ فَبِذَٰلِكَ فَليَفرَحُواْ هُوَ خَيرُُ مِّمَّا يَجمَعُونَ"  #########
##############################################################################

from os.path import join
import os, cPickle
from gi.repository import Gtk
from asm_search import ShowResult
from asm_tablabel import TabLabel
import asm_customs, asm_path

class SavedResult(Gtk.Dialog):
    
    def ok_m(self,*a):
        (model, i) = self.tree_sav.get_selection().get_selected()
        if i :
            nm = model.get_value(i,0).decode('utf8')
            self.parent.notebook.set_current_page(1)
            sr = ShowResult(self.parent)
            sr.hb_stop.hide()
            self.parent.viewerbook.append_page(sr,TabLabel(sr, nm))
            self.parent.viewerbook.set_current_page(-1)
            store = cPickle.load(file(join(asm_path.HOME_DIR, nm+u".pkl")))
            sr.results_books = store
            sr.lab_n_result.set_text('عدد النتائج : {}'.format(len(store), ))
            self.destroy()
            for a in store:
                while (Gtk.events_pending()): Gtk.main_iteration()
                sr.store_results.append(a)
                
    def remove_iter(self, *a):
        (model, i) = self.tree_sav.get_selection().get_selected()
        if i :
            res_self = asm_customs.sure(self, " هل ترغب في حذف النتيجة المحددة ؟")
            if res_self:
                nm = model.get_value(i,0)
                os.remove(join(asm_path.HOME_DIR, nm+'.pkl'))
                self.store_sav.remove(i)
                
    def remove_iters(self, *a):
        res_self = asm_customs.sure(self, " هل ترغب في حذف جميع النتائج الموجودة ؟")
        if res_self:
            for a in self.list_n:
                if a[-4:] == '.pkl':
                    os.remove(join(asm_path.HOME_DIR, a))
            self.store_sav.clear()
    
    def __init__(self, parent):
        self.parent = parent
        Gtk.Dialog.__init__(self, parent=self.parent)
        self.set_icon_name("asmaa")
        area = self.get_content_area()
        area.set_spacing(6)
        self.set_title('نتائج البحوث المحفوظة')
        self.set_default_size(350, 300)
        box = Gtk.Box(spacing=6,orientation=Gtk.Orientation.VERTICAL)
        self.store_sav = Gtk.ListStore(str)
        self.list_n = os.listdir(asm_path.HOME_DIR)
        self.store_sav.clear()
        for v in self.list_n:
            if '.pkl' in v:
                nm = v.replace('.pkl', '')
                self.store_sav.append([nm])
        self.tree_sav = asm_customs.TreeIndex()
        self.tree_sav.connect("row-activated", self.ok_m)
        column = Gtk.TreeViewColumn('اسم الموضع',Gtk.CellRendererText(),text = 0)
        self.tree_sav.append_column(column)
        self.tree_sav.set_model(self.store_sav)
        scroll = Gtk.ScrolledWindow()
        scroll.set_shadow_type(Gtk.ShadowType.IN)
        scroll.add(self.tree_sav)
        remove = asm_customs.ButtonClass("حذف")
        remove.connect('clicked', self.remove_iter)
        hb = Gtk.Box(spacing=5,orientation=Gtk.Orientation.HORIZONTAL)
        hb.pack_start(remove, False, False, 0)
        remove_all = asm_customs.ButtonClass("مسح")
        remove_all.connect('clicked', self.remove_iters)
        hb.pack_start(remove_all, False, False, 0)
        clo = asm_customs.ButtonClass("إغلاق")
        clo.connect('clicked',lambda *a: self.destroy())
        hb.pack_end(clo, False, False, 0)
        box.pack_start(scroll, True, True, 0)
        box.pack_start(hb, False, False, 0)
        area.pack_start(box, True, True, 0)
        self.show_all()