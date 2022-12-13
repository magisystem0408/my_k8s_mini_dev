import 'dart:async';


StreamController<String> _actionController = StreamController<String>();

StreamTransformer<String, String> transform() {
  return StreamTransformer<String, String>.fromHandlers(
      handleData: (value, sink) {
        sink.add(value + ':ありがとう');
      }
  );
}


void main() {
  _actionController.stream.transform(transform()).listen((value) {
    print(value);
  });

  _actionController.sink.add('新聞だよ');
}