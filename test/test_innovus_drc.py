import unittest
import os
import pathlib

from edaac.metrics.parsers import parse_innovus_drc_report


class TestInnovusDRC1(unittest.TestCase):
    def test(self):
        metrics = {
            'drv_total': 22,
            'drv_short_metal_total': 3,
            'drv_short_metal_area': 0.03220000,
            'drv_short_cut_total': 0,
            'drv_short_cut_area': 0.0,
            'drv_out_of_die_total': 0,
            'drv_out_of_die_area': 0.0,
            'drv_spacing_total': 9,
            'drv_spacing_parallel_run_length_total': 5,
            'drv_spacing_eol_total': 4,
            'drv_spacing_cut_total': 0,
            'drv_min_area_total': 10
        }
        result = parse_innovus_drc_report(os.path.join(pathlib.Path(
            __file__).parent.absolute(), 'data', 'drc1.rpt'))
        self.assertDictEqual(metrics, result)


class TestInnovusDRC2(unittest.TestCase):
    def test(self):
        metrics = {
            'drv_total': 76,
            'drv_short_metal_total': 30,
            'drv_short_metal_area': 0.06930000,
            'drv_short_cut_total': 0,
            'drv_short_cut_area': 0.0,
            'drv_out_of_die_total': 0,
            'drv_out_of_die_area': 0.0,
            'drv_spacing_total': 32,
            'drv_spacing_parallel_run_length_total': 19,
            'drv_spacing_eol_total': 13,
            'drv_spacing_cut_total': 0,
            'drv_min_area_total': 14
        }
        result = parse_innovus_drc_report(os.path.join(pathlib.Path(
            __file__).parent.absolute(), 'data', 'drc2.rpt'))
        self.assertDictEqual(metrics, result)


class TestInnovusDRC3(unittest.TestCase):
    def test(self):
        metrics = {
            'drv_total': 333,
            'drv_short_metal_total': 300,
            'drv_short_metal_area': 130.68,
            'drv_short_cut_total': 0,
            'drv_short_cut_area': 0.0,
            'drv_out_of_die_total': 8,
            'drv_out_of_die_area': 0.03050500,
            'drv_spacing_total': 6,
            'drv_spacing_parallel_run_length_total': 5,
            'drv_spacing_eol_total': 1,
            'drv_spacing_cut_total': 0,
            'drv_min_area_total': 19
        }
        result = parse_innovus_drc_report(os.path.join(pathlib.Path(
            __file__).parent.absolute(), 'data', 'drc3.rpt'))
        self.assertDictEqual(metrics, result)



class TestInnovusDRC4(unittest.TestCase):
    def test(self):
        metrics = {
            'drv_total': 101,
            'drv_short_metal_total': 2,
            'drv_short_metal_area': 0.02382500,
            'drv_short_cut_total': 1,
            'drv_short_cut_area': 0.0012500,
            'drv_out_of_die_total': 0,
            'drv_out_of_die_area': 0.0,
            'drv_spacing_total': 41,
            'drv_spacing_parallel_run_length_total': 7,
            'drv_spacing_eol_total': 9,
            'drv_spacing_cut_total': 25,
            'drv_min_area_total': 57
        }
        result = parse_innovus_drc_report(os.path.join(pathlib.Path(
            __file__).parent.absolute(), 'data', 'drc4.rpt'))
        self.assertDictEqual(metrics, result)

