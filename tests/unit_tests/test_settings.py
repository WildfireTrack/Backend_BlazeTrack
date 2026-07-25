from source.config.settings import settings


def test_project_name():
    assert settings.PROJECT_NAME == "BlazeTrack"


def test_project_description():
    assert settings.PROJECT_DESCRIPTION == "Production ready BlazeTrack"


def test_project_version():
    assert settings.PROJECT_VERSION == "0.1.0"


def test_api_v1_str():
    assert settings.API_V1_STR == "/api/v1"


def test_cors_settings_are_lists():
    assert isinstance(settings.ALLOWED_ORIGINS, list)
    assert isinstance(settings.ALLOW_METHODS, list)
    assert isinstance(settings.ALLOW_HEADERS, list)
