from approver import Approver
from director import Director


class Proxy(Approver):
    def approve_100yen(self):
        return "OK"

    # こちらの場合のclassに判断してもらう。
    def approve_3000yen(self):
        return Director().approve_3000yen()


if __name__ == '__main__':
    proxy = Proxy()
    print(proxy.approve_100yen())
    print(proxy.approve_3000yen())
