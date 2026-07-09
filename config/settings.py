from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    media_base_url: str = "http://localhost:8000/static/"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    def build_media_url(self, path: str) -> str:
        return (
            f"{self.media_base_url.rstrip('/')}/{path.lstrip('/')}"
        )


settings = Settings()