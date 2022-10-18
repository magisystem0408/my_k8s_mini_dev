import abc


class Approver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def approve_100yen(self):
        raise NotImplementedError("abstract method")

    @abc.abstractmethod
    def approve_3000yen(self):
        raise NotImplementedError("abstract method")
