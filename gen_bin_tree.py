%%writefile gen_bin_tree.py
"""
Модуль для генерации бинарного дерева в виде словаря.

Вариант: root = 6; height = 5
    left_leaf  = (root * 2) - 2
    right_leaf = root + 4

Каждый узел представлен словарём вида {"значение": [левый, правый]}.
Ключ словаря — строка.
Лист — словарь {"значение": []}.
"""

from typing import Callable, Dict, List, Union

TreeNode = Dict[str, List[Union["TreeNode", list]]]


def left_branch(root: int) -> int:
    """
    Вычислить значение левого потомка.

    :param root: значение родительского узла.
    :return: значение левого потомка по формуле (root * 2) - 2.
    """
    return (root * 2) - 2


def right_branch(root: int) -> int:
    """
    Вычислить значение правого потомка.

    :param root: значение родительского узла.
    :return: значение правого потомка по формуле root + 4.
    """
    return root + 4


def gen_bin_tree(
    height: int = 5,
    root: int = 6,
    l_b: Callable[[int], int] = left_branch,
    r_b: Callable[[int], int] = right_branch,
) -> TreeNode:
    """
    Рекурсивно построить бинарное дерево и вернуть его в виде словаря.

    :param height: высота дерева (неотрицательное целое). По умолчанию 5.
    :param root: значение корневого узла. По умолчанию 6.
    :param l_b: функция вычисления значения левого потомка.
    :param r_b: функция вычисления значения правого потомка.
    :return: словарь, описывающий бинарное дерево.
    :raises ValueError: если height < 0.
    """
    if height < 0:
        raise ValueError("Высота дерева не может быть отрицательной")

    if height == 0:
        return {str(root): []}

    left_subtree = gen_bin_tree(height - 1, l_b(root), l_b, r_b)
    right_subtree = gen_bin_tree(height - 1, r_b(root), l_b, r_b)

    return {str(root): [left_subtree, right_subtree]}


if __name__ == "__main__":
    import pprint
    pprint.pprint(gen_bin_tree(2, 6), width=100)
