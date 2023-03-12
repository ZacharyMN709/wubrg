import os
from itertools import permutations, combinations
from core.colors.color_identity import ColorIdentity


def gen_color_combinations(base):
    ls = list()
    for i in range(0, 6):
        ls += [''.join(x) for x in combinations(base, i)]
    return ls


def gen_colors(base):
    return join_list([x for x in base])


def join_list(ls):
    return '"' + '", "'.join(ls) + '",\n'


def join_list_jump(ls, jump):
    ret = ""
    for i in range(0, len(ls), jump):
        ret += join_list(ls[i:i+jump])
    return ret


def gen_comb(base):
    ret = ""
    for i in range(0, 6):
        ret += join_list([''.join(x) for x in combinations(base, i)])
    return ret


def gen_perm(base):
    ret = ""
    ret += join_list([''.join(x) for x in permutations(base, 0)])
    ret += join_list([''.join(x) for x in permutations(base, 1)])
    ret += join_list_jump([''.join(x) for x in permutations(base, 2)], 4)
    ret += join_list_jump([''.join(x) for x in permutations(base, 3)], 3)
    ret += join_list_jump([''.join(x) for x in permutations(base, 4)], 6)
    ret += join_list_jump([''.join(x) for x in permutations(base, 5)], 6)
    return ret


def gen_splash_combinations():
    color_identity_string = gen_color_combinations('WUBRG')
    splash_identity_string = gen_color_combinations('wubrg')
    ret = gen_comb('wubrg')

    for x in color_identity_string:
        if x == '':
            continue

        x_set = set(x)
        for y in splash_identity_string:
            if len(x_set & set(y.upper())) == 0:
                ret += f'"{x}{y}", '
        ret += '\n'
    return ret


def gen_aliases():
    ret = '"", '
    for c in ColorIdentity:
        ret += join_list(c.get_aliases())
    return ret


def wrap_with_literal(content, var_name):
    ret = f"{var_name} = Literal[\n"
    ret += content
    # Add in 'tabs'
    ret = ret.replace('\n', '\n    ')
    # Trim the last comma, but delete the last new line.
    ret = ret[:-6]
    # Re-add the last new line.
    ret = ret + '\n'
    ret += "]\n\n"

    # If the statement can fit one one line, let it.
    if len(ret) <= 120:
        ret = ret.replace('\n', '').replace('    ', '') + '\n\n'

    return ret


def gen_file_text():
    ret = "from typing import Literal\n\n\n"
    ret += wrap_with_literal(gen_colors('WUBRG'), 'ColorString')
    ret += wrap_with_literal(gen_colors('wubrg'), 'SplashString')
    ret += wrap_with_literal(gen_comb('WUBRG'), 'ColorIdentityString')
    ret += wrap_with_literal(gen_comb('wubrg'), 'SplashIdentityString')
    ret += wrap_with_literal(gen_splash_combinations(), 'ColorCombinationIdentityString')
    ret += wrap_with_literal(gen_aliases(), 'ColorAliasString')
    ret += wrap_with_literal(gen_perm('WUBRG'), 'ColorIdentityScrambledString')
    ret += wrap_with_literal(gen_perm('wubrg'), 'SplashIdentityScrambledString')
    return ret


def main():
    type_file_text = gen_file_text()
    file_name = "color_typing.py"
    cur_dir = os.path.split(__file__)[0]
    target_path = os.path.join(cur_dir, '..', file_name)
    with open(target_path, 'w') as f:
        f.write(type_file_text)


if __name__ == "__main__":
    main()
