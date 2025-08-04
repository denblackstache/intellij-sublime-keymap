import sublime
import sublime_plugin

class FindWithSelectionCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("slurp_find_string")
        self.window.run_command("show_panel", {"panel": "find"})

class ReplaceWithSelectionCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("slurp_replace_string")
        self.window.run_command("show_panel", {"panel": "replace"})
