"""
App data
"""


class AppData:
    def __init__(self):
        self.allow_client_commands: bool = True
        self.auto_detach: bool = True
        self.cmd: str = ""
        self.elevated: bool = False
        self.exclude_global_prep_cmd: bool = False
        self.exclude_global_state_cmd: bool = False
        self.exit_timeout: int = 5
        self.gamepad: str = ""
        self.image_path: str = ""
        self.name: str = "Aim Lab"
        self.output: str = ""
        self.per_client_app_identity: bool = False
        self.scale_factor: int = 100
        self.state_cmd: list = []
        self.terminate_on_pause: bool = False
        self.use_app_identity: bool = False
        self.virtual_display: bool = False
        self.wait_all: bool = True
        self.working_dir: str = ""
