# 개발로그 코드 한 줄 설명서

이 문서는 `1408신승원 - 프로젝트 1주차 개발로그(개별제출).docx`에 작성된 코드만 대상으로 정리한 설명서입니다.

현재 저장소에 있는 최신 코드 전체가 아니라, 개발로그 문서 안에 들어 있던 다음 3개 클래스만 설명합니다.

- `ArcticEnvironment`
- `HunterEvent`
- `IceField`

## 전체 구조

| 클래스 | 역할 |
| --- | --- |
| `ArcticEnvironment` | 전체 생태계 환경을 관리합니다. 턴, 기온, 생물 밀도, 빙하, 사냥 이벤트를 연결합니다. |
| `HunterEvent` | 특정 키 입력이 들어오면 사냥 이벤트를 활성화하고 모든 생물을 제거합니다. |
| `IceField` | 빙하 면적이 턴마다 줄어드는 구조를 관리합니다. |

---

## 1. `ArcticEnvironment`

### 코드

```python
class ArcticEnvironment:
    def __init__(self):
        # 현재 턴 수 (int)
        self.turn = None

        # 현재 기온 (float)
        self.temperature = None

        # 현재 생태계 개체 밀도 (float)
        self.density = None

        # 턴마다 증가하는 온난화 정도 (float)
        self.global_warming_rate = None

        # 빙하 상태를 관리하는 IceField 객체
        self.ice_field = None

        # 사용자 개입 종료 이벤트를 관리하는 HunterEvent 객체
        self.hunter_event = None
```

### 구조 설명

| 코드 | 설명 |
| --- | --- |
| `class ArcticEnvironment:` | `ArcticEnvironment`라는 클래스를 만듭니다. 이 클래스는 전체 시뮬레이션 환경을 관리합니다. |
| `def __init__(self):` | 객체가 처음 생성될 때 자동으로 실행되는 초기화 메서드입니다. |
| `self.turn = None` | 현재 턴 수를 저장할 변수입니다. 아직 실제 값이 없으므로 `None`으로 둡니다. |
| `self.temperature = None` | 현재 기온을 저장할 변수입니다. |
| `self.density = None` | 생태계 개체 밀도를 저장할 변수입니다. |
| `self.global_warming_rate = None` | 턴마다 기온이 얼마나 증가하는지 저장할 변수입니다. |
| `self.ice_field = None` | 빙하 상태를 관리하는 `IceField` 객체를 연결할 자리입니다. |
| `self.hunter_event = None` | 사냥 이벤트를 관리하는 `HunterEvent` 객체를 연결할 자리입니다. |

### 변수 설명

| 변수 | 자료형 의도 | 의미 |
| --- | --- | --- |
| `turn` | `int` | 시뮬레이션이 몇 턴 진행되었는지 나타냅니다. |
| `temperature` | `float` | 현재 기온입니다. |
| `density` | `float` | 빙하 면적 대비 살아 있는 생물 수를 나타내는 값입니다. |
| `global_warming_rate` | `float` | 한 턴이 지날 때마다 증가하는 기온 변화량입니다. |
| `ice_field` | `IceField` | 빙하 면적과 녹는 상태를 관리하는 객체입니다. |
| `hunter_event` | `HunterEvent` | 사용자 개입으로 종료되는 이벤트를 관리하는 객체입니다. |

### `update(self, animals)`

```python
def update(self, animals):
    """
    - turn 증가
    - temperature 변화
    - ice_field의 melt() 호출
    - calculate_density(animals) 호출
    """
    if self.turn is not None:
        self.turn += 1

    if self.temperature is not None and self.global_warming_rate is not None:
        self.temperature += self.global_warming_rate

    if self.ice_field is not None:
        self.ice_field.melt()

    self.calculate_density(animals)

    return None
```

