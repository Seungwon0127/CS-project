class HunterEvent:
    """
    사용자 개입에 의해 발생하는 종료 이벤트 클래스.
    특정 키 입력이 들어오면 활성화되고,
    모든 생물 객체를 제거하여 시뮬레이션 종료 조건을 만든다.
    """

    def __init__(self):

        # 이벤트 활성화 여부 (bool)
        self.active = None

        # 이벤트 발생 키 (str)
        self.trigger_key = None

    def trigger(self, key):
        """
        - key와 trigger_key 비교
        - 같으면 active 값을 True로 변경
        """

        pass

    def eliminate_all(self, animals):
        """
        - 모든 생물의 alive 값을 False로 변경
        - 생태계를 강제로 종료
        """

        pass
