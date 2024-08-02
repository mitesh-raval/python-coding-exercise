from assertpy import assert_that

from coding_exercise.application.splitter import Splitter
from coding_exercise.domain.model.cable import Cable


def test_should_not_return_none_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)).is_not_none()


def test_should_raise_error_if_request_violates_times_constraint():
    assert_that(Splitter().split).raises(ValueError) \
                                   .when_called_with(Cable(10, "coconuts"), 0)


def test_should_raise_error_if_request_violates_cable_length_constraint():
    assert_that(Splitter().split).raises(ValueError) \
                                   .when_called_with(Cable(1, "coconuts"), 1)


def test_should_raise_error_if_request_violates_result_length_constraint():
    assert_that(Splitter().split).raises(ValueError) \
                                   .when_called_with(Cable(10, "coconuts"), 10)


def test_example_1_splitting_cable_from_readme():
    expected_result = [Cable(5, "coconuts-0"), Cable(5, "coconuts-1")]

    result = Splitter().split(Cable(10, "coconuts"), 1)

    assert_that(len(result)).is_equal_to(len(expected_result))

    for i in range(len(result)):
        assert_that(result[i].length).is_equal_to(expected_result[i].length)
        assert_that(result[i].name).is_equal_to(expected_result[i].name)


def test_example_2_splitting_cable_from_readme():
    expected_result = [
        Cable(1, "coconuts-0"),
        Cable(1, "coconuts-1"),
        Cable(1, "coconuts-2"),
        Cable(1, "coconuts-3"),
        Cable(1, "coconuts-4")
    ]

    result = Splitter().split(Cable(5, "coconuts"), 2)

    assert_that(len(result)).is_equal_to(len(expected_result))

    for i in range(len(result)):
        assert_that(result[i].length).is_equal_to(expected_result[i].length)
        assert_that(result[i].name).is_equal_to(expected_result[i].name)


def test_example_3_splitting_cable_last_part_unqual():
    expected_result = [
        Cable(3, "coconuts-0"),
        Cable(3, "coconuts-1"),
        Cable(3, "coconuts-2"),
        Cable(1, "coconuts-3"),
    ]

    result = Splitter().split(Cable(10, "coconuts"), 2)

    assert_that(len(result)).is_equal_to(len(expected_result))

    for i in range(len(result)):
        assert_that(result[i].length).is_equal_to(expected_result[i].length)
        assert_that(result[i].name).is_equal_to(expected_result[i].name)


def test_example_4_splitting_cable_name_zerofilled():
    expected_result = [
        Cable(1, "coconuts-00"),
        Cable(1, "coconuts-01"),
        Cable(1, "coconuts-02"),
        Cable(1, "coconuts-03"),
        Cable(1, "coconuts-04"),
        Cable(1, "coconuts-05"),
        Cable(1, "coconuts-06"),
        Cable(1, "coconuts-07"),
        Cable(1, "coconuts-08"),
        Cable(1, "coconuts-09")
    ]

    result = Splitter().split(Cable(10, "coconuts"), 9)

    assert_that(len(result)).is_equal_to(len(expected_result))

    for i in range(len(result)):
        assert_that(result[i].length).is_equal_to(expected_result[i].length)
        assert_that(result[i].name).is_equal_to(expected_result[i].name)
