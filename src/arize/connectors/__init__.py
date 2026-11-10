"""Data source connectors for Deep Research."""

from arize.connectors._stubs import (
    Attachment,
    BaseConnector,
    Document,
    SyncStatus,
)
from arize.connectors.store import KnowledgeStore

__all__ = ["Attachment", "BaseConnector", "Document", "KnowledgeStore", "SyncStatus"]

# Auto-register built-in connectors
import arize.connectors.obsidian  # noqa: F401

try:
    import arize.connectors.gmail  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.gmail_imap  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.gdrive  # noqa: F401
except ImportError:
    pass  # httpx may not be installed

try:
    import arize.connectors.notion  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.granola  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.gcontacts  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.imessage  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.apple_notes  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.apple_music  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.apple_contacts  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.apple_calendar  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.slack_connector  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.outlook  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.imap  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.gcalendar  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.dropbox  # noqa: F401
except ImportError:
    pass  # httpx may not be installed

try:
    import arize.connectors.whatsapp  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.oura  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.apple_health  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.strava  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.spotify  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.google_tasks  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.weather  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.github_notifications  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.hackernews  # noqa: F401
except ImportError:
    pass

try:
    import arize.connectors.news_rss  # noqa: F401
except ImportError:
    pass
