"""Custom Pheval Runner."""
import json
from dataclasses import dataclass
from pathlib import Path

from pheval.runners.runner import PhEvalRunner
from core import runner
from pheval_exo_rag.constants import notFullhpListOfOMIM619340, allfromomim619340

from pheval_exo_rag.post_process.post_process import generate_pheval_result, PhEvalDiseaseResult


@dataclass
class ExoRagPhevalRunner(PhEvalRunner):

    """CustomPhevalRunner Class."""

    input_dir: Path  #
    testdata_dir: Path
    tmp_dir: Path
    output_dir: Path
    config_file: Path
    version: str

    def __init__(self):
        self.main_runner = None

    def prepare(self):
        """Prepare method."""
        self.main_runner = runner.Runner()
        self.main_runner.initialize_data()
        self.main_runner.setup_collections()
        print("preparing")

    def run(self):
        """Run method."""
        if self.main_runner is not None:
            self.results = self.main_runner.run_analysis(notFullhpListOfOMIM619340)
            print("running with custom pheval runner")
        else:
            print("main_system is not initialized")

    def post_process(self):
        """Post-process method."""
        config = self.load_configuration(self.config_file)

        self.output_dir.mkdir(parents=True, exist_ok=True)

        if self.input_dir_config.disease_analysis and self.results:
            disease_results = self.create_disease_results(self.results)
            generate_pheval_result(
                pheval_result=disease_results,
                sort_order_str=config.get('sort_order', 'asc'),
                output_dir=self.output_dir,
                tool_result_path=Path("disease_results.tsv")
            )
        else:
            print("No results to process")

    @staticmethod
    def create_disease_results(query_results):
        # Convert query results to PhEvalDiseaseResult instances
        return [PhEvalDiseaseResult(disease_name=disease_id, disease_identifier=disease_id, score=distance)
                for disease_id, distance in query_results]

    @staticmethod
    def load_configuration(config_file):
        with open(config_file, 'r') as file:
            return json.load(file)

