import sublime
import sublime_plugin

class SmartCommandFallbackCommand(sublime_plugin.TextCommand):
    def run(self, edit, primary=None, fallback=None):
        try:
            if primary:
                self.view.run_command(primary)
        except Exception:
            if fallback:
                self.view.run_command(fallback)
