import abc

class AbstructBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def build_title(self, title):
        pass

    @abc.abstractmethod
    def build_header(self, header):
        pass

    @abc.abstractmethod
    def build_contents(self, contents):
        pass

    @abc.abstractmethod
    def build_footer(self, footer):
        pass


class HTMLBuilder(AbstructBuilder):

    def build_title(self, title):
        return "<h1>{}</h1>\n".format(title)

    def build_header(self, header):
        return "<header><p>{}</p></header>\n".format(header)

    def build_contents(self, contents):
        html_contents = []
        for content in contents:
            html_contents.append("<p>{}</p>\n".format(content))
        return "".join(html_contents)

    def build_footer(self, footer):
        return "<footer><p>{}</p></footer>\n".format(footer)

class TextBuilder(AbstructBuilder):

    def build_title(self, title):
        return "**{}**\n".format(title)

    def build_header(self, header):
        return "{}\n".format(header)

    def build_contents(self, contents):
        text_contents = []
        for content in contents:
            text_contents.append("{}\n".format(content))
        return "".join(text_contents)

    def build_footer(self, footer):
        return "{}\n".format(footer)
