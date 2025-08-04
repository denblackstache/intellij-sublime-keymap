import sublime
import sublime_plugin

class SmartFormatCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        has_selection = any(not region.empty() for region in self.view.sel())

        if has_selection:
            self.view.run_command("lsp_format_document_range")
        else:
            self.view.run_command("lsp_format_document")
