import pheval_exo_rag.core.runner as ck


class RunnerHelper:
    def __init__(self, input_dir, testdata_dir, tmp_dir, output_dir, config_file, version):
        self.runner = ck.Runner()
        self.input_dir = input_dir
        self.testdata_dir = testdata_dir
        self.tmp_dir = tmp_dir
        self.output_dir = output_dir
        self.config_file = config_file
        self.version = version

    def initialize_runner(self):
        self.runner.initialize_data(self.input_dir, self.testdata_dir)
        self.runner.setup_collections(self.tmp_dir, self.output_dir)

    def run_analysis(self):
        self.runner.run_analysis(notFullhpListOfOMIM619340, allfromomim619340)
