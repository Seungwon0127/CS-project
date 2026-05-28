class InteractionEvent:
    def __init__(self):

        #이벤트 종류(str)
        self.event_type = None

        #행동 수행 객체(Animal)
        self.actor = None

        #이벤트 대상 객체(Animal)
        self.target = None

        #이벤트 발생 위치(tuple)
        self.location = None

        #이벤트 성공 여부(bool)
        self.success = None

        #표시 시간(float)
        self.timer = None
    def update(self):
        """
        - 이벤트 상태 갱신
        - 타이머 감소
        """
        if self.timer is not None:
            self.timer -= 1
            if self.timer < 0:
                self.timer = 0

        return None
    def is_finished(self):
        """
        - 이벤트 종료 여부 판단
        - 타이머가 0 이하이면 종료
        """
        if self.timer is None:
            return False

        return self.timer <= 0
