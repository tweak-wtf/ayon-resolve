import os

from ayon_core.addon import AYONAddon, IHostAddon

RESOLVE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class ResolveAddon(AYONAddon, IHostAddon):
    name = "resolve"
    host_name = "resolve"

    def initialize(self, module_settings):
        self.enabled = True

    def get_launch_hook_paths(self, app):
        if app.host_name != self.host_name:
            return []
        return [
            os.path.join(RESOLVE_ROOT_DIR, "hooks")
        ]

    def get_workfile_extensions(self):
        return [".drp"]
