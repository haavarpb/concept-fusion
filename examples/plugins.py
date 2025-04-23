from importlib.metadata import entry_points


def plugin_dataset(config_dict, basedir, sequence, **kwargs):
    return entry_points(group="gradslam.plugin")[config_dict["plugin_name"]].load()(config_dict, basedir, sequence, **kwargs)
