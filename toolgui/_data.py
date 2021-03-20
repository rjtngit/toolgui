import toolgui
import configparser
import ast

_UNSET = object()
_LITERALS = (int, float, bool, str)



@toolgui.on_app_start()
def init_default_data():
    for cls in get_all_subclasses(StaticData):
        cls._init()

def get_all_subclasses(cls):
    all_subclasses = []

    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))

    return all_subclasses

class StaticData:
    @classmethod
    def _init(cls):
        cls._defaults = {}
        for var in vars(cls):
            if not var.startswith("_"):
                curval = getattr(cls, var)
                if type(curval) in _LITERALS:
                    cls._defaults[var] = curval

    @classmethod
    def reset(cls):
        for var in vars(cls):
            if not var.startswith("_"):
                curval = getattr(cls, var)
                if type(curval) in _LITERALS:
                    default_val = cls._defaults[var]
                    setattr(cls, var, default_val)

    @classmethod
    def count_values(cls):
        result = 0
        for var in dir(cls):
            if not var.startswith("_"):
                val = getattr(cls, var)
                if val and type(val) in _LITERALS:
                    result += 1
        return result

    @classmethod
    def has_any_values(cls):
        return cls.count_values() > 0


def settings(name):
    """
    @settings(name)

    Decorator to serialize a class's static variables in the toolgui.ini file.
    """
    def dec(settings_class):
        @toolgui.on_app_quit()
        def save_settings():
            config = configparser.ConfigParser()
            config.read("toolgui.ini")
            if not config.has_section(name):
                config.add_section(name)
            for var in dir(settings_class):
                if not var.startswith("_"):
                    val = getattr(settings_class, var)
                    config.set(name, var, repr(val))
            with open("toolgui.ini", 'w+') as configfile:
                config.write(configfile)

        @toolgui.on_app_start()
        def load_settings():
            config = configparser.ConfigParser()
            config.read("toolgui.ini")
            if not config.has_section(name):
                config.add_section(name)
            for var in dir(settings_class):
                if not var.startswith("_"):
                    val = config.get(name, var, fallback=_UNSET)
                    if val is not _UNSET:
                        try:
                            setattr(settings_class, var, ast.literal_eval(val))
                        except ValueError as exc:
                            print(f"Malformed settings data: "
                                  f"{settings_class.__name__}."
                                  f"{var} = {str(val)}")
        return settings_class
    return dec