import sublime
import sublime_plugin


class ToggleReadonlyModeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    if (self.view.is_read_only()):
      self.view.set_read_only(False)
      self.view.set_status('read_only_mode', 'writeable')
      self.view.window().status_message("View " + str(self.view.file_name()) + " is writeable.")
    else:
      self.view.set_read_only(True)
      self.view.set_status('read_only_mode', 'readonly')
      self.view.window().status_message("View " + str(self.view.file_name()) + " is readonly.")


class ToggleReadonlyListener(sublime_plugin.EventListener):
   def on_load(self, view):
      if view.settings().get('read_only_mode'):
        view.set_read_only(True)
        view.set_status('read_only_mode', 'readonly')
        view.window().status_message("View " + str(view.file_name()) + " is readonly.")