| 코드 | 설명 |
| --- | --- |
| `def update(self, animals):` | 환경 상태를 한 턴 진행하는 메서드입니다. `animals`는 생물 객체 목록입니다. |
| `if self.turn is not None:` | 턴 값이 설정되어 있을 때만 증가시킵니다. |
| `self.turn += 1` | 현재 턴 수를 1 증가시킵니다. |
| `if self.temperature is not None and self.global_warming_rate is not None:` | 기온과 온난화 정도가 둘 다 설정되어 있는지 확인합니다. |
| `self.temperature += self.global_warming_rate` | 현재 기온에 온난화 정도를 더합니다. |
| `if self.ice_field is not None:` | 빙하 객체가 연결되어 있는지 확인합니다. |
| `self.ice_field.melt()` | 빙하 객체의 `melt()` 메서드를 호출해서 빙하 면적을 줄입니다. |
| `self.calculate_density(animals)` | 살아 있는 생물 수와 빙하 면적을 이용해 밀도를 다시 계산합니다. |
| `return None` | 이 메서드는 값을 반환하기보다 객체 내부 상태를 바꾸는 역할을 합니다. |

### `calculate_density(self, animals)`

```python
def calculate_density(self, animals):
    """
    - alive가 True인 생물 수 계산
    - ice_field.area를 이용해 density 계산
    """
    alive_count = sum(1 for animal in animals if getattr(animal, "alive", False))
    area = getattr(self.ice_field, "area", None)

    if area is None or area == 0:
        self.density = None
    else:
        self.density = alive_count / area

    return self.density
```

| 코드 | 설명 |
| --- | --- |
| `def calculate_density(self, animals):` | 생물 밀도를 계산하는 메서드입니다. |
| `alive_count = sum(...)` | `animals` 목록에서 `alive` 값이 `True`인 생물 수를 셉니다. |
| `getattr(animal, "alive", False)` | `animal`에 `alive` 속성이 있으면 그 값을 가져오고, 없으면 `False`로 처리합니다. |
| `area = getattr(self.ice_field, "area", None)` | `ice_field` 객체의 `area` 값을 가져옵니다. 없으면 `None`으로 처리합니다. |
| `if area is None or area == 0:` | 빙하 면적이 없거나 0이면 밀도를 계산할 수 없습니다. |
| `self.density = None` | 계산할 수 없는 상태이므로 밀도를 `None`으로 둡니다. |
| `else:` | 면적이 정상적으로 있을 때 실행됩니다. |
| `self.density = alive_count / area` | 살아 있는 생물 수를 빙하 면적으로 나누어 밀도를 구합니다. |
| `return self.density` | 계산된 밀도를 반환합니다. |

### `handle_event(self, key, animals)`

```python
def handle_event(self, key, animals):
    """
    - hunter_event.trigger(key) 호출
    - hunter_event가 active 상태가 되면 eliminate_all(animals) 호출
    """
    if self.hunter_event is None:
        return None

    self.hunter_event.trigger(key)

    if self.hunter_event.active:
        self.hunter_event.eliminate_all(animals)

    return self.hunter_event.active
```

| 코드 | 설명 |
| --- | --- |
| `def handle_event(self, key, animals):` | 사용자 입력 이벤트를 처리하는 메서드입니다. |
| `if self.hunter_event is None:` | 사냥 이벤트 객체가 연결되어 있는지 확인합니다. |
| `return None` | 이벤트 객체가 없으면 아무 일도 하지 않고 끝냅니다. |
| `self.hunter_event.trigger(key)` | 입력된 키를 사냥 이벤트 객체에 전달합니다. |
| `if self.hunter_event.active:` | 사냥 이벤트가 활성화되었는지 확인합니다. |
| `self.hunter_event.eliminate_all(animals)` | 활성화되었다면 모든 생물을 제거 처리합니다. |
| `return self.hunter_event.active` | 이벤트가 활성화되었는지 반환합니다. |

### `check_end_condition(self)`

```python
def check_end_condition(self):
    """
    반환: True/False
    종료 조건:  ice_field.is_melted() or hunter_event.active가 True
    """
    ice_melted = False
    hunter_active = False

    if self.ice_field is not None:
        ice_melted = self.ice_field.is_melted()

    if self.hunter_event is not None:
        hunter_active = bool(self.hunter_event.active)

    return ice_melted or hunter_active
```

