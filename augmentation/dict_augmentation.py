import os
import exrex
from typing import List
from itertools import product

from prod.dict_parsers.GraphDictParser import GraphDictParser
from prod.dict_parsers.BaseDictParser import BaseDictParser


class DictAugmentation:
    def __init__(self, path: str, files: List[str], graphed: List[bool]):
        self._parsers = {
            True: GraphDictParser,
            False: BaseDictParser
        }
        self.sub_dict = {}

        for file, graphed in zip(files, graphed):
            parser = self._parsers[graphed](filename=os.path.join(path, file))
            self.sub_dict.update(parser.get_dict())

    def augment_string(self, tokenized_string: str, max_num_vars=3):
        new_st = []
        for token in tokenized_string.split():
            if token in self.sub_dict:
                tmp_list = []
                for i in self.sub_dict[token]:
                    for num_var, new_var in enumerate(exrex.generate(s=i)):
                        tmp_list.append(new_var)
                        if num_var >= max_num_vars:
                            break
                new_st.append(tmp_list)
            else:
                new_st.append([token])

        strings = []

        for tup in product(*[range(len(i)) for i in new_st]):
            st = []
            for num, idx in enumerate(tup):
                st.append(str(new_st[num][idx]))
            strings.append(' '.join(st))

        return strings