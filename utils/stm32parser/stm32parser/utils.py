import re
import string

def lcutstrip(string, cut, strip=string.whitespace):
    if string.startswith(cut):
        string = string[len(cut):].lstrip(strip)

    return string

def rcutstrip(string, cut, strip=string.whitespace):
    if string.endswith(cut):
        string = string[: -len(cut)].rstrip(strip)
    return string

def split_comment(line):
    comment = ''
    if '/*' in line:
        line, comment = line.split('/*', maxsplit=1)
        comment = comment.strip().strip('*!</ ')

    return line, comment
    
def strip_unsigned(expr):
    expr = expr.strip()
    
    expr = re.sub(r'^[0-9]UL$', lambda o: o.group(0)[:-2], expr)
    expr = re.sub(r'^[0-9]U$' , lambda o: o.group(0)[:-1], expr)
    
    expr = re.sub(r'0x[0-9A-F]+UL', lambda o: o.group(0)[:-2], expr)
    expr = re.sub(r'[0-9]+UL', lambda o: o.group(0)[:-2], expr)
    
    expr = re.sub(r'0x[0-9A-F]+U' , lambda o: o.group(0)[:-1], expr)
    expr = re.sub(r'[0-9]+U' , lambda o: o.group(0)[:-1], expr)

    return expr