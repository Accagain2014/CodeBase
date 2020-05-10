

- model_fn  # [model function]  (features, labels, mode, params, config)
    - 返回结果: tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op) # 返回整个模型的loss / train_op
    - 核心接口代码, 定义loss, 定义train_op, 定义输出
        - 参数: features/labels, 依靠tf.estimator.EstimatorSpec.train(input_fn=({'fea_name': 'fea_value'}, labels))


- input_fn
    - 定义好: ({'fea_name': 'fea_value'}, labels)

    
- model_fn
    - train
        - loss
        - train_op
            - optimizer.compute_gradients(loss)
    - eval
        - loss
        - predictions
        - eval_metric_ops
    - predict
        - predictions
        - export_outputs
        
        