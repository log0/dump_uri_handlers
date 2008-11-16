    import os
    import re
    import sys
    from sets import Set

    file = open('/usr/share/gconf/schemas/desktop_gnome_url_handlers.schemas', 'r')
    data = file.read()
    file.close()

    """
    The interesting parts are "applyto" tags. The term between 4th and 5th slash is the URI we want.
    """

    uris = re.compile('([a-zA-Z0-9/\-]+)', re.MULTILINE).findall(data)
    handlers = []

    for uri in uris:
        handler = uri.split('/')[4]
        handlers.append(handler)

    for handler in sorted(Set(handlers)):
        print handler

