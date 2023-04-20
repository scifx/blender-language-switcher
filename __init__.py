bl_info = {
    "name" : "Language switcher",
    "author" : "SciFX", 
    "description" : "一键切换中英文（Switch between Chinese and English with one click",
    "blender" : (3, 0, 0),
    "version" : (1, 0, 0),
    "location" : "",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "https://github.com/scifx/blender-language-switcher/issues", 
    "category" : "User Interface" 
}


import bpy
import bpy.utils.previews


addon_keymaps = {}
_icons = None
nodetree = {'scifx_lang': False, }


def layout(self, context):
    if not (False):
        layout = self.layout
        op = layout.operator('scifx.operator_0', text='语言', icon_value=0, emboss=False, depress=False)


class scifx_lang_operator(bpy.types.Operator):
    bl_idname = "scifx.operator_0"
    bl_label = "Operator"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        nodetree['scifx_lang'] = not nodetree['scifx_lang']
        if nodetree['scifx_lang']:
            bpy.context.preferences.view.language = 'en_US'
        else:
            bpy.context.preferences.view.language = 'zh_CN'
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.TOPBAR_MT_editor_menus.append(layout)
    bpy.utils.register_class(scifx_lang_operator)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.types.TOPBAR_MT_editor_menus.remove(layout)
    bpy.utils.unregister_class(scifx_lang_operator)
