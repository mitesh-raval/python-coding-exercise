from coding_exercise.domain.model.cable import Cable


class Splitter:

    def __validate(self, cable_length, times):
        valid = True

        if cable_length <= 2 or cable_length >= 1024:
            valid = False

        if times < 1 or times > 64:
            valid = False

        if cable_length // (times + 1) < 1:
            valid = False

        if not valid:
            raise ValueError

    def split(self, cable: Cable, times: int) -> list[Cable]:
        self.__validate(cable.length, times)

        equal_parts = times + 1
        parts_length, rem_cable_length = divmod(cable.length, equal_parts)

        # initialize local var, defaulting to zero if there is no remaining
        # last part
        last_part_length = 0

        if rem_cable_length > 0:
            total_new_parts, last_part_length = divmod(rem_cable_length, parts_length)
            equal_parts += total_new_parts

        if last_part_length > 0:
            total_parts = equal_parts + 1
        else:
            total_parts = equal_parts

        # calculate width for cable name formatting with zero filled, right justified id
        part_id_width = len(str(total_parts))

        result = [
            Cable(parts_length, f"{cable.name}-{i:0{part_id_width}}")
            for i in range(equal_parts)
        ]

        if last_part_length > 0:
            result.append(
                Cable(last_part_length, f"{cable.name}-{equal_parts:0{part_id_width}}")
            )

        return result
