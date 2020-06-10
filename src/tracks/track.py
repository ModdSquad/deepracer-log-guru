import math
from src.analyze.visitor import VisitorMap

from src.graphics.track_graphics import TrackGraphics

DISPLAY_BORDER = 0.3

class Track:
    def __init__(self):

        # Fields that the subclass needs to provide to define the track
        self.ui_name = ""
        self.ui_description = ""
        self.ui_length_in_m = 0
        self.ui_width_in_cm = 0
        self.ui_difficulty = ""
        self.private_description = ""
        self.world_name = ""
        self.track_section_dividers = []
        self.track_width = 0
        self.track_waypoints = []

        # Fields that we will populate automatically
        self.drawing_points = []
        self.measured_left_distance = 0.0
        self.measured_middle_distance = 0.0
        self.measured_right_distance = 0.0
        self.min_x = 0.0
        self.max_x = 0.0
        self.min_y = 0.0
        self.max_y = 0.0
        self.mid_x = 0.0
        self.mid_y = 0.0

        self.is_ready = False

    def prepare(self):
        self.assert_sensible_info()
        self.make_last_waypoint_complete_loop()
        self.process_raw_waypoints()
        self.calculate_distances()
        self.calculate_range_of_coordinates()

        self.is_ready = True

    def assert_sensible_info(self):
        track_width_error_in_cm = abs(self.ui_width_in_cm - 100 * self.track_width)

        assert len(self.ui_name) > 5
        assert len(self.ui_description) > 10
        assert 10 < self.ui_length_in_m < 70
        assert 70 < self.ui_width_in_cm < 110
        assert self.ui_difficulty in ["Easy", "Medium", "Hard", "*NONE*"]
        assert len(self.private_description) > 10
        assert len(self.world_name) > 5
        # assert track_width_error_in_cm < 2
        assert len(self.track_waypoints) > 20

        if track_width_error_in_cm > 0.1:
            print("WARNING - UI width is wrong by " + str(round(track_width_error_in_cm)) + " cm for track: " + self.ui_name)
            print(self.ui_width_in_cm, self.track_width)

    def process_raw_waypoints(self):
        section_centers = self.get_section_centers()

        section = "A"
        previous = self.track_waypoints[-2]   # Must be penultimate since last one is same as first one

        (self.min_x, self.min_y) = previous
        (self.max_x, self.max_y) = previous

        for i, w in enumerate(self.track_waypoints):
            # Tracks often contain a repeated waypoint, suspect this is deliberate to mess up waypoint algorithms!
            if previous != w:

                left = self.get_target_point(previous, w, 90, self.track_width / 2)
                right = self.get_target_point(previous, w, -90, self.track_width / 2)

                is_divider = ( i in self.track_section_dividers)
                is_center = ( i in section_centers )

                if is_divider:
                    section = chr(ord(section) + 1)

                self.drawing_points.append(Track.DrawingPoint(left, w, right, is_divider, is_center, section))
                previous = w

                self.consider_new_point_in_area(left)
                self.consider_new_point_in_area(w)
                self.consider_new_point_in_area(right)

        self.mid_x = (self.min_x + self.max_x) / 2
        self.mid_y = (self.min_y + self.max_y) / 2



    def get_section_centers(self):
        centers = []
        previous = 0
        for d in self.track_section_dividers:
            centers.append(round((d + previous)/2))
            previous = d

        centers.append(round((len(self.track_waypoints) + previous) / 2))

        return centers

    def consider_new_point_in_area(self, point):
        (x, y) = point
        self.min_x = min(self.min_x, x)
        self.min_y = min(self.min_y, y)

        self.max_x = max(self.max_x, x)
        self.max_y = max(self.max_y, y)

    def calculate_distances(self):
        previous = self.drawing_points[-1]
        for p in self.drawing_points:
            self.measured_left_distance += self.get_distance_between_points(previous.left, p.left)
            self.measured_middle_distance += self.get_distance_between_points(previous.middle, p.middle)
            self.measured_right_distance += self.get_distance_between_points(previous.right, p.right)
            previous = p

    def calculate_range_of_coordinates(self):
        (self.min_x, self.min_y) = self.drawing_points[0].middle
        self.max_x = self.min_x
        self.max_y = self.min_y

        for p in self.drawing_points:
            (x1, y1) = p.left
            (x2, y2) = p.middle
            (x3, y3) = p.right

            self.min_x = min(self.min_x, x1, x2, x3)
            self.max_x = max(self.max_x, x1, x2, x3)

            self.min_y = min(self.min_y, y1, y2, y3)
            self.max_y = max(self.max_y, y1, y2, y3)

    def make_last_waypoint_complete_loop(self):
        last_point = self.track_waypoints[-1]
        first_point = self.track_waypoints[0]

        (last_x, last_y) = last_point
        (first_x, first_y) = first_point

        if abs(last_x - first_x) > 0.0001 or abs(last_y - first_y) > 0.0001:
            self.track_waypoints.append(first_point)

    def get_target_point(self, start, finish, direction_offset, distance):

        (start_x, start_y) = start
        (finish_x, finish_y) = finish

        direction_in_radians = math.atan2(finish_y - start_y, finish_x - start_x)

        direction_to_target = math.degrees(direction_in_radians) + direction_offset
        radians_to_target = math.radians(direction_to_target)

        x = finish_x + math.cos(radians_to_target) * distance
        y = finish_y + math.sin(radians_to_target) * distance

        return x, y

    def configure_track_graphics(self, track_graphics :TrackGraphics):
        track_graphics.set_track_area(self.min_x - DISPLAY_BORDER, self.min_y - DISPLAY_BORDER, self.max_x + DISPLAY_BORDER, self.max_y + DISPLAY_BORDER)






    def OLD_draw_for_frequency_analysis(self, track_graphics, colour):

        track_graphics.plot_line(self.drawing_points[0].left, self.drawing_points[0].right, 3, colour)
        self._draw_edges(track_graphics, colour)
        for p in self.drawing_points:
            if p.is_divider:
                track_graphics.plot_line(p.left, p.right, 3, colour)

    def OLD_draw_for_route_plotting(self, track_graphics :TrackGraphics, colour):
        track_graphics.plot_line(self.drawing_points[0].left, self.drawing_points[0].right, 3, colour)
        self.draw_track_edges(track_graphics, colour)

        for (i, p) in enumerate(self.drawing_points):
            if i % 10 == 0:
                size = 4
            else:
                size = 2
            track_graphics.plot_dot(p.middle, size, colour)

            if p.is_divider:
                track_graphics.plot_line(p.left, p.right, 3, colour)

            if p.is_center:
                # self._plot_label(track_graphics, p.middle, p.section, 30)
                pass   # NOT WORKING VERY WELL AT CHOOSING GOOD POSITION

    def OLD_plot_label(self, track_graphics :TrackGraphics, point, text, size):
        off_track_point = self.get_target_point((self.mid_x, self.mid_y), point, -180, 1.5 * self.track_width)
        track_graphics.plot_text(off_track_point, text, size)



    def draw_track_edges(self, track_graphics, colour):

        previous_left = self.drawing_points[-1].left
        previous_right = self.drawing_points[-1].right

        for p in self.drawing_points:
            if self.get_distance_between_points(previous_left, p.left) > 0.08:
                track_graphics.plot_line(previous_left, p.left, 3, colour)
                previous_left = p.left
            if self.get_distance_between_points(previous_right, p.right) > 0.08:
                track_graphics.plot_line(previous_right, p.right, 3, colour)
                previous_right = p.right

    def draw_starting_line(self, track_graphics, colour):
        track_graphics.plot_line(self.drawing_points[0].left, self.drawing_points[0].right, 3, colour)

    def draw_section_dividers(self, track_graphics, colour):
        for p in self.drawing_points:
            if p.is_divider:
                track_graphics.plot_line(p.left, p.right, 3, colour)

    def draw_waypoints(self, track_graphics, colour, minor_size, major_size):
        for (i, p) in enumerate(self.drawing_points):
            if i % 10 == 0:
                track_graphics.plot_dot(p.middle, major_size, colour)
            else:
                track_graphics.plot_dot(p.middle, minor_size, colour)

    def draw_grid(self, track_graphics, colour):
        x = self.min_x

        while x < self.max_x:
            track_graphics.plot_line(
                (x, self.min_y),
                (x, self.max_y),
                1,
                colour)
            x += 1

        y = self.min_y

        while y < self.max_y:
            track_graphics.plot_line(
                (self.min_x, y),
                (self.max_x, y),
                1,
                colour)
            y += 1

    def get_distance_between_points(self, first, second):
        (x1, y1) = first
        (x2, y2) = second

        x_diff = x2 - x1
        y_diff = y2 - y1

        return math.sqrt(x_diff * x_diff + y_diff * y_diff)

    class DrawingPoint:
        def __init__(self, left, middle, right, is_divider, is_center, section):
            self.left = left
            self.middle = middle
            self.right = right
            self.is_divider = is_divider
            self.is_center = is_center
            self.section = section

    def get_visitor_map(self, granularity):
        return VisitorMap(self.min_x - DISPLAY_BORDER, self.min_y - DISPLAY_BORDER, self.max_x + DISPLAY_BORDER, self.max_y + DISPLAY_BORDER, granularity)