| 코드 | 설명 |
| --- | --- |
| `def check_end_condition(self):` | 시뮬레이션이 끝났는지 확인하는 메서드입니다. |
| `ice_melted = False` | 빙하가 녹았는지 저장하는 임시 변수입니다. 기본값은 `False`입니다. |
| `hunter_active = False` | 사냥 이벤트가 활성화되었는지 저장하는 임시 변수입니다. |
| `if self.ice_field is not None:` | 빙하 객체가 연결되어 있으면 검사합니다. |
| `ice_melted = self.ice_field.is_melted()` | 빙하가 최소 면적까지 줄었는지 확인합니다. |
| `if self.hunter_event is not None:` | 사냥 이벤트 객체가 연결되어 있으면 검사합니다. |
| `hunter_active = bool(self.hunter_event.active)` | `active` 값을 `True` 또는 `False`로 변환합니다. |
| `return ice_melted or hunter_active` | 빙하가 녹았거나 사냥 이벤트가 켜졌으면 종료 조건을 만족합니다. |

---

## 2. `HunterEvent`

### 코드

```python
class HunterEvent:
    def __init__(self):
        # 이벤트 활성화 여부 (bool)
        self.active = None

        # 이벤트 발생 키 (str)
        self.trigger_key = None
```

### 구조 설명

| 코드 | 설명 |
| --- | --- |
| `class HunterEvent:` | 사냥 이벤트를 관리하는 클래스를 만듭니다. |
| `def __init__(self):` | 사냥 이벤트 객체가 생성될 때 실행됩니다. |
| `self.active = None` | 이벤트가 활성화되었는지 저장합니다. 처음에는 값이 없으므로 `None`입니다. |
| `self.trigger_key = None` | 이벤트를 발생시키는 키를 저장합니다. |

### 변수 설명

| 변수 | 자료형 의도 | 의미 |
| --- | --- | --- |
| `active` | `bool` | 사냥 이벤트가 활성화되었는지 나타냅니다. |
| `trigger_key` | `str` | 이벤트를 발생시키는 입력 키입니다. |

### `trigger(self, key)`

```python
def trigger(self, key):
    """
    - key와 trigger_key 비교
    - 같으면 active 값을 True로 변경
    """
    if self.trigger_key is not None and key == self.trigger_key:
        self.active = True

    return self.active
```

| 코드 | 설명 |
| --- | --- |
| `def trigger(self, key):` | 입력된 키가 이벤트 발생 키와 같은지 확인하는 메서드입니다. |
| `if self.trigger_key is not None and key == self.trigger_key:` | 발생 키가 설정되어 있고 입력 키와 같으면 조건이 참입니다. |
| `self.active = True` | 조건이 맞으면 이벤트를 활성화합니다. |
| `return self.active` | 현재 이벤트 활성화 상태를 반환합니다. |

### `eliminate_all(self, animals)`

```python
def eliminate_all(self, animals):
    """
    - 모든 생물의 alive 값을 False로 변경
    - 생태계를 강제로 종료
    """
    for animal in animals:
        if hasattr(animal, "alive"):
            animal.alive = False

    return None
```

| 코드 | 설명 |
| --- | --- |
| `def eliminate_all(self, animals):` | 모든 생물을 제거하는 메서드입니다. |
| `for animal in animals:` | 생물 목록을 하나씩 반복합니다. |
| `if hasattr(animal, "alive"):` | 해당 객체에 `alive` 속성이 있는지 확인합니다. |
| `animal.alive = False` | 생물의 생존 상태를 `False`로 바꿉니다. |
| `return None` | 별도 결과값 없이 내부 객체들의 상태만 바꿉니다. |

---

## 3. `IceField`

### 코드

```python
class IceField:
    def __init__(self):
        # 현재 빙하 면적 (float)
        self.area = None

        # 턴마다 감소하는 빙하 면적 (float)
        self.melt_rate = None

        # 빙하 소멸 기준 면적 (float)
        self.min_area = None
```

### 구조 설명

| 코드 | 설명 |
| --- | --- |
| `class IceField:` | 빙하 상태를 관리하는 클래스를 만듭니다. |
| `def __init__(self):` | 빙하 객체가 생성될 때 실행됩니다. |
| `self.area = None` | 현재 빙하 면적을 저장합니다. 처음에는 `None`입니다. |
| `self.melt_rate = None` | 턴마다 감소하는 빙하 면적을 저장합니다. |
| `self.min_area = None` | 빙하가 소멸했다고 판단할 기준 면적을 저장합니다. |

