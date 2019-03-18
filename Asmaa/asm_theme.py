# -*- coding: utf-8 -*-

##############################################################################
#a########  "قُلۡ بِفَضلِ ٱللَّهِ وَبِرَحمَتِهِۦ فَبِذَٰلِكَ فَليَفرَحُواْ هُوَ خَيرُُ مِّمَّا يَجمَعُونَ"  ########
##############################################################################


from gi.repository import Gtk, Gdk
import asm_config, asm_customs

#a----------------------------------------------------------------------       


class MyTheme(object):
    
    def apply_preference(self, *a):
        
        if asm_config.getv('tr') == '1':
            self.font_tit     = asm_config.getv('font_tit')
            self.font_idx     = asm_config.getv('font_idx')
            self.font_nass    = asm_config.getv('font_nass')
            self.font_qrn     = asm_config.getv('font_qrn')
            self.font_bks     = asm_config.getv('font_bks')
            self.color_tit    = asm_config.getv('color_tit')
            self.color_idx    = asm_config.getv('color_idx')
            self.color_nass   = asm_config.getv('color_nass')
            self.color_qrn    = asm_config.getv('color_qrn')
            self.color_bks    = asm_config.getv('color_bks')
            self.color_bg     = asm_config.getv('color_bg')
            self.color_bgs    = asm_config.getv('color_bgs')
            self.color_sel    = asm_config.getv('color_sel')
            self.color_fnd    = asm_config.getv('color_fnd')
            self.color_bg_sel = asm_config.getv('color_bg_sel')
            self.color_bg_qrn = asm_config.getv('color_bg_qrn')
            
        elif asm_config.getv('tr') == '2':
            self.font_tit     = 'KacstOne 32'
            self.font_idx     = 'KacstOne 18'
            self.font_nass    = 'Amiri Quran 32'
            self.font_qrn     = 'Amiri Quran 32'
            self.font_bks     = 'KacstOne 20'
            self.color_tit    = '#f7f7e6e69494'
            self.color_idx    = '#ffffffffffff'
            self.color_nass   = '#ffffffffffff'
            self.color_qrn    = '#ffffffffffff'
            self.color_bks    = '#ffffffffffff'
            self.color_bg     = '#555555555555'
            self.color_bgs    = '#555555555555'
            self.color_sel    = '#444444444444'
            self.color_fnd    = '#222222222222'
            self.color_bg_sel = '#dddddddddddd'
            self.color_bg_qrn = '#888888888888'
            
        else:
            self.font_tit     = 'KacstOne Bold 20'
            self.font_idx     = 'KacstOne 13'
            self.font_nass    = 'Simplified Naskh 22'
            self.font_qrn     = 'Amiri Quran 23'
            self.font_bks     = 'KacstOne 15'
            self.color_tit    = '#868609091515'
            self.color_idx    = '#868609091515'
            self.color_nass   = '#1bac34a102b8'
            self.color_qrn    = '#202040400000'
            self.color_bks    = '#868609091515'
            self.color_bg     = '#f7d1f3fce63d'
            self.color_bgs    = '#f7d1f3fce63d'
            self.color_sel    = '#ffffffffffff'
            self.color_fnd    = '#fe71fab0870b'
            self.color_bg_sel = '#9e9ec1c17a7a'
            self.color_bg_qrn = '#fcb2eb47aeb5'
    
    def __init__(self):
        self.refresh()
        
    def refresh(self, *a):
        self.apply_preference()
        css_data = '''
        Tree {
        background-color: '''+asm_customs.rgb(self.color_bg)+''';
        background-image: none;
        color: '''+asm_customs.rgb(self.color_bks)+''';
        font: '''+self.font_bks+''';
        }
        Treeindex {
        background-color: '''+asm_customs.rgb(self.color_bgs)+''';
        background-image: none;
        color: '''+asm_customs.rgb(self.color_idx)+''';
        font: '''+self.font_idx+''';
        }
        View:selected,
        Viewbitaka:selected,
        Tree:selected,
        Treeindex:selected {
        background-color: '''+asm_customs.rgb(self.color_bg_sel)+''';
        background-image: none;
        color: '''+asm_customs.rgb(self.color_sel)+''';
        }
        View {
        background-color: '''+asm_customs.rgb(self.color_bg)+''';
        background-image: none;
        color: '''+asm_customs.rgb(self.color_nass)+''';
        font: '''+self.font_nass+''';
        }
        Viewbitaka {
        background-color: '''+asm_customs.rgb(self.color_bgs)+''';
        background-image: none;
        color: '''+asm_customs.rgb(self.color_nass)+''';
        font: KacstOne 13;
        }
        '''
            
        screen = Gdk.Screen.get_default()
        css_provider = Gtk.CssProvider()
        context = Gtk.StyleContext()
        try: css_provider.load_from_data(css_data)
        except: css_provider.load_from_data('')
        context.add_provider_for_screen(screen, css_provider,
                                         Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
