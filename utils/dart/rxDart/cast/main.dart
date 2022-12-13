import 'dart:async';


StreamController<String> controller = StreamController<String>.broadcast();

void main() {
  listener1();
  listener2();

  controller.sink.add('一度の配信で複数人に届ける');
}

void listener1() {
  controller.stream.listen((data) {
    print("リスナー1");
    print(data);
  });
}

void listener2() {
  controller.stream.listen((data) {
    print('リスナー2');
    print(data);
  });
}