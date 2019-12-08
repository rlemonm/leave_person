class LeavePerson():
    """需要请假的人"""
    def __init__(self, person_name, leave_reason, leave_days):
        self.person_name = person_name
        self.leave_reason = leave_reason
        self.leave_days = leave_days

    def get_person_name(self):
        return self.person_name

    def get_leave_reason(self):
        return self.leave_reason

    def get_leave_days(self):
        return self.leave_days

    def set_leader(self, leader):
        self.leader = leader

    def commit_leave(self):
        print(f"{self.get_person_name()}因为{self.leave_reason}需要请假{self.get_leave_days()}天，望批准")
        if self.leader is not None:
            self.leader.handle_request(self)


class Leader():
    """批准请假的人"""
    def __init__(self, name, duty):
        self.name = name
        self.duty = duty
        self.next_request = None

    def get_leader_name(self):
        return self.name

    def get_leader_duty(self):
        return self.duty

    def set_next_request(self, next_request):
        self.next_request = next_request

    def get_next_request(self):
        return self.next_request

    def handle_request(self, LeavePerson):
        pass


class GroupLeader(Leader):
    """小组长"""
    def __init__(self, name, duty):
        super().__init__(name, duty)

    def handle_request(self, LeavePerson):
        if LeavePerson.get_leave_days() <= 2:
            print(f"同意{LeavePerson.get_person_name()}请假，签字人{self.get_leader_name()},{self.get_leader_duty()}")

        next_request = self.get_next_request()
        if next_request is not None:
            next_request.handle_request(LeavePerson)


class Manager(Leader):
    """部门经理"""
    def __init__(self, name, duty):
        super().__init__(name, duty)

    def handle_request(self, LeavePerson):
        if LeavePerson.get_leave_days() > 2:
            print(f"同意{LeavePerson.get_person_name()}请假，签字人{self.get_leader_name()},{self.get_leader_duty()}")

        next_request = self.get_next_request()
        if next_request is not None:
            next_request.handle_request(LeavePerson)


class HR(Leader):
    """人事经理"""
    def __init__(self, name, duty):
        super().__init__(name, duty)

    def handle_request(self, LeavePerson):
        print(f"{LeavePerson.get_person_name()}的请假条已经处理，情况属实，处理人{self.get_leader_name()}")
        next_request = self.get_next_request()


if __name__ == '__main__':
    group_leader = GroupLeader('张三', '组长')
    manager = Manager('李四', '部门经理')
    hr = HR('王五', '人事经理')

    group_leader.set_next_request(manager)
    manager.set_next_request(hr)

    leave_person1 = LeavePerson('小王', '看医生', 1)
    leave_person1.set_leader(group_leader)
    leave_person1.commit_leave()
    print('='*50)
    leave_person2 = LeavePerson('小李', '家里有事', 8)
    leave_person2.set_leader(group_leader)
    leave_person2.commit_leave()
