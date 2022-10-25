from algorizum import PlainTextFormatter, HTMLFormatter

"""
アルゴリズムの書き換えを容易にする。
"""


class Report(object):
    def __init__(self, title, text, formatter):
        self.title = title
        self.text = text
        self.formatter = formatter

    def output_report(self):
        self.formatter.output_report(self.title, self.text)


if __name__ == '__main__':
    title = "猫まむし"
    contents = ["goods", "best"]

    plainReport = Report(title, contents, PlainTextFormatter())
    plainReport.output_report()

    print("*" * 10 + "プロセス2" + "*" * 10)
    htmlReport = Report(title, contents, HTMLFormatter())
    htmlReport.output_report()
