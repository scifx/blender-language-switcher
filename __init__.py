bl_info = {
    "name" : "Language switcher",
    "author" : "SciFX", 
    "description" : "一键切换中英文（Switch between Chinese and English with one click，快捷键Ctrl+Shift+L",
    "blender" : (3, 0, 0),
    "version" : (1, 0, 1),
    "location" : "",
    "warning" : "",
    "doc_url": "https://github.com/scifx/blender-language-switcher", 
    "tracker_url": "https://github.com/scifx/blender-language-switcher/issues", 
    "category" : "User Interface" 
}


import bpy
import bpy.utils.previews


addon_keymaps = {}
_icons = None
language_switcher = {'scifx_language': False, }
class scifx_OT_Operator_1A63E(bpy.types.Operator):
    bl_idname = "scifx.operator_1a63e"
    bl_label = "Operator"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return not False

    def execute(self, context):
        language_switcher['scifx_language'] = not language_switcher['scifx_language']
        if language_switcher['scifx_language']:
            bpy.context.preferences.view.language = 'en_US'
        else:
            bpy.context.preferences.view.language = ('zh_HANS' if (bpy.app.version[0] >= 4) else 'zh_CN')
        bpy.context.preferences.view.use_translate_new_dataname = False
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def scifx_add_to_topbar_mt_editor_menus_E0406(self, context):
    if not (False):
        layout = self.layout
        op = layout.operator('scifx.operator_1a63e', text='语言', icon_value=0, emboss=False, depress=False)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(scifx_OT_Operator_1A63E)
    bpy.types.TOPBAR_MT_editor_menus.append(scifx_add_to_topbar_mt_editor_menus_E0406)
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name='Window', space_type='EMPTY')
    kmi = km.keymap_items.new('scifx.operator_1a63e', 'L', 'PRESS',
        ctrl=True, alt=False, shift=True, repeat=False)
    addon_keymaps['9A500'] = (km, kmi)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(scifx_OT_Operator_1A63E)
    bpy.types.TOPBAR_MT_editor_menus.remove(scifx_add_to_topbar_mt_editor_menus_E0406)
