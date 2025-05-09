from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Auth"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Users"),
                "icon": "group",
                "link": reverse_lazy("admin:accounts_user_changelist"),
            },
            {
                "title": _("Group"),
                "icon": "group",
                "link": reverse_lazy("admin:auth_group_changelist"),
            },
        ],
    },
    {
        "title": _("Other"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Order"),
                "icon": "receipt_long",
                "link": reverse_lazy("admin:api_ordermodel_changelist"),
            },
            {
                "title": _("Location"),
                "icon": "location_on",
                "link": reverse_lazy("admin:api_locationmodel_changelist"),
            },
        ],
    },
]