### 변수 설명

| 변수 | 자료형 의도 | 의미 |
| --- | --- | --- |
| `area` | `float` | 현재 빙하 면적입니다. |
| `melt_rate` | `float` | 한 턴마다 줄어드는 빙하 면적입니다. |
| `min_area` | `float` | 빙하 소멸 또는 최소 유지 기준 면적입니다. |

### `melt(self)`

```python
def melt(self):
    """
    - 현재 area 감소
    - 최소 면적 이하로 감소하지 않도록 처리
    """
    if self.area is None or self.melt_rate is None:
        return None

    self.area -= self.melt_rate

    if self.min_area is not None and self.area < self.min_area:
        self.area = self.min_area

    return self.area
```

| 코드 | 설명 |
| --- | --- |
| `def melt(self):` | 빙하 면적을 줄이는 메서드입니다. |
| `if self.area is None or self.melt_rate is None:` | 현재 면적이나 감소량이 없으면 계산할 수 없습니다. |
| `return None` | 계산하지 않고 종료합니다. |
| `self.area -= self.melt_rate` | 현재 빙하 면적에서 감소량을 뺍니다. |
| `if self.min_area is not None and self.area < self.min_area:` | 최소 면적 기준이 있고, 현재 면적이 그보다 작아졌는지 확인합니다. |
| `self.area = self.min_area` | 최소 면적보다 작아지지 않도록 값을 고정합니다. |
| `return self.area` | 줄어든 뒤의 빙하 면적을 반환합니다. |

### `is_melted(self)`

```python
def is_melted(self):
    """
    반환: True / False
    """
    if self.area is None or self.min_area is None:
        return False

    return self.area <= self.min_area
```

| 코드 | 설명 |
| --- | --- |
| `def is_melted(self):` | 빙하가 기준 면적까지 줄었는지 확인하는 메서드입니다. |
| `if self.area is None or self.min_area is None:` | 현재 면적이나 기준 면적이 없으면 판단할 수 없습니다. |
| `return False` | 판단할 수 없으므로 아직 녹지 않았다고 봅니다. |
| `return self.area <= self.min_area` | 현재 면적이 기준 면적 이하이면 `True`, 아니면 `False`입니다. |

### `contains(self, location)`

```python
def contains(self, location):
    """
    반환: True / False
    """
    if self.area is None or location is None:
        return False

    x, y = location
    side_length = self.area ** 0.5

    return 0 <= x <= side_length and 0 <= y <= side_length
```

| 코드 | 설명 |
| --- | --- |
| `def contains(self, location):` | 특정 위치가 빙하 영역 안에 있는지 확인하는 메서드입니다. |
| `if self.area is None or location is None:` | 빙하 면적이나 위치 정보가 없으면 판단할 수 없습니다. |
| `return False` | 판단할 수 없으므로 영역 밖으로 처리합니다. |
| `x, y = location` | 위치 튜플을 x좌표와 y좌표로 나눕니다. |
| `side_length = self.area ** 0.5` | 빙하 면적을 정사각형으로 보고 한 변의 길이를 계산합니다. |
| `return 0 <= x <= side_length and 0 <= y <= side_length` | x, y가 모두 정사각형 범위 안이면 `True`를 반환합니다. |

---

## 개발로그 코드의 실행 흐름

1. `ArcticEnvironment` 객체가 전체 환경을 관리합니다.
2. `ArcticEnvironment.ice_field`에 `IceField` 객체가 연결됩니다.
3. `ArcticEnvironment.hunter_event`에 `HunterEvent` 객체가 연결됩니다.
4. `update(animals)`가 실행되면 턴과 기온이 바뀌고, 빙하가 녹고, 생물 밀도가 계산됩니다.
5. `handle_event(key, animals)`가 실행되면 입력 키에 따라 사냥 이벤트가 활성화될 수 있습니다.
6. 사냥 이벤트가 활성화되면 모든 생물의 `alive` 값이 `False`가 됩니다.
7. `check_end_condition()`은 빙하가 녹았거나 사냥 이벤트가 활성화되었는지 확인해 종료 여부를 반환합니다.

