#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

import tkinter as tk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.gridspec import GridSpec
from matplotlib.axes import Axes
from matplotlib.ticker import PercentFormatter

from src.analyze.core.line_fitting import get_linear_regression, get_quadratic_regression, get_cubic_regression
from src.analyze.graph.graph_analyzer import GraphAnalyzer
from src.utils.lists import get_list_of_empty_lists

from src.analyze.core.controls import EpisodeCheckButtonControl, StatsControl, \
    GraphScaleControl, GraphLineFittingControl, EvaluationPairsControl, ShowFinalIterationControl, \
    EpisodeTrainingRewardTypeControl


class AnalyzeTrainingProgress(GraphAnalyzer):

    def __init__(self, guru_parent_redraw, matplotlib_canvas: FigureCanvasTkAgg, control_frame: tk.Frame):

        super().__init__(guru_parent_redraw, matplotlib_canvas, control_frame)

        self.episode_control = EpisodeCheckButtonControl(guru_parent_redraw, control_frame, True)
        self._stats_control = StatsControl(guru_parent_redraw, control_frame)
        self._scale_control = GraphScaleControl(guru_parent_redraw, control_frame)
        self._line_fitting_control = GraphLineFittingControl(guru_parent_redraw, control_frame)
        self._evaluation_pairs_control = EvaluationPairsControl(guru_parent_redraw, control_frame)
        self._final_iteration_control = ShowFinalIterationControl(guru_parent_redraw, control_frame)
        self._episode_reward_type_control = EpisodeTrainingRewardTypeControl(guru_parent_redraw, control_frame)

    def build_control_frame(self, control_frame):
        self.episode_control.add_to_control_frame()
        self._stats_control.add_to_control_frame()
        self._scale_control.add_to_control_frame()
        self._line_fitting_control.add_to_control_frame()
        self._evaluation_pairs_control.add_to_control_frame()
        self._final_iteration_control.add_to_control_frame()
        self._episode_reward_type_control.add_to_control_frame()

    def add_plots(self):
        if not self.all_episodes:
            return

        gs = self.graph_figure.add_gridspec(1, 2, left=0.08, right=0.98, bottom=0.08, top=0.92)

        axes_left: Axes = self.graph_figure.add_subplot(gs[0, 0])
        axes_right: Axes = self.graph_figure.add_subplot(gs[0, 1])

        self.create_plot_iteration_vs_total_reward(axes_left)
        self.create_plot_iteration_vs_percent_complete(axes_right)

    def create_plot_iteration_vs_total_reward(self, axes):
        # Plot data

        if self.all_episodes and self.episode_control.show_all():
            if self._stats_control.show_median():
                self.add_plot_iteration_vs_total_reward(axes, "All - Median", self.all_episodes, np.median, "C5")
            if self._stats_control.show_mean():
                self.add_plot_iteration_vs_total_reward(axes, "All - Mean", self.all_episodes, np.mean, "C6")
            if self._stats_control.show_best():
                self.add_plot_iteration_vs_total_reward(axes, "All - Best", self.all_episodes, np.max, "C7")
            if self._stats_control.show_worst():
                self.add_plot_iteration_vs_total_reward(axes, "All - Worst", self.all_episodes, np.min, "C8")

        if self.filtered_episodes and self.episode_control.show_filtered():
            if self._stats_control.show_median():
                self.add_plot_iteration_vs_total_reward(axes, "Filtered - Median", self.filtered_episodes, np.median, "C1")
            if self._stats_control.show_mean():
                self.add_plot_iteration_vs_total_reward(axes, "Filtered - Mean", self.filtered_episodes, np.mean, "C2")
            if self._stats_control.show_best():
                self.add_plot_iteration_vs_total_reward(axes, "Filtered - Best", self.filtered_episodes, np.max, "C3")
            if self._stats_control.show_worst():
                self.add_plot_iteration_vs_total_reward(axes, "Filtered - Worst", self.filtered_episodes, np.min, "C4")

        if self.episode_control.show_evaluations() and self._episode_reward_type_control.measure_total_event_rewards():
            if self._stats_control.show_median():
                self.add_plot_iteration_vs_evaluation_total_reward(axes, "Evaluations - Median", self.evaluation_phases, np.median, "C9")
            if self._stats_control.show_mean():
                self.add_plot_iteration_vs_evaluation_total_reward(axes, "Evaluations - Mean", self.evaluation_phases, np.mean, "C10")
            if self._stats_control.show_best():
                self.add_plot_iteration_vs_evaluation_total_reward(axes, "Evaluations - Best", self.evaluation_phases, np.max, "C11")
            if self._stats_control.show_worst():
                self.add_plot_iteration_vs_evaluation_total_reward(axes, "Evaluations - Worst", self.evaluation_phases, np.min, "C12")

        # Format the plot
        if self._episode_reward_type_control.measure_total_event_rewards():
            axes.set_title("Total Event Reward Per Episode")
        elif self._episode_reward_type_control.measure_max_future_reward():
            axes.set_title("Max Future Reward Per Episode")
        else:
            assert self._episode_reward_type_control.measure_mean_future_reward()
            axes.set_title("Mean Future Reward Per Episode")

        axes.set_xlabel("Training Iteration")

        if self.log_meta and self.is_fixed_scale():
            best = self.log_meta.episode_stats.best_reward
            worst = self.log_meta.episode_stats.worst_reward
            if best != worst:
                border = 0.02 * (best - worst)
                axes.set_ybound(worst - border, best + border)

        if axes.has_data():
            axes.legend(frameon=True, framealpha=0.8, shadow=True)

    def create_plot_iteration_vs_percent_complete(self, axes):

        # Plot data
        if self.episode_control.show_all():
            if self._stats_control.show_median():
                self.add_plot_iteration_vs_percent_complete(axes, "All - Median", self.all_episodes, np.median, "C5")
            if self._stats_control.show_mean():
                self.add_plot_iteration_vs_percent_complete(axes, "All - Mean", self.all_episodes, np.mean, "C6")
            if self._stats_control.show_best():
                self.add_plot_iteration_vs_percent_complete(axes, "All - Best", self.all_episodes, np.max, "C7")
            if self._stats_control.show_worst():
                self.add_plot_iteration_vs_percent_complete(axes, "All - Worst", self.all_episodes, np.min, "C8")

        if self.filtered_episodes and self.episode_control.show_filtered():
            if self._stats_control.show_median():
                self.add_plot_iteration_vs_percent_complete(axes, "Filtered - Median", self.filtered_episodes, np.median, "C1")
            if self._stats_control.show_mean():
                self.add_plot_iteration_vs_percent_complete(axes, "Filtered - Mean", self.filtered_episodes, np.mean, "C2")
            if self._stats_control.show_best():
                self.add_plot_iteration_vs_percent_complete(axes, "Filtered - Best", self.filtered_episodes, np.max, "C3")
            if self._stats_control.show_worst():
                self.add_plot_iteration_vs_percent_complete(axes, "Filtered - Worst", self.filtered_episodes, np.min, "C4")

        if self.episode_control.show_evaluations():
            if self._stats_control.show_median():
                self.add_plot_iteration_vs_evaluation_percent_complete(axes, "Evaluations - Median", self.evaluation_phases, np.median, "C9")
            if self._stats_control.show_mean():
                self.add_plot_iteration_vs_evaluation_percent_complete(axes, "Evaluations - Mean", self.evaluation_phases, np.mean, "C10")
            if self._stats_control.show_best():
                self.add_plot_iteration_vs_evaluation_percent_complete(axes, "Evaluations - Best", self.evaluation_phases, np.max, "C11")
            if self._stats_control.show_worst():
                self.add_plot_iteration_vs_evaluation_percent_complete(axes, "Evaluations - Worst", self.evaluation_phases, np.min, "C12")

        # Format the plot
        axes.set_title("Track Completion")
        axes.set_xlabel("Training Iteration")
        axes.yaxis.set_major_formatter(PercentFormatter())

        if self.is_fixed_scale():
            axes.set_ybound(0, 105)

        if axes.has_data():
            axes.legend(frameon=True, framealpha=0.8, shadow=True)

    def is_fixed_scale(self):
        return self._scale_control.fixed_scale()

    def add_plot_iteration_vs_total_reward(self, axes: Axes, label, episodes, stat_method, colour):
        show_final_iteration = self._final_iteration_control.show_final_iteration()
        (plot_x, plot_y) = get_plot_data_iteration_vs_total_reward(episodes, stat_method, show_final_iteration,
                                                                   self._episode_reward_type_control)
        self.plot_data_or_smooth_it(axes, label, plot_x, plot_y, colour)

    def add_plot_iteration_vs_evaluation_total_reward(self, axes: Axes, label, evaluation_phases, stat_method, colour):
        (plot_x, plot_y) = self.get_plot_data_iteration_vs_evaluation_total_reward(evaluation_phases, stat_method)
        self.plot_data_or_smooth_it(axes, label, plot_x, plot_y, colour)

    def add_plot_iteration_vs_percent_complete(self, axes: Axes, label, episodes, stat_method, colour):
        show_final_iteration = self._final_iteration_control.show_final_iteration()
        (plot_x, plot_y) = get_plot_data_iteration_vs_percent_complete(episodes, stat_method, show_final_iteration)
        self.plot_data_or_smooth_it(axes, label, plot_x, plot_y, colour)

    def add_plot_iteration_vs_evaluation_percent_complete(self, axes: Axes, label, evaluation_phases, stat_method, colour):
        (plot_x, plot_y) = self.get_plot_data_iteration_vs_evaluation_percent_complete(evaluation_phases, stat_method)
        self.plot_data_or_smooth_it(axes, label, plot_x, plot_y, colour)

    def plot_data_or_smooth_it(self, axes: Axes, label: str, plot_x: np.ndarray, plot_y: np.ndarray, colour: str):
        if self._line_fitting_control.linear_fitting():
            (x_values, y_values, r) = get_linear_regression(plot_x, plot_y)
        elif self._line_fitting_control.quadratic_fitting():
            (x_values, y_values) = get_quadratic_regression(plot_x, plot_y)
        elif self._line_fitting_control.cubic_fitting():
            (x_values, y_values) = get_cubic_regression(plot_x, plot_y)
        else:
            x_values = plot_x
            y_values = plot_y

        axes.plot(x_values, y_values, colour, label=label)
        self._plot_solo_items(axes, x_values, y_values, colour)

    def get_plot_data_iteration_vs_evaluation_total_reward(self, evaluation_phases, stat_method):
        plot_iteration = []
        plot_data = []

        previous_eval = None
        for i, this_eval in enumerate(evaluation_phases):
            if self._evaluation_pairs_control.show_combined() and i % 2 == 1:
                plot_value = stat_method(np.concatenate((this_eval.rewards, previous_eval.rewards)))
                plot_data.append(plot_value)
                plot_iteration.append(i - 0.5)
            elif ((self._evaluation_pairs_control.show_odd() and i % 2 == 1) or
                  (self._evaluation_pairs_control.show_even() and i % 2 == 0) or
                  self._evaluation_pairs_control.show_separate()):

                plot_data.append(stat_method(this_eval.rewards))
                plot_iteration.append(i)

            previous_eval = this_eval

        return np.array(plot_iteration), np.array(plot_data)

    def get_plot_data_iteration_vs_evaluation_percent_complete(self, evaluation_phases, stat_method):
        plot_iteration = []
        plot_data = []

        previous_eval = None
        for i, this_eval in enumerate(evaluation_phases):
            if self._evaluation_pairs_control.show_combined() and i % 2 == 1:
                plot_value = stat_method(np.concatenate((this_eval.progresses, previous_eval.progresses)))
                plot_data.append(plot_value)
                plot_iteration.append(i - 0.5)
            elif ((self._evaluation_pairs_control.show_odd() and i % 2 == 1) or
                  (self._evaluation_pairs_control.show_even() and i % 2 == 0) or
                  self._evaluation_pairs_control.show_separate()):

                plot_data.append(stat_method(this_eval.progresses))
                plot_iteration.append(i)

            previous_eval = this_eval

        return np.array(plot_iteration), np.array(plot_data)


