class Solution:
    def find(self, l, b, h):
        # code here
        surface_area = 2 * (l * b + b * h + h * l)
        volume = l * b * h
        return [surface_area, volume]