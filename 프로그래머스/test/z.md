객관식 1.
아래에는 안드로이드 문제와 iOS문제가 각각 10문제씩 있습니다.

자신이 풀고 싶은 문제가 안드로이드 문제인지 아니면 iOS 문제인지 선택해 주세요.

문제 순서
문제 번호 문제 종류
2번 ~ 11번 안드로이드 문제
12번 ~ 21번 iOS 문제
문제 설명에 본 문제는 (안드로이드/iOS) 문제입니다 라고 적혀있습니다.

주의 사항
자신이 선택하지 않은 문제를 풀면 그 문제는 0점이 됩니다.
예를 들어 안드로이드 문제를 선택하고 iOS문제를 풀면, iOS문제는 0점 처리됩니다.
반대로 iOS문제를 선택하고 안드로이드 문제를 풀면, 안드로이드 문제는 0점 처리됩니다.

만약 아무런 보기도 선택하지 않았을 경우, 자동으로 안드로이드 문제를 선택한 것으로 간주합니다.

①
안드로이드

②
iOS

③
무응답 - 본 항목을 선택하는 경우 모든 문항이 0점 처리 됩니다.

객관식 2.
[본 문제는 안드로이드 문제입니다.]
안드로이드에서 레이아웃을 재사용하는 방법에는 <include/> 및 <merge/> 태그를 사용하여 다른 레이아웃을 현재 레이아웃에 삽입하는 방법이 있다. 아래의 include와 merge의 설명 중 옳지 않은 것을 모두 고르시오.

①
merge는 중복된 뷰 그룹을 포함하는 것을 방지할 수 있다.

②
include 태그를 사용하면 레이아웃 속성을 재정의 할 수 없다.

③
merge는 include태그를 사용하지 않고 사용한다.

④
merge레이아웃을 다른 레이아웃에 포함하면 merge요소가 무시된다.

객관식 3.
[본 문제는 안드로이드 문제입니다.]
안드로이드에서 ViewStub을 사용할 때 얻을 수 있는 장점을 고르시오.

①
코드레벨에서의 로드 없이 바로 사용할 수 있다.

②
merge 태그를 xml에서 같이 사용하여 효과적으로 뷰를 만들 수 있다.

③
필요할 때만 뷰를 로드하여 메모리 사용량을 줄이고 랜더링 속도를 높일 수 있다.

④
자주 사용하는 view에 사용하면 효과적이다.

객관식 4.
[본 문제는 안드로이드 문제입니다.]
Activity Stack에 A-B-C-D Activity들이 있는 상황에서 LaunchMode가 SingleTop으로 설정된 D Activity를 Start 했을 때 일어나는 동작을 고르시오.

①
새로운 D Activity가 생성되며 A-B-C-D-D의 형태로 스택에 적재된다.

②
새로운 D Activity가 생성되지만 onCreate 메소드가 호출된다.

③
새로운 D Activity가 생성되지 않고 onResume 메소드가 호출된다.

④
새로운 D Activity가 생성되지 않고 onNewIntent 메소드가 호출된다.

객관식 5.
[본 문제는 안드로이드 문제입니다.]
안드로이드 Lifecycle에 대한 설명으로 옳지 않은 것을 고르시오.

①
onCreate는 Activity가 생성될 때 실행되며, 필수로 구현해야 하는 메소드다.

②
onStart는 Activity가 시작될 때 실행되며, 사용자와 상호작용할 수 있다.

③
onResume은 Activity가 포그라운드에 들어갈 때 시스템에 의해 호출된다.

④
onPause는 사용자가 Activity를 떠날 때 나타내는 첫 번째 신호로써 호출된다.

객관식 6.
[본 문제는 안드로이드 문제입니다.]
Activity, Fragment의 LifeCycle에 대한 아래의 설명중 옳은 것을 고르시오.

①
Activity나 Fragment가 포그라운드에서 포커스를 얻은 상태에서 부분적으로 가려지면 포커스를 잃고 ‘일시중지 상태'로 전환되며 ‘onPause’가 호출된다.

②
‘일시중지 상태'에서 다시 포그라운드로 돌아오면 ‘onResume’ ‘onPause’가 순차적으로 호출된다.

③
새로운 Activity나 Fragment가 포그라운드로 올라오고 포커스를 갖게 되면서 현재 보이고 있는 Activity나 Fragment를 완전히 가리게 되면 포커스를 잃고 ‘중지’ 상태로 전환되며 ‘onStop’이 호출된다.

④
‘중지' 상태의 동일한 인스턴스가 다시 포그라운드로 돌아오면 시스템은 Activity나 Fragment에 ‘onStart’ ‘onResume’을 차례로 호출한다.

