# java.util 하위에 위치
- List : ArrayList, Vector(멀티스레드 환경에서 적합) 두 객체의 동작은 동일
  - 길이 가변
  - Object(고정된 타입이 아닌 다양한 데이터 저장 가능)
  - 순서가 있으며, 중복 데이터 허용
- Set : HashSet
  - 순서가 없으며, 중복 데이터 불가
- Map : HashMap
  - key, value 형식으로 데이터 관리

# Thread vs Runnable
- Thread : 멀티스레드 생성
- Runnable : 단일스레드에 포함
