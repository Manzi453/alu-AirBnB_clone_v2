def do_create(self, arg):
    """Create object with params (e.g., 'create Place city_id="0001" name="My_house"')"""
    if not arg:
        print("** class name missing **")
        return

    args = arg.split()
    class_name = args[0]

    if class_name not in HBNBCommand.classes:
        print("** class doesn't exist **")
        return

    kwargs = {}
    for param in args[1:]:
        if '=' not in param:
            continue
        key, value = param.split('=', 1)
        
        # Handle string values
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1].replace('_', ' ').replace('\\"', '"')
        # Handle float values
        elif '.' in value:
            try:
                value = float(value)
            except ValueError:
                continue
        # Handle integer values
        else:
            try:
                value = int(value)
            except ValueError:
                continue
        
        kwargs[key] = value

    new_instance = HBNBCommand.classes[class_name](**kwargs)
    new_instance.save()
    print(new_instance.id)