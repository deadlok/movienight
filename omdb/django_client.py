from django.conf import settings

from omdb.client import OmdbClient


def get_client_from_settings():
    """Create an instance of an OmdbClient using the OMDB_KEY from the Django settings."""
    print("***KEY")
    print(settings.OMDB_KEY)
    return OmdbClient(settings.OMDB_KEY)
