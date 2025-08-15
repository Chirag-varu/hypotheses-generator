def parse_fact_input(fact_str: str) -> tuple:
    """
    Parse a string like 'has_property(sky, dark)' into a tuple ('has_property', 'sky', 'dark')
    """
    if "(" not in fact_str or not fact_str.endswith(")"):
        raise ValueError("Format must be: predicate(arg1, arg2)")

    predicate, args = fact_str.split("(", 1)
    args = args[:-1]  # remove trailing ')'
    arg_list = [arg.strip() for arg in args.split(",")]

    if len(arg_list) != 2:
        raise ValueError("Must provide exactly 2 arguments.")
    
    return (predicate.strip(), arg_list[0], arg_list[1])
