from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.person_cnt_map = {}
        self.length = len(times)
        self.win = [-1] * self.length
        self.check_point = 0

    def q(self, t: int) -> int:
        # 寻找要查找的时间点
        time_index = 0
        while time_index < self.length and self.times[time_index] <= t:
            time_index += 1
        time_index -= 1

        # 没有被计算过,继续计算
        if self.win[time_index] == -1:
            for i in range(self.check_point, time_index + 1):
                cur_person_key = self.persons[i]
                self.person_cnt_map.setdefault(cur_person_key, 0)
                self.person_cnt_map[cur_person_key] += 1
                cur_person_value = self.person_cnt_map[cur_person_key]
                cur_person = (cur_person_key, cur_person_value)

                if i >= 1:
                    pre_win_person_key = self.win[i - 1]
                    pre_win_person_value = self.person_cnt_map[pre_win_person_key]
                    pre_win_person = (pre_win_person_key, pre_win_person_value)
                    self.win[i] = max(cur_person, pre_win_person, key=lambda x: x[1])[0]
                else:
                    self.win[i] = cur_person[0]
            self.check_point = max(self.check_point, time_index + 1)

        print(
            f"t:{t} ,res:{self.win[time_index]}, time_index:{time_index}, range:{self.check_point, time_index} win:{self.win} map:{self.person_cnt_map}")
        return self.win[time_index]


# a = TopVotedCandidate([0, 0, 0, 0, 1], [0, 6, 39, 52, 75])
# res = a.q(45)
# res = a.q(49)
# res = a.q(59)
# res = a.q(68)
# res = a.q(42)
# res = a.q(37)
# res = a.q(99)
# res = a.q(26)


a = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
a.q(3)
a.q(12)
a.q(25)
a.q(15)
a.q(24)
a.q(8)
