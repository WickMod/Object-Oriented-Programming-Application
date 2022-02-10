from VideoSharing_Repo.AppSettingsRepository import AppSettingsRepository

class AppSettingsService:

    app_repo: AppSettingsRepository

    def __init__(self) -> None:
        self.app_repo = AppSettingsRepository()

    def app_version(self) -> str:
        return self.app_repo.app_version()

    def app_name(self) -> str:
        return self.app_repo.app_name()