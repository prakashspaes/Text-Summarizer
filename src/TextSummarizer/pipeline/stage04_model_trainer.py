from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.model_trainer import ModelTrainer
from TextSummarizer.logging import logger
import os

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()