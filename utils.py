import sys, re


def get_args() -> dict[str, str]:
    arg_line = ' '.join(sys.argv[1:])

    arg_patterns = {'debug':   r'(-d|--debug)\s+([1-9][0-9]{0,2})',
                    'players': r'(-p|--players)\s+([1-4])',
                    'height': r'(-h|--height)\s+([1-9][0-9]{2,3})',
                    'width': r'(-w|--width)\s+([1-9][0-9]{2,3})'}
    
    args = {}
    for arg_key, arg_pattern in arg_patterns.items():
        matches = re.findall(arg_pattern, arg_line)
        if matches:
            arg_value = matches[0][1]
            args[arg_key] = arg_value
    
    return args
        