객관식 7.
[본 문제는 안드로이드 문제입니다.]
Intent는 메시징 객체로, 다른 앱 구성요소로부터 작업을 요청하는 데 사용할 수 있다. 아래의 Intent에 대한 것 중 옳지 않은 설명을 고르시오.

①
화면을 구성하는 Activity를 실행하기 위해선, Intent를 startActivity로 전달하며, Intent에는 시작할 Activity와 필수 데이터를 담아야 한다.

②
Intent객체에는 Android 시스템이 어느 구성요소를 시작할지 판별하는 데, 사용하는 정보가 담겨 있다.

③
서비스가 일회성인 경우는 Intent를 bindService에 전달하고, 클라이언트 - 서버 인터페이스로 디자인된 경우에는 Intent를 startService에 전달한다.

④
Intent를 sendBroadcast() 또는 sendOrderedBroadcast()에 전달하면 다른 앱에 브로드캐스트를 전달할 수 있다.

객관식 8.
[본 문제는 안드로이드 문제입니다.]
Intent에는 명시적/ 암시적 두 종류의 Intent가 있다. 각 Intent에 대한 설명중 옳은 것을 모두 고르시오.

①
명시적 인텐트는 일반적으로 앱 밖에서 안드로이드 구성요소를 시작할 때 사용한다.

②
Android API 레벨과 상관없이 암시적 인텐트로 서비스를 시작하는 것이 가능하다.

③
명시적 인텐트는 인텐트를 충족시키기 위해 대상 앱의 패키지명 혹은 완전한 클래스명을 제공해야 한다.

④
암시적 인텐트를 사용하면 Android 시스템에서 시작할 수 있는 구성요소를 찾는다. 이때 인텐트의 내용을 기기에 있는 다른 여러 앱의 매니페스트 파일에 선언된 인텐트 필터와 비교한다.

객관식 9.
[본 문제는 안드로이드 문제입니다.]
Android 구성요소 중 Service는 포그라운드 서비스, 백그라운드 서비스, 바인드 서비스의 형태로 존재한다. 포그라운드 서비스를 실행할 때 고려해야 할 사항을 모두 고르시오.

①
앱이 포그라운드 서비스를 너무 많이 사용하지 않아야 한다.

②
포그라운드 서비스는 상태 표시줄 알람을 표시하고 우선순위가 PRIORITY_DEFAULT 이상이어야 한다.

③
포그라운드 서비스는 사용자가 능동적으로 인식하고 있으므로, 메모리가 부족하더라도 시스템이 중단 후보로 고려할 수 없다.

④
API레벨과 상관없이 FOREGROUND_SERVICE 권한을 요청해야 한다.

객관식 10.
[본 문제는 안드로이드 문제입니다.]
IntentService 클래스는 단일 백그라운드 스레드에서 작업을 실행하기 위한 간단한 구조를 제공한다. IntentService의 제한사항으로 볼 수 없는 것을 고르시오.

①
사용자 인터페이스와 직접 상호작용 할 수 없으므로 결과를 UI에 배치하려면 Activity로 보내야 한다.

②
작업 요청이 순차적으로 실행된다. 작업이 IntentService에서 실행 중일 때 다른 요청을 전송하면, 요청은 첫 번째 작업이 끝날 때까지 대기한다.

③
IntentService에서 실행되는 작업은 중단할 수 없다.

④
필수 콜백 메서드 onStartCommand와 onHandleIntent를 구현해야 한다.

객관식 11.
[본 문제는 안드로이드 문제입니다.]
Android MVVM 아키텍쳐의 ViewModel은 Android 프레임워크에서 제공된다. 이 ViewModel 클래스에 대해 옳은 설명을 고르시오.

①
ViewModel 객체는 뷰 또는 LifeCycleOwners의 특정 인스턴스와 같은 생명주기로 설계되었다.

②
ViewModel 객체는 LiveData와 같이, 수명주기를 인식하는 Observable의 변경 사항을 관찰하여, 비즈니스 로직을 완성할 수 있다.

③
ViewModel이 Finish 될 때, onFinished 메소드가 호출된다.

④
ViewModel의 목적은 UI 컨트롤러의 데이터를 캡슐화하여 구성이 변경되어도 데이터를 유지하는 것이다.

객관식 12.
[본 문제는 iOS 문제입니다.]
ARC에 대한 설명으로 틀린 것을 고르시오.

①
weak으로 참조 시, 레퍼런스 카운트가 증가되지 않는다.

②
메모리에서 방출되는 시점은 강한 참조의 카운트가 0이 되는 시점이다.

③
unowned으로 선언된 변수도 레퍼런스 카운트가 증가되지 않는다.

④
weak은 옵셔널로 받기 때문에, 참조되는 객체가 메모리에서 날아가면 nil로이 된다.