def get_plot_data_iteration_vs_total_reward(episodes, stat_method, show_final_iteration: bool,
                                            reward_control: EpisodeTrainingRewardTypeControl):
    iteration_count = episodes[-1].iteration + 1

    # Gather all the rewards into a list per iteration
    iteration_reward = get_list_of_empty_lists(iteration_count)
    for e in episodes:
        if reward_control.measure_total_event_rewards():
            iteration_reward[e.iteration].append(e.total_reward)
        elif reward_control.measure_max_future_reward():
            iteration_reward[e.iteration].append(np.max(e.discounted_future_rewards[0]))
        else:
            assert reward_control.measure_mean_future_reward()
            iteration_reward[e.iteration].append(np.mean(e.discounted_future_rewards[0]))

    if not show_final_iteration:
        iteration_count -= 1
        iteration_reward = iteration_reward[:-1]

    # Build the plot data using numpy to get the average percent for each iteration
    plot_iteration = np.arange(0, iteration_count)
    plot_total_reward = np.zeros(iteration_count)
    for i, ir in enumerate(iteration_reward):
        if ir:
            plot_total_reward[i] = stat_method(np.array(ir))
        else:
            plot_total_reward[i] = np.nan

    return plot_iteration, plot_total_reward


def get_plot_data_iteration_vs_percent_complete(episodes, stat_method, show_final_iteration: bool):
    iteration_count = episodes[-1].iteration + 1

    # Gather all the percentage completions into a list per iteration
    iteration_percent_complete = get_list_of_empty_lists(iteration_count)
    for e in episodes:
        iteration_percent_complete[e.iteration].append(e.percent_complete)

    if not show_final_iteration:
        iteration_count -= 1
        iteration_percent_complete = iteration_percent_complete[:-1]

    # Build the plot data using numpy to get the average percent for each iteration
    plot_iteration = np.arange(0, iteration_count)
    plot_percent_complete = np.zeros(iteration_count)
    for i, ipc in enumerate(iteration_percent_complete):
        if ipc:
            plot_percent_complete[i] = stat_method(np.array(ipc))
        else:
            plot_percent_complete[i] = np.nan

    return plot_iteration, plot_percent_complete


