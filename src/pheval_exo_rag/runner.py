"""Custom Pheval Runner."""
from dataclasses import dataclass
from pathlib import Path
from pheval.runners.runner import PhEvalRunner
import core.runner as ck
from src.pheval_exo_rag.constants import notFullhpListOfOMIM619340, allfromomim619340



@dataclass
class CustomPhevalRunner(PhEvalRunner):
    """CustomPhevalRunner Class."""

    input_dir: Path
    testdata_dir: Path
    tmp_dir: Path
    output_dir: Path
    config_file: Path
    version: str
    main_system: ck.Runner = None

    def prepare(self):
        """prepare method."""
        main_runner = ck.Runner()
        main_runner.initialize_data()
        main_runner.setup_collections()
        print("preparing")

    def run(self):
        """run method."""
        if self.main_system is not None:
            self.main_system.run_analysis(notFullhpListOfOMIM619340)
            self.main_system.run_analysis(allfromomim619340)
            print("running with custom pheval runner")
        else:
            print("main_system is not initialized")
        print("running with custom pheval runner")

    def post_process(self):
        """post_process method."""
        print("post processing")
