import abc


class Formatter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def output_report(self, title, text):
        raise NotImplementedError()


class HTMLFormatter(Formatter):
    def output_report(self, title, text):
        print("<html><head><title>{}</title></head>".format(title))
        print("<body>")
        for line in text:
            print("<p>{}</p>".format(line))
        print("</body>")
        print("</html>")


class PlainTextFormatter(Formatter):
    def output_report(self, title, text):
        print("**{}**".format(title))
        for line in text:
            print(" -", line)
