import os.path
import re
from requests import get

from core.utilities.strings import isolate_string

valid_responses = [200]

type_tuples = [
    ('Supertype', '205.4a', 'The supertypes are', None),
    ('Type', '205.2a', 'The card types are', 'See section 3'),
    ('Land Subtype', '205.3i', 'The land types are', 'Of that list'),
    ('Creature Subtype', '205.3m', 'The creature types are', None),
    ('Artifact Subtype', '205.3g', 'The artifact types are', None),
    ('Enchantment Subtype', '205.3h', 'The enchantment types are', None),
    ('Planeswalker Subtype', '205.3j', 'The planeswalker types are', None),
    ('Instant Subtype', '205.3k', 'The spell types are', None),
    ('Sorcery Subtype', '205.3k', 'The spell types are', None),
]


def get_rules_text(url: str = "https://media.wizards.com/2023/downloads/MagicComp%20Rules%2020230203.txt"):
    response = get(url)
    decoded_text = response.content.decode('utf-8-sig')
    decoded_text = decoded_text.replace('\r', '\n')
    decoded_text = decoded_text.replace('\n\n\n\n', '\n\n\n')
    decoded_text = decoded_text.replace('\n\n\n', '\n\n')
    decoded_text = decoded_text.replace("’", "'")
    return decoded_text


def get_rules_dict(rules_body: str):
    regex = re.compile(r'(.*?) (.*)')

    rule_list = rules_body.split('\n\n')
    rule_dict = dict()
    for rule_line in rule_list:
        match = regex.match(rule_line)
        if match:
            k, v = match.groups()
            rule_dict[k] = v
    return rule_dict


def extract_types(rules_dict: dict[str, str], key: str, truncate_from: str, truncate_to: str = None):
    types_str = isolate_string(rules_dict[key], truncate_from, truncate_to)[:-1]
    types_str = types_str.replace(", and", ",")
    types = types_str.split(', ')

    cleaned_types = list()
    for type_str in types:
        sub_str = type_str[0].upper() + type_str[1:]

        if "(" in sub_str:
            i = sub_str.index("(") - 1
            cleaned_types.append(sub_str[:i])
        else:
            cleaned_types.append(sub_str)
    return cleaned_types


def rule_dict_from_url(url: str = "https://media.wizards.com/2023/downloads/MagicComp%20Rules%2020230203.txt"):
    full_rules = get_rules_text(url)
    rules_body = isolate_string(full_rules, 'Credits', 'Glossary')
    rules_dict = get_rules_dict(rules_body)
    return rules_dict


def gen_type_file_text(rules_dict: dict[str, str]):
    def gen_types() -> str:
        text = """
# region Card Type Types
# https://mtg.fandom.com/wiki/Supertype
# https://media.wizards.com/2023/downloads/MagicComp%20Rules%2020230203.txt, from https://magic.wizards.com/en/rules

"""

        for info_tuple in type_tuples:
            type_var = info_tuple[0].upper().replace(' ', '_')
            rule_num = info_tuple[1]
            types = extract_types(rules_dict, rule_num, info_tuple[2], info_tuple[3])
            formatted_text = format_type_typing(type_var, types)
            text += f"# From Rule {rule_num}\n" + formatted_text

        text += """
SUBTYPE = Union[LAND_SUBTYPE, CREATURE_SUBTYPE, ARTIFACT_SUBTYPE, ENCHANTMENT_SUBTYPE,
                PLANESWALKER_SUBTYPE, INSTANT_SUBTYPE, SORCERY_SUBTYPE]

ANY_TYPE = Union[SUPERTYPE, TYPE, SUBTYPE]
# endregion Card Type Types"""
        return text

    def format_type_typing(var_name: str, types: list[str]):
        line_len = 116
        text = ""
        new_line = "    "
        for type_str in types:
            to_add = f'"{type_str}", '
            if len(to_add) + len(new_line) > line_len:
                text += new_line + '\n'
                new_line = "    " + to_add
            else:
                new_line += to_add
        text += new_line[:-2]

        if text.count('\n') == 0:
            text = text.strip()

        if text.startswith(' '):
            return f"{var_name} = Literal[\n{text}\n]\n\n"
        else:
            return f"{var_name} = Literal[{text}]\n\n"

    def gen_sets():
        text = """
# region Card Type Sets
# Extracting the card types from the data type definitions."""

        for info_tuple in type_tuples:
            var_name = info_tuple[0].upper().replace(' ', '_')
            text += f"{var_name}S: set[{var_name}] = set(get_args({var_name}))\n"

        text += """
SUBTYPE_DICT: dict[TYPE, set[SUBTYPE]] = {
    "Land": LAND_SUBTYPES,
    "Creature": CREATURE_SUBTYPES,
    "Artifact": ARTIFACT_SUBTYPES,
    "Enchantment": ENCHANTMENT_SUBTYPES,
    "Planeswalker": PLANESWALKER_SUBTYPES,
    "Instant": INSTANT_SUBTYPES,
    "Sorcery": SORCERY_SUBTYPES
}
# endregion Card Type Sets"""
        return text

    file_text = "from game_metadata import Literal, Union, get_args"

    return file_text + '\n\n' + gen_types() + '\n\n' + gen_sets() + '\n'


def main():
    rules_dict = rule_dict_from_url()
    type_file_text = gen_type_file_text(rules_dict)
    file_name = "card_types.py"
    cur_dir = os.path.split(__file__)[0]
    target_path = os.path.join(cur_dir, '../..', file_name)
    with open(target_path, 'w') as f:
        f.write(type_file_text)


if __name__ == "__main__":
    main()
