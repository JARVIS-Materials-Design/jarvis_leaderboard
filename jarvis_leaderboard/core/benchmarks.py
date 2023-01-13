from jarvis.db.jsonutils import loadjson

ai_bench = loadjson("ai_bench.json")


class Benchmarks(object):
    def __init__(
        self,
        bench_name="jv_exfoliation_energy",
        model_name="alignn",
        train_ids=[],
        val_ids=[],
        test_ids=[],
        actual_train_data=[],
        actual_val_data=[],
        actual_test_data=[],
        pred_train_data=[],
        pred_val_data=[],
        pred_test_data=[],
        dataset_name="",
        dataset_version="",
        time_taken=[],
        workflow=[],
        metrics=["mae"],
        language="python",
        platform="linux",
        software_requirements=[],
        hardware_requirements=[],
    ):
        self.bench_name = bench_name
        self.model_name = model_name
        self.train_ids = train_ids
        self.val_ids = val_ids
        self.test_ids = test_ids
        self.actual_train_data = actual_train_data
        self.actual_val_data = actual_val_data
        self.actual_test_data = actual_test_data
        self.pred_train_data = pred_train_data
        self.pred_val_data = pred_val_data
        self.pred_test_data = pred_test_data
        self.dataset_name = dataset_name
        self.dataset_version = dataset_version
        self.time_taken = time_taken
        self.workflow = workflow
        self.metrics = metrics
        self.language = language
        self.platform = platform
        self.software_requirements = software_requirements
        self.hardware_requirements = hardware_requirements

    def run(self):
        print("run workflow")

    def collect_output(self):
        print("collect_output")

    def from_dict(self, d={}):
        print("collect_output")

        return Benchmarks(
            bench_name=d["bench_name"],
            model_name=d["model_name"],
            train_ids=d["train_ids"],
            val_ids=d["val_ids"],
            test_ids=d["test_ids"],
            actual_train_data=d["actual_train_data"],
            actual_val_data=d["actual_val_data"],
            actual_test_data=d["actual_test_data"],
            pred_train_data=d["pred_train_data"],
            pred_val_data=d["pred_val_data"],
            pred_test_data=d["pred_test_data"],
            dataset_name=d["dataset_name"],
            dataset_version=d["dataset_version"],
            time_taken=d["time_taken"],
            workflow=d["workflow"],
            metrics=d["metrics"],
            language=d["language"],
            platform=d["platform"],
            software_requirements=d["software_requirements"],
            hardware_requirements=d["hardware_requirements"],
        )

    def to_dict(self, d={}):
        print("collect_output")

    def analysis(self, d={}):
        print("collect_output")
