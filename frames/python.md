

## Collecions Usage

example_index_to_features = collections.defaultdict(list) # 创建一个默认为空list的dict


_PrelimPrediction = collections.namedtuple(  # pylint: disable=invalid-name
      "PrelimPrediction",
      ["feature_index", "start_index", "end_index", "start_logit", "end_logit"])
      
      
all_predictions = collections.OrderedDict()

list[::]