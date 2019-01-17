from django.utils.translation import gettext as _


class HelloService:
    """
    Service for generating hello messages
    """

    def sayHello(self, what: str = None):
        if what is None:
            return _('Hello')
        else:
            return _('Hello %(what)s') % {'what': what}

    def echo(self, data: str):
        """
        Returns a string version of data. May raise StringConversionException in case data is not a valid unicode string
        :param data: string to return back
        :return: data string
        """
        return str(data)
