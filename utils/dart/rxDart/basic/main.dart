import 'dart:async';



var controller = StreamController<String>();


void main(){
  streamTest();

  controller.sink.add('完全に猫まむし');
  controller.sink.add('テスト');

}


void streamTest(){
  controller.stream.listen((data){
    print('購読している人1');
    print(data);
  });
}