⑤
struct는 강한 참조될 때마다, 레퍼런스 카운트가 증가한다.

객관식 13.
[본 문제는 iOS 문제입니다.]
UIViewController 생명주기에 관한 설명으로 옳지 않은 것은?

①
스토리보드로 커스텀 뷰를 그리는 경우, ViewDidLoad이 불려지기 전에 커스텀 뷰의 속성을 변경하면 크래쉬가 난다.

②
viewWillAppear은 뷰가 단순히 보일 때가 아니라, 해당하는 뷰가 view hierarchy에 더해지는 시점에 발동된다.

③
viewDidLoad가 호출되었을 때, subview의 bounds도 정해진다.

④
viewDidLoad는 해당하는 뷰가 메모리에서 릴리즈 되면, 여러 번 불려질 수도 있다.

⑤
didReceivememoryWarning은 이용 가능 메모리가 낮아졌을 때 불려지는 함수다.

객관식 14.
[본 문제는 iOS 문제입니다.]
Frame과 Bounds의 차이점으로 옳지 않은 것은?

①
Frame을 변화시키면. draw(\_:)을 부르지 않아도 뷰를 다시 보여준다.

②
Frame은 origin과 size으로 이루어진다.

③
Bounds는 frame과 다르게 자신만의 좌표 시스템 안에서 나타내 진다.

④
Bounds의 origin은 디폴트로 (0,0)이다.

⑤
Bounds의 origin을 변경하더라도 subview의 frame은 동일하므로 drawing 되는 위치는 똑같다.

객관식 15.
[본 문제는 iOS 문제입니다.]
Class와 Struct의 차이점으로 옳지 않은 것은?

①
Class는 레퍼런스 타입으로 존재하는 객체를 할당할 때 메모리 주소가 복사되어 할당이 된다.

②
Struct은 값 자체가 복제되어 할당이 되므로, Class처럼 하나의 객체를 공유하는 것은 불가능하다.

③
Struct은 상속이 가능하다.

④
Class는 멀티스레딩 시 접근이 여러 곳에서 올 수 있으므로 적절한 Lock이 필요하다.

⑤
Struct은 value type으로 불변성 구현에 유리하다

객관식 16.
[본 문제는 iOS 문제입니다.]
Optional에 대한 설명으로 옳지 않은 것은?

①
해당하는 값이 존재하지 않을 수 있을 때 쓰는 유형이다.

②
Optional Binding은 래핑 된 값을 새 변수에 조건부로 바인딩하는 것을 의미한다.

③
Optional Chaining은 옵셔널 (Optional)에 속해 있는 nil 일지도 모르는 프로퍼티, 메서드, 서브스크립션 등을 가져오거나 호출할 때 사용할 수 있는 일련의 과정이다.

④
Optional Chaining에서 해당 값이 nil 이어도 프로퍼티, 메서드, 서브 스크립트 등을 호출할 수 있다.

⑤
Forced Unwrapping은 강제로 꺼내는 행위인데, 이때 해당 값이 nil일 경우 런타임 에러를 던지게 된다.

객관식 17.
[본 문제는 iOS 문제입니다.]
다음 중 콘솔에 출력될 숫자로 올바른 것은?

var value = "1"

let printValue = { [value] in
print(value)
}

value = "2"

let newPrintValue = printValue

value = "3"

newPrintValue()

①
1

②
2

③
3

④
컴파일 에러

객관식 18.
[본 문제는 iOS 문제입니다.]
다음 중 콘솔에 출력될 알파벳을 순서대로 나열한 것은?

class Test {
lazy var printA: Int? = {
print("A")
return nil
}()

    func printB() -> Int? {
        print("B")
        return printA ?? 1
    }

    let printC: () -> Int = {
        print("C")
        return 2
    }

}

let test = Test()
test.printB() ?? test.printC()

①
AB

②
BA

③
BAC

④
ABC

객관식 19.
[본 문제는 iOS 문제입니다.]
UIWindow의 기본적으로 정의되어있는 Level에 해당하지 않는 것은?

①
StatusBar

②
Normal

③
Root

④
Alert

객관식 20.
[본 문제는 iOS 문제입니다.]
다음 중 Scene이 활성화 상태에서 User Events에 반응할 수 없는 비활성화 상태로 변할 때 호출되는 SceneDelegate 함수는?

①
sceneDidBecomeActive

②
sceneWillResignActive

③
sceneWillEnterForeground

④
sceneDidEnterBackground

객관식 21.
[본 문제는 iOS 문제입니다.]
lazy에 대한 설명으로 올바르지 않은 것은?

①
let과 함께 쓸 수 없다.

②
thread safe 하지 않다.

③
struct나 class의 property에 사용할 수 있다.

④
computed property에 쓸 수 있다.
