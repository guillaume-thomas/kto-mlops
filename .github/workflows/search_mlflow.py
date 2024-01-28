import mlflow


def search_last_run_by_experiment_name(experiment_name: str):
    current_experiment = dict(mlflow.get_experiment_by_name(experiment_name))
    experiment_id = current_experiment['experiment_id']
    df = mlflow.search_runs([experiment_id],
                            filter_string="attributes.status = 'FINISHED'",
                            max_results=1,
                            order_by=["attributes.end_time DESC"])
    return df.loc[0, 'run_id']
