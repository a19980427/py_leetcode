from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        sum_area = 0

        point_map = {}

        for rectangle in rectangles:
            sum_area += self.compute_area(rectangle)
            points = self.get_all_points(rectangle)
            for point in points:
                if point_map.get(point, False):
                    point_map[point] += 1
                else:
                    point_map[point] = 1
        return self.is_legal(point_map, sum_area)

    def compute_area(self, rectangle):
        x1, y1, x2, y2 = rectangle
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        return width * height

    def get_all_points(self, rectangle):
        x1, y1, x2, y2 = rectangle
        left_down = (x1, y1)
        left_up = (x1, y2)
        right_down = (x2, y1)
        right_up = (x2, y2)
        return [left_down, left_up, right_down, right_up]

    def is_legal(self, point_map, sum_area):
        single_points_times = 0

        x1_min = float('inf')
        y1_min = float('inf')
        x2_max = -float('inf')
        y2_max = -float('inf')

        for k, v in point_map.items():
            if v == 1:
                single_points_times += 1
                x1_min = min(x1_min, k[0])
                y1_min = min(y1_min, k[1])
                x2_max = max(x2_max, k[0])
                y2_max = max(y2_max, k[1])
            elif v % 2 == 1:
                return False
        return single_points_times == 4 and sum_area == self.compute_area([x1_min, y1_min, x2_max, y2_max])


# def has_overlap(self, rectangleA, rectangleB):
#     a_x1, a_y1, a_x2, a_y2 = rectangleA
#     b_x1, b_y1, ba_x2, b_y2 = rectangleB
#     left = max(a_x1, b_x1)
#     right = min(a_x2, ba_x2)
#     top = min(a_y2, b_y2)
#     bottom = max(a_y1, b_y1)
#     return not (left >= right or bottom >= top)

a = Solution()
a.isRectangleCover([[0, 0, 1, 1], [0, 0, 2, 1], [1, 0, 2, 1], [0, 2, 2, 3]])
